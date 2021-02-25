from __future__ import annotations
from abc import ABC, abstractmethod

import os
import time

HOME_DIR = os.getenv("HOME")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
#print(DIR_PATH)

import sys

import metaverse
import metaverse.architectures.arch_factory as arch_factory
import metaverse.architectures.actr_cmu.cmuactr_factory as cmu_factory

_DEBUG = True

class AbstractExperiment(ABC):
    """
    The Experiment class defines the basic steps required of all
    experiments regardless of target environment or task. Specific
    routines for registered environments extend this class.
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def start(self):
        """Logic to initialize the experimental parameters"""
        pass

    @abstractmethod
    def run(self):
        """Run the experiment"""
        pass

    @abstractmethod
    def stop(self):
        """Logic to clean up the experimental parameters"""
        pass

    @abstractmethod
    def report(self):
        """General metrics from model and environment"""
        pass

import metaverse.utils.loggers as log
import metaverse.architectures as architectures


class Experiment(AbstractExperiment):
    """Experiment class handles interaction between Model and Environment.

    """

    def __init__(self, model, env, name="", map=None):

        self.name = name
        self.model = model
        self.env = env

        self.model.env = self.env
        self.env.model = self.model


        # TODO: Need Try/Catch since architecture and environment are mandatory;
        #  should fail if either are None

        if _DEBUG:
            print(f"Agent: {model}")
            print(f"Environment: {env}")

        observation_space = self.env.getObservationSpace()
        print(f"Observation space: {observation_space}")

        action_space = self.env.getActionSpace()
        print(f"Action space: {action_space}")

        # TODO: try if env is GymEnv

        if observation_space is not None:
            self.model.perception.setObservationSpace(observation_space)
        if action_space is not None:
            self.model.motor.setActionSpace(action_space)
        if map is not None:
            self.model.perception.obs_map = map


    def load(self, filename=""):
        """Load the parameters from a json file"""

        print("Testing " + self.arch + " in environment " + self.env)

        # factory = arch_factory.AbstractFactory

    def save(self, savefilename=None):
        """Should write the current parameters to a json file"""

        self.filename = savefilename+".json"

        if savefilename is None:
            self.filename = self.name+".json"

        print(f"Saving experiment to: {self.filename}")


    def start(self, filename,dir=DIR_PATH+"/results/"):
        """Start transcript, appending print output to given filename"""
        time = get_timestr()
        self.outfile = dir+filename+"_"+time+".log"
        print(f"Logging experiment to {self.outfile}")
        sys.stdout = log.Transcript(self.outfile)

    def stop(self):
        """Stop transcript and return print functionality to normal"""
        self.model.shutdown()
        print(f"Shutting down experiment at {self.outfile}")

        self.env.close()

        sys.stdout.logfile.close()
        sys.stdout = sys.stdout.terminal


    def run(self, maxtrials=1, maxsteps=-1, asynch=False):
        """Running experiments go through six (6) steps:
            1: get state from environment
            2: present state to agent perception
            3: trigger cognitive cycle in agent
            4: get motor action from agent
            5: present motor action to environment
            6: trigger cycle in environment
        """

        print(f"Starting Experiment with {maxtrials} trials of {maxsteps} steps each.")

        # 1: get state from environment to initialize
        self.obs = self.env.getLastObservation()
        self.model.perception.update_model_action(self.obs)
        #print(f"Experiment:run() sees :{self.obs}")

        import subprocess
        import threading

        if asynch: #run asynchronously
            pass
            #agent_thread = subprocess.Popen(self.agent.run(100, True))
        step = 0
        trial = 0

        #self.agent.run()

        while step != maxsteps and trial < maxtrials:
            #check to see if environment is done
            while not self.env.done:
                print(f"step: {step}")
                #2: present state to agent perception as self.obs
                self.model.last_observation = self.obs
                #3: trigger cognitive cycle in agent
                self.model.step()
                #4: get motor action from agent
                self.next_action = self.model.motor.next_action
                #print(f"Experiment:run() does :{self.next_action}")
                #5: present motor action to environment
                # if self.next_action:
                self.env.next_action = self.next_action
                #6: trigger cycle in environment
                self.env.step()
                # 1: get state from environment to
                # time.sleep(0.05)
                self.obs = self.env.getLastObservation()
                #print(f"Experiment:run() sees :{self.obs}")
                self.model.perception.update_model_action(self.obs)
                step = step + 1
                time.sleep(0.1)

            else: #environment in solved state; reset
                trial = trial + 1
                print(f"Trial {trial}, Number of steps {step}")
                step = 0
                self.env.reset()
                self.obs = self.env.getLastObservation()
                #self.agent.reset()
                self.model.perception.update_model_action(self.obs)
                self.model.step()

    def report(self):
        """define some kind of pretty print report on all the stats.

            Inputs: choice of reports to generate

            Outputs: pretty print output of reports, or raw logs
                - Environment: TBD
                - Model: TBD
                - Stats: TBD
        """

        print(f"Reporting on outfile: {self.outfile}")
        parser = log.Parser(self.outfile)
        parser.importACTR()


def get_timestr():
    """get_timestr() returns a formatted date-time stamp for incremental log files."""

    return time.strftime("%Y%m%d-%H%M%S")

if __name__ == '__main__':

    loadFile = "cmu_count_test.json"
    saveFile = "cmu_count_test.log"

    #unittest()
    # exp = Experiment()
    #
    # exp.load(loadFile)
    #
    # exp.start()
    # exp.run()
    # exp.stop()
    #
    # exp.save(saveFile)