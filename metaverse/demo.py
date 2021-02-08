from __future__ import annotations
from cmd import Cmd
import importlib
import sys
import os

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

from metaverse.experiments import *

from subprocess import *

from metaverse import director

from metaverse.architectures import arch_factory
from metaverse.architectures.actr_cmu.actr_cmu_factory import CmuActrFactory

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

        psych_envs = ['Counting']
        gym_envs = ['CartPole-v0', 'MountainCar-v1', 'LunarLander-v1']  # TODO: create env registry
        sc2_envs = ['MoveToBeacon']  # TODO: replace with Gym versions

        print(f"Environments Registry: {psych_envs} {gym_envs} {sc2_envs}")

        architectures = ['CMUACTR', 'CCMACTR', 'Soar', 'Nengo']  # TODO: create arch registry
        print("Architecture Registry: " + str(architectures))

        print("Starting Psych Model experiments...")

        import metaverse.architectures.actr_cmu.actr_cmu_factory as cmu_factory
        import metaverse.architectures.soar.soar_factory as soar_factory

        factory_switch = {
            "CMUACTR": cmu_factory.CmuActrFactory(),
            "SOAR" : soar_factory.SoarFactory()
        }

        model_switch = {
            "CMUACTR": "cmu_count_test.lisp",
            "SOAR": "notsureyet"
        }

        arch_list = ['CMUACTR', 'SOAR']

        for arch in arch_list:
            factory = factory_switch.get(arch, arch_factory.AbstractFactory)
            modelFile = model_switch.get(arch)  # TODO: load from experiment config
            model = factory.createModel()
            model.load(modelFile)  # TODO: rename to load()?


            """
            *************************************
                Choose architecture sub-options for:
            *************************************
                    > Declarative Memory
                    > Procedural Memory
                    > Others??
            """

            model.workingMemory = factory.createWorkingMemory()
            model.declarativeMemory = factory.createDeclarativeMemory()
            model.proceduralMemory = factory.createProceduralMemory()
            model.perception = factory.createPerception()
            model.motor = factory.createMotor()


            from metaverse.environments.env_factory import Environment

            myenv = Environment()

            """
            Configure environment-specific options:
            > map or challenge
            > single or multi-agent
            > difficulty rating
            """


            myexp = Experiment(model, myenv)
            myexp.run()



if __name__ == '__main__':

    # prompt = MyPrompt()
    # prompt.prompt = 'Thesis> '
    # prompt.cmdloop('Starting Metaverse prompt...')

    prompt = MyPrompt()
    prompt.do_demo()
    #print(os.environ['PYTHONPATH'])
    #for l in sys.path:
#        print(l)


    # myexp = Experiment()
    # myexp.run_all()



