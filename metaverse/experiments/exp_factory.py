from __future__ import annotations
from abc import ABC, abstractmethod

import os
import time
import logging
from datetime import datetime
import numpy as np

log = logging.getLogger("metaverse")

HOME_DIR = os.getenv("HOME")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
#print(DIR_PATH)

import sys

import metaverse
import metaverse.architectures.arch_factory as arch_factory
import metaverse.architectures.actr_cmu.cmuactr_factory as cmu_factory

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

    @abstractmethod
    def set_parameters(self, iv=None, start_val=None, end_val=None, inc=None):
        """Trial parameters:
        """
        pass




import metaverse.utils.scribe as scribe

import metaverse.architectures as architectures


class Experiment(AbstractExperiment):
    """Experiment class handles interaction between Model and Environment.

    """

    def __init__(self, model, env, name="", map=None, events=None):

        self.name = name
        self.model = model
        self.env = env

        self.model.env = self.env
        self.env.model = self.model
        self.events = events

        #Stats for reporting
        # TODO: move this into a proper structure

        self.trials_count = 0
        self.trials_time = 0

        self.steps_count = 0
        self.steps_time = 0

        self.start_time = 0
        self.stop_time = 0

        self.do_iv_test = False
        self._iv = None #independent variable
        self._iv_low = None #iv starting value
        self._iv_high = None #iv ending value
        self._iv_inc = None #iv increment amount per trial

        # TODO: Need Try/Catch since architecture and environment are mandatory;
        #  should fail if either are None

        # if _DEBUG:
        logging.info(f"Agent: {model}")
        logging.info(f"Environment: {env}")

        self.map = map

        self.observation_space = self.env.getObservationSpace()
        print(f"Observation space: {self.observation_space}")

        self.action_space = self.env.getActionSpace()
        print(f"Action space: {self.action_space}")

        # TODO: try if env is GymEnv

        if self.observation_space is not None:
            self.model.perception.setObservationSpace(self.observation_space)
        if self.action_space is not None:
            self.model.motor.setActionSpace(self.action_space)
        if self.map is not None:
            self.model.perception.obs_map = self.map

    def set_parameters(self, iv=None, iv_low=None, iv_high=None, iv_inc=None):
        """Trial parameters:
        """
        self._iv = iv
        self._iv_low = iv_low
        self._curr_iv_inc = iv_low
        self._iv_high = iv_high
        self._iv_inc = iv_inc

        print("Experiment():set_parameters()")
        print(f"Independent Variable: {self._iv}")
        print(f"Low value: {self._iv_low}")
        print(f"High value: {self._iv_high}")
        print(f"Increment: {self._iv_inc}")

        if self._iv and self._iv_low and self._iv_high and self._iv_inc:
            self.do_iv_test = True

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

        self.start_time = datetime.now()
        self.outfile = dir+filename+"_"+get_timestr()+".log"
        print(f"Logging experiment to {self.outfile}")
        sys.stdout = scribe.Transcript(self.outfile)


    def stop(self):
        """Stop transcript and return print functionality to normal"""
        self.stop_time = datetime.now()
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
        self.max_trials = maxtrials
        self.max_steps = maxsteps

        self.obs = self.env.getLastObservation()
        self.model.perception.update_model_action(self.obs)
        #print(f"Experiment:run() sees :{self.obs}")

        import subprocess
        import threading

        if asynch: #run asynchronously
            pass
            #agent_thread = subprocess.Popen(self.agent.run(100, True))
        step = 0
        clock = 0
        trial = 0

        self.exp_rewards = 0
        self.trial_rewards = np.zeros((maxtrials, ), dtype=np.int32)




        #self.agent.run()

        while trial < maxtrials:
            #check to see if environment is done
            while not self.env.done and not self.model.done and step <= maxsteps:
                log.info(f"Experiment.step(): Trial: {trial} Step: {step}")
                clock_time = (clock+1) * 0.05
                print(f"[STEP] {format(clock_time, '.2f')}")
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
                clock = clock + 1
                time.sleep(0.05)

            else: #environment or agent are in solved state; reset
                self.trial_rewards[trial] = self.env.episode_reward
                trial = trial + 1
                print(f"Trial {trial}, Number of steps {step}")
                step = 0
                #if testing an IV then update model
                if self.do_iv_test and (self._curr_iv_inc <= self._iv_high):
                    print(f"Experiment:run()._curr_iv_inc: {self._curr_iv_inc}")
                    self._curr_iv_inc += self._iv_inc
                    if "ps" in self._iv:
                        self.model._clock = self._curr_iv_inc
                self.model.reset()
                self.env.reset()
                self.obs = self.env.getLastObservation()

                if self.observation_space is not None:
                    self.model.perception.setObservationSpace(self.observation_space)
                if self.action_space is not None:
                    self.model.motor.setActionSpace(self.action_space)
                if self.map is not None:
                    self.model.perception.obs_map = self.map


                #self.agent.reset()
                self.model.perception.update_model_action(self.obs)
                self.model.step()

    def report(self, arch=None, test_iv="all"):
        """define some kind of pretty print report on all the stats.

            Inputs: choice of reports to generate

            Outputs: pretty print output of reports, or raw logs
                - Environment: TBD
                - Model: TBD
                - Stats: TBD
        """

        #try to get arch from the model
        if arch is None:
            arch = self.model.arch

        #Report on experiment

        print("*****************************************")
        print("***********   RESULTS   *****************")
        print("*****************************************")

        print("\n------------------------------------")
        print("Experiment Results")
        print("------------------------------------")

        #print(f"{self.scribe.experiment.load.filename})
        print(f"Start Time: {self.start_time}")
        print(f"Stop Time: {self.stop_time}")

        running_time = self.stop_time - self.start_time
        print(f"Runnig Time: {running_time}")

        print(f"Number of Trials: {self.max_trials}")

        print(f"Running Time: {self.trials_time}")

        print(f"Number of Steps: {self.steps_count}")
        print(f"Steps Time: {self.steps_time}")

        print(f"Log File: {self.outfile}")

        print("\n------------------------------------")
        print("Environment Results")
        print("------------------------------------")

        print(f"Name: {self.env.name}")
        #print(f"Type: {self.env.env_name}")

        avg_reward = self.trial_rewards.mean()
        print(f"Average Reward: {avg_reward}")



        print("\n------------------------------------")
        print("Agent Results")
        print("------------------------------------")
        print(f"Name: ")
        print(f"Type: ")

        return self.outfile

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