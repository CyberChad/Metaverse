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
import metaverse.architectures.actr_cmu.actr_cmu_factory as cmu_factory

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

import metaverse.utils.loggers as log
import metaverse.architectures as architectures


class Experiment(AbstractExperiment):

    def __init__(self, model, env, name=""):

        self.name = name
        self.model = model
        self.env = env

        if _DEBUG:
            print(f"Model: {model}")
            print(f"Environment: {env}")

        # Need Try/Catch since architecture and environment are mandatory
        # fails if either are None

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


    def start(self, filename):
        """Start transcript, appending print output to given filename"""
        sys.stdout = log.Transcript(filename)

    def stop():
        """Stop transcript and return print functionality to normal"""
        sys.stdout.logfile.close()
        sys.stdout = sys.stdout.terminal

    def run(self, steps=1):

        result = self.model.run(steps)
        print(result)

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