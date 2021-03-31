from __future__ import annotations
from cmd import Cmd
import importlib
import sys
import os

import yaml
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
import metaverse.utils.scribe as scribe

from metaverse.experiments.exp_factory import Experiment

import metaverse.architectures.actr_cmu.cmuactr_factory as cmu_factory
import metaverse.architectures.soar.soar_factory as soar_factory
import metaverse.architectures.actr_ccmsuite.ccmsuite_factory as ccm_factory

import metaverse.environments.env_factory as env_factory
from metaverse.environments.env_factory import SimpleEnvironment, GymEnvironment, StarCraftEnvironment

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
        "metaverse": {
            "handlers": ["fileHandler"],
            "level": "INFO"
        }
    },

    "formatters": {
        "myFormatter": {
            "format": "%(name)s : %(levelname)s : %(message)s"
        }
    }
}

#"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

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

# --------------------------
#       CMU ACT-R Tests
# --------------------------
def test_cmu_counting():

    # test CMU ACT-R Counting
    factory = cmu_factory.CmuActrFactory()
    model = factory.createModel()
    model.load("/tests/psych/count_test.lisp")

    myenv = SimpleEnvironment(name="counting")

    myexp = Experiment(model, myenv, "CMU Counting")
    myexp.start("cmu_count_test") # appends to a log file
    myexp.run(1, 50)
    myexp.stop() #closes log file
    myexp.report("ACTR")

def test_cmu_cartpole():

    # test CMU ACT-R Counting
    factory = cmu_factory.CmuActrFactory()
    model = factory.createModel()

    model.load("/tests/gym/cartpole.lisp")

    map = ['cart_pos', 'cart_vel', 'pole_pos', 'pole_vel']
    #model.perception.setObservationSpace(map)

    myenv = GymEnvironment("CartPole-v0") #TODO: pass registered gym.env_id??

    model.motor.next_action = 0

    myexp = Experiment(model, myenv, "CMU Gym Cartpole", map)
    myexp.start("cmu_cartpole") # appends to a log file
    myexp.run(10, 195) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    myexp.report("ACTR")

def test_cmu_starcraft():

    # test CMU ACT-R Counting
    factory = cmu_factory.CmuActrFactory()
    model = factory.createModel()
    map = ['beacon_x', 'beacon_y']
    #model.perception.setObservationSpace(map)

    model.load("/tests/sc2/gym_sc2-beacons-simple.lisp")

    myenv = StarCraftEnvironment("SC2MoveToBeacon-v1")
    myexp = Experiment(model, myenv, "CMU StarCraft Beacons",map)

    model.motor.next_action = [-1, -1]

    myexp.start("cmu_beacons") # appends to a log file
    myexp.run(1, 100) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    myexp.report("ACTR")

# --------------------------
#       Soar Tests
# --------------------------

def test_soar_counting():

    # test CMU ACT-R Counting

    factory = soar_factory.SoarFactory()
    #modelFile = model_switch.get(arch)  # TODO: load from experiment config
    model = factory.createModel()

    model.load("soar_agent.config")

    trials = 1
    steps = 11

    myenv = SimpleEnvironment("counting", maxsteps=steps)

    myexp = Experiment(model, myenv, "Soar Counting")
    myexp.start("soar_counting") # appends to a log file
    #myexp.run(12)
    myexp.run(trials, steps)
    myexp.stop() #closes log file
    myexp.report("Soar")

def test_soar_cartpole():

    # test CMU ACT-R Counting
    factory = soar_factory.SoarFactory()
    model = factory.createModel()

    model.load("cart-pole.soar","cart-pole")

    myenv = GymEnvironment("CartPole-v0") #TODO: pass registered gym.env_id??

    myexp = Experiment(model, myenv, "Soar Gym Cartpole")
    model.perception.create_input_wmes

    myexp.start("soar_cartpole") # appends to a log file
    myexp.run(10, 195) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    myexp.report("Soar")

def test_soar_starcraft():

    # test CMU ACT-R Counting
    factory = soar_factory.SoarFactory()
    model = factory.createModel()

    model.load("starcraft2.soar","starcraft")

    myenv = StarCraftEnvironment("SC2MoveToBeacon-v1")
    myexp = Experiment(model, myenv, "Soar StarCraft Beacons")

    model.motor.next_action = [-1, -1]

    myexp.start("soar_beacons") # appends to a log file
    myexp.run(1, 100) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    myexp.report("Soar")

# --------------------------
#       CCM ACT-R Tests
# --------------------------

def test_ccm_counting():

    # test CMU ACT-R Counting
    factory = ccm_factory.CcmFactory()
    model = factory.createModel()
    model.load('metaverse.architectures.actr_ccmsuite.counting_prods')
    model.working.addWME('add 5 2 count:None sum:None')

    #TODO: move these to a config file
    model.declarative.addDM('count 0 1')
    model.declarative.addDM('count 1 2')
    model.declarative.addDM('count 2 3')
    model.declarative.addDM('count 3 4')
    model.declarative.addDM('count 4 5')
    model.declarative.addDM('count 5 6')
    model.declarative.addDM('count 6 7')
    model.declarative.addDM('count 7 8')
    model.declarative.addDM('count 8 9')
    model.declarative.addDM('count 9 10')

    myenv = SimpleEnvironment("counting")

    myexp = Experiment(model, myenv, "CMU Counting")
    myexp.start("ccm_count_test") # appends to a log file
    myexp.run(1, 10)
    myexp.stop() #closes log file
    myexp.report("CCM")

def test_ccm_cartpole():

    # test CMU ACT-R Counting
    factory = ccm_factory.CcmFactory()
    model = factory.createModel()

    model.load('metaverse.architectures.actr_ccmsuite.cartpole_prods')

    myenv = GymEnvironment("CartPole-v0") #TODO: pass registered gym.env_id??

    map = ['cart_pos', 'cart_vel', 'pole_pos', 'pole_vel']
    myexp = Experiment(model, myenv, "CCM Gym Cartpole", map)
    model.motor.next_action = 0 #TODO: change to random action space

    myexp.start("ccm_cartpole") # appends to a log file
    myexp.run(10, 195) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    myexp.report("CCM") #TODO: get report type from agent factory

def test_ccm_starcraft():

    # test CMU ACT-R Counting
    factory = ccm_factory.CcmFactory()
    model = factory.createModel()
    #model.perception = Sc2Perception()

    model.load('metaverse.architectures.actr_ccmsuite.beacon_prods')

    myenv = StarCraftEnvironment("SC2MoveToBeacon-v1")
    map = ['loc_x', 'loc_y']
    myexp = Experiment(model, myenv, "CCM StarCraft Beacons", map)

    model.motor.next_action = [-1,-1]  # TODO: change to random action space

    myexp.start("ccm_beacons") # appends to a log file
    myexp.run(1, 100) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    myexp.report("CCM") #TODO: get report type from agent factory


def get_experiments_from_file(config_file, exp_list='ALL', format='YAML'):

    logger.info(f"Loading YAML config: {config_file} ")

    experiments = []

    stream = open(config_file, 'r')

    config_data = yaml.safe_load(stream)

    ix = 0

    for exp in config_data:  # list of experiments


        experiment, config, model, environment = {},{},{},{}

        # print(f"New Experiment: {doc.name()}")
        print(f"New Experiment")
        print(exp)

        # Parse config tree
        exp_config = exp.get('config')
        print(f"Config: {exp_config}")

        config_name = exp_config.get('name')
        config["name"] = config_name
        config_trials = exp_config.get('trials')
        config["trials"] = config_trials
        config_steps = exp_config.get('steps')
        config["steps"] = config_steps

        experiment["config"] = config

        # Parse model tree
        model_config = exp.get('model')
        print(f"Model: {model_config}")

        model_arch = model_config.get('architecture')
        model["architecture"] = model_arch
        model_file = model_config.get('file')
        model["file"] = model_file

        experiment["model"] = model

        # Parse environment tree
        env_config = exp.get('environment')
        print(f"Model: {env_config}")

        env_name = env_config.get('name')
        environment["name"] = env_name
        env_type = env_config.get('type')
        environment["type"] = env_type
        env_adapter = env_config.get('adapter')
        environment["adapter"] = env_adapter
        env_map = env_config.get('obs_map')
        environment["obs_map"] = env_map
        env_default_act = env_config.get('env_default_act')
        environment["default_act"] = env_default_act



        experiment["environment"] = environment

        experiments.append(experiment)

    return experiments


def get_arch_factory(fact_name=None):

    logger.debug(f"get_arch_factory({fact_name})")
    print(f"get_factory() name: {fact_name}")

    factory = None

    lisp_actr_fact = cmu_factory.CmuActrFactory()
    python_actr_fact = ccm_factory.CcmFactory()
    soar_fact = soar_factory.SoarFactory()

    switcher = {
        'ACTR': lisp_actr_fact,
        'CCM': python_actr_fact,
        'Soar' : soar_fact
    }

    factory = switcher.get(fact_name, "Invalid arch_factory name")

    return factory

def get_env_factory(fact_name=None):

    logger.debug(f"get_env_factory({fact_name})")
    print(f"get_env_factory() name: {fact_name}")

    factory = None

    simple = SimpleEnvironment()
    gym = GymEnvironment("CartPole-v0")

    switcher = {
        'simple': simple,
        'gym' : gym
    }

    factory = switcher.get(fact_name, "Invalid env_factory name")

    return factory

def do_experiment(exp_configs):

    for experiment in exp_configs:

        exp_config = experiment["config"]
        model_config = experiment["model"]
        env_config = experiment["environment"]

        exp_name = exp_config["name"]
        exp_trials = exp_config["trials"]
        exp_steps = exp_config["steps"]
        print(f"Starting Experiment: {exp_name}")

        model_arch = model_config["architecture"]
        factory = get_arch_factory(model_arch)

        model = factory.createModel()
        model_file = model_config["file"]
        model.load(model_file)

        env_default_act = env_config["default_act"]

        model.motor.next_action = env_default_act

        env_type = env_config["type"]
        myenv = get_env_factory(env_type)

        env_map = env_config["obs_map"]

        myexp = Experiment(model, myenv, exp_name,env_map)
        #myexp = Experiment(model, myenv, "CMU Gym Cartpole", map)

        myexp.start(exp_name) # appends to a log file
        myexp.run(exp_trials, exp_steps)
        myexp.stop() #closes log file
        #myexp.report("ACTR")

def launch_cmd_prompt():
    prompt = MyPrompt()
    prompt.prompt = 'Thesis> '
    prompt.cmdloop('Starting Metaverse prompt...')

    prompt = MyPrompt()
    prompt.do_demo()

    myexp = Experiment()
    myexp.run_all()

def launch_exp_from_config():

    CONFIG_FILE = "demo_config.yaml"
    exp_configs = get_experiments_from_file(CONFIG_FILE)
    print("*** START EXPERIMENTS***")
    do_experiment(exp_configs)

def compare_production_systems():

    #changes to production cycle rate
    cycle_start = 1 #once per second
    cycle_end = 0.05 #10 times per second

    task = "production_test"
    trials = 5
    steps = 10

    test_iv = "ps"
    iv_start = 0.05
    iv_end = 0.1
    iv_inc = 0.01

    prod_test_config_switch = {
        'ACTR': "/tests/psych/count_test.lisp",
        'CCM' : 'metaverse.architectures.actr_ccmsuite.counting_prods',
        'Soar' : "soar_agent.config"
    }

    architectures = ['ACTR', 'CCM', 'Soar']
    architectures1 = ['ACTR']
    architectures2 = ['CCM']
    architectures3 = ['Soar']

    reporter = scribe.Reporter()
    experiments = []

    for arch in architectures:

        factory = get_arch_factory(arch)
        model = factory.createModel()
        model_file = prod_test_config_switch.get(arch)
        model.load(model_file)
        myenv = SimpleEnvironment(task)
        myexp = Experiment(model, myenv, task)
        #myexp.set_parameters(test_iv, iv_start, iv_end, iv_inc )
        myexp.start(task+"_"+arch)  # appends to a log file
        myexp.run(trials, steps)
        myexp.stop()  # closes log file
        outfile = myexp.report()
        experiments.append([arch, outfile])
        reporter.add_experiment(arch, outfile)

    with open('last_counting_experiments.yaml', 'w') as yaml_file:
        yaml.dump(experiments, yaml_file)

    reporter.gen_arch_frames()
    reporter.declarative_mem_activation_report(plot="series")

    #model.working.addWME('add 5 2 count:None sum:None')

    #changes to production cycle time

def compare_procedural_memories():

    #test conflict resolution
    pass

    #test utility learning


    #test production compilation

def compare_declarative_memories():

    #test storage and recall
    pass

    #test activation and decay


def compare_cartpole():


    task = "visual task"
    trials = 1
    steps = 195

    test_iv = "ps"
    iv_start = 0.05
    iv_end = 0.1
    iv_inc = 0.01

    prod_test_config_switch = {
        'ACTR': "/tests/gym/cartpole.lisp",
        'CCM': 'metaverse.architectures.actr_ccmsuite.cartpole_prods',
        'Soar': "/tests/cart-pole/soar_agent.config"
    }

    architectures = ['ACTR', 'CCM', 'Soar']
    architectures1 = ['ACTR']
    architectures2 = ['CCM']
    architectures3 = ['Soar']

    reporter = scribe.Reporter()
    experiments = []

    # for arch in architectures:
    #     factory = get_arch_factory(arch)
    #     model = factory.createModel()
    #     model_file = prod_test_config_switch.get(arch)
    #     model.load(model_file)
    #     #myenv = SimpleEnvironment(task)
    #     myenv = GymEnvironment("CartPole-v0")  # TODO: pass registered gym.env_id??
    #     model.motor.next_action = 0
    #     myexp = Experiment(model, myenv, task, map)
    #     # myexp.set_parameters(test_iv, iv_start, iv_end, iv_inc )
    #     myexp.start(task + "_" + arch)  # appends to a log file
    #     myexp.run(trials, steps)
    #     myexp.stop()  # closes log file
    #     outfile = myexp.report()
    #     experiments.append([arch, outfile])
    #     reporter.add_experiment(arch, outfile)

    # test CMU ACT-R Counting
    factory = cmu_factory.CmuActrFactory()
    model = factory.createModel()
    model.load("/tests/gym/cartpole.lisp")
    map = ['cart_pos', 'cart_vel', 'pole_pos', 'pole_vel']
    myenv = GymEnvironment("CartPole-v0") #TODO: pass registered gym.env_id??
    model.motor.next_action = 0
    myexp = Experiment(model, myenv, "CMU Gym Cartpole", map)
    myexp.start("cmu_cartpole") # appends to a log file
    myexp.run(5, 195) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    outfile = myexp.report("ACTR")
    experiments.append(["ACTR", outfile])
    reporter.add_experiment("ACTR", outfile)

    # test CMU ACT-R Counting
    factory = ccm_factory.CcmFactory()
    model = factory.createModel()
    model.load('metaverse.architectures.actr_ccmsuite.cartpole_prods')
    myenv = GymEnvironment("CartPole-v0") #TODO: pass registered gym.env_id??
    map = ['cart_pos', 'cart_vel', 'pole_pos', 'pole_vel']
    myexp = Experiment(model, myenv, "CCM Gym Cartpole", map)
    model.motor.next_action = 0 #TODO: change to random action space
    myexp.start("ccm_cartpole") # appends to a log file
    myexp.run(5, 195) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    outfile = myexp.report("CCM") #TODO: get report type from agent factory
    experiments.append(["CCM", outfile])
    reporter.add_experiment("CCM", outfile)

    # test CMU ACT-R Counting
    factory = soar_factory.SoarFactory()
    model = factory.createModel()
    model.load("cart-pole.soar","cart-pole")
    myenv = GymEnvironment("CartPole-v0") #TODO: pass registered gym.env_id??
    myexp = Experiment(model, myenv, "Soar Gym Cartpole")
    model.perception.create_input_wmes
    myexp.start("soar_cartpole") # appends to a log file
    myexp.run(5, 195) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    outfile =  myexp.report("Soar")
    experiments.append(["Soar", outfile])
    reporter.add_experiment("Soar", outfile)

    with open('last_cartpole_experiments.yaml', 'w') as yaml_file:
        yaml.dump(experiments, yaml_file)

    reporter.gen_arch_frames()
    reporter.vision_activation_report(plot="series")
    reporter.motor_activation_report(plot="series")


def compare_beacons():


    task = "visual task"
    trials = 1
    steps = 195

    test_iv = "ps"
    iv_start = 0.05
    iv_end = 0.1
    iv_inc = 0.01

    prod_test_config_switch = {
        'ACTR': "/tests/gym/cartpole.lisp",
        'CCM': 'metaverse.architectures.actr_ccmsuite.cartpole_prods',
        'Soar': "/tests/cart-pole/soar_agent.config"
    }

    architectures = ['ACTR', 'CCM', 'Soar']
    architectures1 = ['ACTR']
    architectures2 = ['CCM']
    architectures3 = ['Soar']

    reporter = scribe.Reporter()
    experiments = []

    # for arch in architectures:
    #     factory = get_arch_factory(arch)
    #     model = factory.createModel()
    #     model_file = prod_test_config_switch.get(arch)
    #     model.load(model_file)
    #     #myenv = SimpleEnvironment(task)
    #     myenv = GymEnvironment("CartPole-v0")  # TODO: pass registered gym.env_id??
    #     model.motor.next_action = 0
    #     myexp = Experiment(model, myenv, task, map)
    #     # myexp.set_parameters(test_iv, iv_start, iv_end, iv_inc )
    #     myexp.start(task + "_" + arch)  # appends to a log file
    #     myexp.run(trials, steps)
    #     myexp.stop()  # closes log file
    #     outfile = myexp.report()
    #     experiments.append([arch, outfile])
    #     reporter.add_experiment(arch, outfile)

    # test CMU ACT-R Starcraft
    factory = cmu_factory.CmuActrFactory()
    model = factory.createModel()
    map = ['beacon_x', 'beacon_y']
    #model.perception.setObservationSpace(map)
    model.load("/tests/sc2/gym_sc2-beacons-simple.lisp")
    myenv = StarCraftEnvironment("SC2MoveToBeacon-v1")
    myexp = Experiment(model, myenv, "CMU StarCraft Beacons",map)
    model.motor.next_action = [-1, -1]
    myexp.start("cmu_beacons") # appends to a log file
    myexp.run(1, 100) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    outfile = myexp.report("ACTR")
    experiments.append(["ACTR", outfile])
    reporter.add_experiment("ACTR", outfile)

    # test CCM ACT-R Starcraft
    factory = ccm_factory.CcmFactory()
    model = factory.createModel()
    #model.perception = Sc2Perception()
    model.load('metaverse.architectures.actr_ccmsuite.beacon_prods')
    myenv = StarCraftEnvironment("SC2MoveToBeacon-v1")
    map = ['loc_x', 'loc_y']
    myexp = Experiment(model, myenv, "CCM StarCraft Beacons", map)
    model.motor.next_action = [-1,-1]  # TODO: change to random action space
    myexp.start("ccm_beacons") # appends to a log file
    myexp.run(1, 100) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    outfile = myexp.report("CCM") #TODO: get report type from agent factory
    experiments.append(["CCM", outfile])
    reporter.add_experiment("CCM", outfile)

    # test Soar Starcraft
    factory = soar_factory.SoarFactory()
    model = factory.createModel()
    model.load("starcraft2.soar","starcraft")
    myenv = StarCraftEnvironment("SC2MoveToBeacon-v1")
    myexp = Experiment(model, myenv, "Soar StarCraft Beacons")
    model.motor.next_action = [-1, -1]
    myexp.start("soar_beacons") # appends to a log file
    myexp.run(1, 100) #if no cycles provided, env determines end state
    myexp.stop() #closes log file
    outfile = myexp.report("Soar")
    experiments.append(["Soar", outfile])
    reporter.add_experiment("Soar", outfile)

    with open('last_beacons_experiments.yaml', 'w') as yaml_file:
        yaml.dump(experiments, yaml_file)

    reporter.gen_arch_frames()
    reporter.vision_activation_report(plot="series")
    reporter.motor_activation_report(plot="series")


def compare_motor_systems():

    #test key press rate
    pass

    #test key press delays?


if __name__ == '__main__':

    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger("metaverse")
    logger.info("=== Program started ===")

    #----------------------------------------
    #           Config Tests
    # ----------------------------------------

    #launch_exp_from_config()

    #----------------------------------------
    #           Component Tests
    # ----------------------------------------

    #compare_production_systems()

    #compare_working_memories()

    #compare_cartpole()

    compare_beacons()

    #----------------------------------------
    #           CMU ACT-R Tests
    # ----------------------------------------

    #print("*** START CMU COUNTING ***")
    #test_cmu_counting()
    #
    # print("*** START CMU CARTPOLE ***")
    # test_cmu_cartpole()
    #
    # print("*** START CMU StarCraft ***")
    # test_cmu_starcraft()

    # # # ----------------------------------------
    # # #           Soar Tests
    # # # ----------------------------------------
    #
    # print("*** START SOAR COUNTING ***")
    # test_soar_counting()
    #
    # print("*** START Soar CARTPOLE ***")
    # test_soar_cartpole()
    #
    # print("*** START Soar StarCraft ***")
    # test_soar_starcraft()
    #
    # # ----------------------------------------
    # #           CCMSuite3 ACT-R Tests
    # # ----------------------------------------
    #
    # print("*** START CCMSuite3 COUNTING ***")
    # test_ccm_counting()
    #
    # print("*** START CCMSuite3 CartPole ***")
    # test_ccm_cartpole()
    #
    # print("*** START CCMSuite3 StarCraft ***")
    # test_ccm_starcraft()
    #
    # logger.info("=== Program Finished ===")