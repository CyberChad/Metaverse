from __future__ import annotations
from cmd import Cmd
import importlib
import sys
import os

import logging
import logging.config

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

#from Utils.parsers import XMLParser
from multiprocessing import Process
import threading
import queue
from abc import ABC, abstractmethod

import metaverse
import metaverse.architectures
import metaverse.environments
import metaverse.experiments
from metaverse.experiments.exp_factory import Experiment

import metaverse.architectures.actr_cmu.cmuactr_factory as cmu_factory
import metaverse.architectures.soar.soar_factory as soar_factory
import metaverse.architectures.actr_ccmsuite.ccmsuite_factory as ccm_factory

from metaverse.environments.env_factory import SimpleEnvironment, GymEnvironment

from metaverse.experiments import *

from subprocess import *

from metaverse import director

from metaverse.architectures import arch_factory
from metaverse.architectures.actr_cmu.cmuactr_factory import CmuActrFactory

from metaverse.architectures.soar.soar_factory import SoarFactory

import xml.etree.ElementTree as ET
import subprocess
import time
import psutil
import os

import click

CMUACTR_PATH = "/home/chad/ACT-R/" #TODO: replace this with env variable or config
SOAR_PATH = "" #not sure if this is necessary with SoarLibs

#xmlParser = XMLParser()
#xmlParser.__init__("Counting.metamind")

#Client thread for human intervention

"""
Based on http://docs.python.org/howto/logging.html#configuring-logging
"""
dictLogConfig = {
    "version": 1,
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler",
            "formatter": "myFormatter",
            "filename": "config.log"
        }
    },
    "loggers": {
        "metaDemo": {
            "handlers": ["fileHandler"],
            "level": "INFO",
        }
    },

    "formatters": {
        "myFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    }
}

def loadFromXML(file):

    tree = ET.parse(file)
    # print(tree)
    root = tree.getroot()
    print(root.tag)

    for elem in root:
        print(elem.tag, elem.attrib)
        # for subelem in elem:
            # print(subelem.text)

    return tree

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def check_process_image(self, procName=""):
    imgName = "act-r-64"
    notResponding = 'Not Responding'

    r = checkIfProcessRunning(imgName)

    if not r:
        print('%s: No such process, starting...' % (imgName))
        print("Starting CMU ACT-R Dispatcher...")

        c = CMUACTR_PATH + "run-act-r.command"


        #sub_cmd = subprocess.Popen(CMUACTR_PATH + "run-act-r.command", shell=True, stdout=subprocess.PIPE)
        # handle = Popen(CMUACTR_PATH + "run-act-r.command", shell=True, stdin=PIPE, stderr=PIPE, stdout=PIPE)
        # print(handle.stdout.read())
        # handle.flush()

        # pid = os.fork()
        # if pid:
        #     #parent
        #     time.sleep(10)
        # else:
        #     #child
        #     #subprocess.call(CMUACTR_PATH + "run-act-r.command")
        #     p = Process(target=to_use_in_separate_process, args=(CMUACTR_PATH+'run-act-r.command'))
        #     #p.run()
        #     #p.start()


    else:
        print('%s: process is already running.' % (imgName))

def to_use_in_separate_process(*args):
    print(args)

    # check args before using them:
    if len(args) > 1:
        subprocess.call((args[0], args[1]))
        print('subprocess called')

def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    print ('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            print ('%s in r[i]' %(name))
            return r[i]
    return []

# **************************************
#           MAIN CMD LOOP
# **************************************

class MyPrompt(Cmd):
    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True

    def do_add(self, inp):
        print("Adding '{}'".format(inp))

    def help_add(self):
        print("Add a new entry to the system.")

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting")
        raise SystemExit

    def do_shell(self, line):
        "Run a shell command"
        print("running shell command:", line)
        sub_cmd = subprocess.Popen(line,shell=True,stdout=subprocess.PIPE)
        output = sub_cmd.communicate()[0]
        print(output)
        self.last_output = output

    def do_start(self, line=""):
        "Start an architecture"
        print("running an architecture:", line)
        check_process_image(line)

    def do_reload(self, line=""):
        "Reload a module"
        print("Reloading:", line)
        try:
            importlib.reload(metaverse.demo)
            importlib.reload(metaverse.experiments.experiments)
            importlib.reload(metaverse.architectures)

        except TypeError:
            print("Oops! Couldn't reload...")

    def do_listmods(self, line=""):
        "List python modules"
        list = sys.modules
        print(sys.modules)


    def do_run(self, line=""):
        """run an experiment."""

        try:
            arch, env = [str(s) for s in line.split()]
            print(f"Architecture: {arch}")
            print(f"Environment: {env}")

            myexp = Experiment(arch, env)
            myexp.run_all()

        except ValueError:
            print("Run command usage: run <arch> <env>")

    def do_demo(self, line=""):
        """Run the demo with multiple options."""

        psych_tests = ['Counting']
        gym_tests = ['CartPole-v0', 'MountainCar-v1', 'LunarLander-v1']  # TODO: create env registry
        sc2_tests = ['MoveToBeacon']  # TODO: replace with Gym versions

        env_list = [psych_tests, gym_tests, sc2_tests]

        #print(f"Environments Registry: {psych_envs} {gym_envs} {sc2_envs}")

        architectures = ['CMUACTR', 'CCMACTR', 'Soar', 'Nengo']  # TODO: create arch registry
        print("Architecture Registry: " + str(architectures))

        print("Starting Psych Model experiments...")



        factory_switch = {
            "CMUACTR": cmu_factory.CmuActrFactory(),
            "SOAR" : soar_factory.SoarFactory(),
            "CCMSUITE" : ccm_factory.CcmFactory()
        }

        model_switch = {
            "CMUACTR": "cmu_count_test.lisp",
            "SOAR": "soar_agent.config",
            "CCMSUITE" : ""
        }

        arch_list = ['CMUACTR', 'SOAR', 'CCMSUITE']

        for env in env_list:
#            print(f"Environment: {env}")
            for test in env:
                for arch in arch_list:
                    print(f"Running {arch} on {test} test.")
                    #TODO: call to experiment

def test_cmu_counting():

    # test CMU ACT-R Counting
    factory = cmu_factory.CmuActrFactory()
    model = factory.createModel()
    model.load("/tests/psych/count_test.lisp")

    myenv = SimpleEnvironment("counting")

    myexp = Experiment(model, myenv, "CMU Counting")
    myexp.start("cmu_count_test") # appends to a log file
    myexp.run(1, 6)
    myexp.stop() #closes log file
    # myexp.report()


def test_cmu_cartpole():

    # test CMU ACT-R Counting
    factory = cmu_factory.CmuActrFactory()
    model = factory.createModel()

    model.load("/tests/gym/cartpole.lisp")

    myenv = GymEnvironment("CartPole-v0") #TODO: pass registered gym.env_id??

    myexp = Experiment(model, myenv, "CMU Gym Cartpole")
    myexp.start("cmu_cartpole") # appends to a log file
    myexp.run(10, 195) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    #myexp.report()

def test_cmu_starcraft():

    # test CMU ACT-R Counting
    factory = cmu_factory.CmuActrFactory()
    model = factory.createModel()

    model.load("/tests/gym/cartpole.lisp")

    myenv = GymEnvironment("CartPole-v0") #TODO: pass registered gym.env_id??

    myexp = Experiment(model, myenv, "CMU Gym Cartpole")
    myexp.start("cmu_cartpole") # appends to a log file
    myexp.run(10, 195) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    #myexp.report()


def test_soar_counting():

    # test CMU ACT-R Counting

    factory = soar_factory.SoarFactory()
    #modelFile = model_switch.get(arch)  # TODO: load from experiment config
    model = factory.createModel()

    model.load("soar_agent.config")

    myenv = SimpleEnvironment("counting")

    myexp = Experiment(model, myenv, "Soar Counting")
    myexp.start("soar_counting") # appends to a log file
    #myexp.run(12)
    myexp.run(1, 12)
    myexp.stop() #closes log file



def test_soar_cartpole():

    # test CMU ACT-R Counting
    factory = soar_factory.SoarFactory()
    model = factory.createModel()

    model.load("cart-pole.soar","cart-pole")

    myenv = GymEnvironment("CartPole-v0") #TODO: pass registered gym.env_id??

    myexp = Experiment(model, myenv, "Soar Gym Cartpole")
    myexp.start("soar_cartpole") # appends to a log file
    myexp.run(50, 195) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    #myexp.report()

def test_ccm_counting():

    # test CMU ACT-R Counting
    factory = ccm_factory.CcmFactory()
    model = factory.createModel()
    model.load('metaverse.architectures.actr_ccmsuite.counting_prods')
    model.working.addWME('add 5 2 count:None sum:None')

    #TODO: move these to a config file
    model.declarative.addWME('count 0 1')
    model.declarative.addWME('count 1 2')
    model.declarative.addWME('count 2 3')
    model.declarative.addWME('count 3 4')
    model.declarative.addWME('count 4 5')
    model.declarative.addWME('count 5 6')
    model.declarative.addWME('count 6 7')
    model.declarative.addWME('count 7 8')

    myenv = SimpleEnvironment("counting")

    myexp = Experiment(model, myenv, "CMU Counting")
    myexp.start("ccm_count_test") # appends to a log file
    myexp.run(1, 10)
    myexp.stop() #closes log file
    # myexp.report()

def test_ccm_cartpole():

    # test CMU ACT-R Counting
    factory = ccm_factory.CcmFactory()
    model = factory.createModel()

    model.load('metaverse.architectures.actr_ccmsuite.cartpole_prods')

    myenv = GymEnvironment("CartPole-v0") #TODO: pass registered gym.env_id??

    myexp = Experiment(model, myenv, "CCM Gym Cartpole")
    myexp.start("ccm_cartpole") # appends to a log file
    myexp.run(10, 195) #if no cycles provided, env determines end state
    myexp.stop() #closes log file


if __name__ == '__main__':

    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger("metaDemo")

    logger.info("------ Program started -------")
    logger.info("Done!")

    # prompt = MyPrompt()
    # prompt.prompt = 'Thesis> '
    # prompt.cmdloop('Starting Metaverse prompt...')

    # prompt = MyPrompt()
    # prompt.do_demo()

    #myexp = Experiment()
    # myexp.run_all()

    #----------------------------------------
    #           CMU ACT-R Tests
    # ----------------------------------------

    # print("*** START CMU COUNTING ***")
    # time.sleep(1)
    # test_cmu_counting()
    # time.sleep(1)
    #
    # print("*** START CMU CARTPOLE ***")
    # time.sleep(1)
    # test_cmu_cartpole()
    # time.sleep(1)

    print("*** START CMU StarCraft ***")
    time.sleep(1)
    test_cmu_starcraft()
    time.sleep(1)


    # ----------------------------------------
    #           Soar Tests
    # ----------------------------------------

    # print("*** START SOAR COUNTING ***")
    # time.sleep(1)
    # test_soar_counting()
    # time.sleep(1)

    # print("*** START Soar CARTPOLE ***")
    # time.sleep(1)
    # test_soar_cartpole()
    # time.sleep(1)

    # ----------------------------------------
    #           CCMSuite3 ACT-R Tests
    # ----------------------------------------

    # print("*** START CCMSuite3 COUNTING ***")
    # time.sleep(1)
    # test_ccm_counting()
    # time.sleep(1)

    # print("*** START CCMSuite3 CartPole ***")
    # time.sleep(1)
    # test_ccm_cartpole()
    # time.sleep(1)