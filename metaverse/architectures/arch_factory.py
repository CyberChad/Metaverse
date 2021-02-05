#from __future__ import print_function

from __future__ import annotations
from abc import ABC, abstractmethod

import subprocess
import time
import psutil
import os

from pysc2.agents import base_agent
from pysc2.agents.base_agent import actions

# import actr_cmu, actr_ccmsuite, actr_jackdot

import logging
import sys

# ********************************************
#               Factories
# ********************************************

class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def createModel(self) -> AbstractModel:
        pass

    @abstractmethod
    def createWorkingMemory(self) -> AbstractWorkingMemory:
        pass

    # @abstractmethod
    # def createDeclarativeMemory(self) -> AbstractDeclarativeMemory:
    #     pass
    #
    # @abstractmethod
    # def createProceduralMemory(self) -> AbstractProceduralMemory:
    #     pass
    #
    # @abstractmethod
    # def createPerception(self) -> AbstractPerception:
    #     pass
    #
    # @abstractmethod
    # def createMotor(self) -> AbstractMotor:
    #     pass




# ********************************************
#               Products
# ********************************************

class AbstractModel(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def create(self) -> str:
        pass

    @abstractmethod
    def step(self) -> str:
        pass

    @abstractmethod
    def run(self) -> str:
        pass

    @abstractmethod
    def reset(self) -> str:
        pass

    @abstractmethod
    def shutdown(self) -> str:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""

class AbstractWorkingMemory(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def addWME(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def removeWME(self, collaborator: AbstractModel) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""

# ************************* Client Code ***********

def createModel(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    model = factory.createModel()

    working_memory = factory.createWorkingMemory()

    print(f"{working_memory.addWME()}")
    print(f"{working_memory.removeWME(model)}", end="")

#*************************** END OF EXAMPLE **************

class Arch(object):
    """The main MetaMind Architecture class. It encapsulates a cognitive architecture
    with arbitrary behind-the-scenes dynamics. An architecture can be partially
    or fully implemented according to the Common Model of Cognition

    The main API methods that users of this class need to know are:

    step
    reset
    close

    """

class CommonModel(Arch):

    """ A cognitive architecture that ascribes to the Common Model of Cognition.
    It functions just as any regular MetaMind architecture but imposes a required
    structure on the following modules:

    Working Memeory (Buffers)
    Procedural Long-Term Memory (Production System)
    Declarative Long-Term Memory
    Perception
    Motor

    """

class SimpleAgent(base_agent.BaseAgent):
    def step(self, obs):
        super(SimpleAgent, self).step(obs)

        return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])

# holds the different cognitive architectures that we have available
class Architectures:
    def __init__(self, cogArchConfig):
        self.cogArchConfig = cogArchConfig #holds the configuration file



if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(CmuActrFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(SoarFactory())



