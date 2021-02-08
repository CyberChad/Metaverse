from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractEnvironment(ABC):
    """Interface for virtual environments. Currently supporting:

        OpenAI Gym:
            CartPole
            MountainCar
            LunarLander

        StarCraft mini-games:
            move to beacon
            collect mineral shards
            defeat roaches
    """

    @abstractmethod
    def __init__(self):
        pass


class Environments:
    def __init__(self, envConfig):
        self.envConfig = envConfig #holds the configuration file
        self.adapters = ['psych', 'gym', 'sc2']
        self.psych_envs = ['Counting']
        self.gym_envs = ['CartPole-v0', 'MountainCar-v1', 'LunarLander-v1']  # TODO: create env registry
        self.sc2_envs = ['MoveToBeacon']  # TODO: replace with Gym versions

class StarcraftEnvironment():
    pass

class Environment(AbstractEnvironment):

    def __init__(self, name="", adapter = "psych"):
        self.name = name
        self.adapter = adapter

        self.actions = []
        self.observations = []

    def setAdapter(self, adapter):
        self.adapter = adapter

    def getActionSpace(self):

        return self.actions

    def getObservations(self):

        return self.observations