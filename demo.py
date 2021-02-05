from __future__ import annotations
#from Utils.parsers import XMLParser
from multiprocessing import Process

from abc import ABC, abstractmethod

import xml.etree.ElementTree as ET
import subprocess
import time
import psutil
import os

CMUACTR_PATH = "/home/chad/ACT-R/" #TODO: replace this with env variable or config
SOAR_PATH = "" #not sure if this is necessary with SoarLibs

#xmlParser = XMLParser()
#xmlParser.__init__("Counting.metamind")

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



def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    print ('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            print ('%s in r[i]' %(name))
            return r[i]


    return []


def experiment(env,arch):

    print("Testing "+arch+" in environment "+ env)


    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    arch_factory.createModel(CmuActrFactory())

    """
    *************************************
        Choose architecture sub-options for:
    *************************************
            > Declarative Memory
            > Procedural Memory
            > Others??
    """

    #configure each Factory Product with Common Model options

    """
    Configure environment-specific options:
    > map or challenge
    > single or multi-agent
    > difficulty rating
    """

    #select map/challenge/task-specific options

if __name__ == '__main__':

    from metaverse import director

    mymodel = director.MetaLoader("testmodel")


    """
    *************************************
    Load Experimental Framework
    *************************************
    """

    from metaverse.architectures import arch_factory
    from metaverse.architectures.actr_cmu.actr_cmu_factory import CmuActrFactory
    from metaverse.architectures.soar.soar_factory import SoarFactory


    """
    *************************************
    Choose Environment:
    *************************************
        > Gym
        > StarCraft2
        > HELK or Qemu machine?


    """

    environments = ['CartPole-v0', 'MountainCar-v1', 'LunarLander-v1'] #TODO: create env registry
    print("Environments Registry: " + str(environments))

    """
    *************************************
    Cognitive Architectures:
    *************************************

        > ACT-R_CMU
        > SOAR
        > Nengo?
        > SIGMA?
    """

    architectures = ['CMUACTR', 'CCMACTR', 'Soar', 'Nengo'] #TODO: create arch registry
    print("Architecture Registry: " + str(architectures))

    """
    *************************************
    Optional Experiment Config:
    *************************************

        > number of agents per environment
        > number of runs per agent
    """

    for env in environments:
        for arch in architectures:
            experiment(env,arch)


