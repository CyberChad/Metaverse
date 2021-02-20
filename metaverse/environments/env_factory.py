from __future__ import annotations
from abc import ABC, abstractmethod
import os
import gym

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


last_run_passed = False
num_consecutive_passes = 0
is_paused = False
episode_num = 1

running = False

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

class SimpleEnvironment(AbstractEnvironment):

    def __init__(self, name="", adapter = "psych", target=10):
        self.name = name
        self.adapter = adapter

        self.actions = []
        self.observations = []
        self.last_observation = None


        self.done = False
        self.count = 0
        self.target = target

    def setAdapter(self, adapter):
        self.adapter = adapter

    def getActionSpace(self):

        return self.actions

    def getObservations(self):

        return self.observations

    def getLastObservation(self):
        return self.last_observation

    def step(self):
        self.count = self.count + 1
        if self.count == self.target:
            self.done = True

    def reset(self):
        pass

    def close(self):
        pass


class GymEnvironment(AbstractEnvironment):

    def __init__(self, name="CartPole-v0", adapter = "gym"):
        self.name = name
        self.adapter = adapter

        self.gym_env = gym.make('CartPole-v0')
        self.last_observation = self.gym_env.reset()
        self.step_num = 0

        self.actions = self.gym_env.action_space
        self.observations = self.gym_env.observation_space

        self.done = False

    def setAdapter(self, adapter):
        self.adapter = adapter

    def getActionSpace(self):

        return self.actions

    def getObservationSpace(self):

        return self.observations

    def getLastObservation(self):
        return self.last_observation

    def nextAction(self, action):
        self.next_action = action

    def step(self):
        print("Env:step()")
        self.gym_env.render()
        if self.next_action is not None:
            print("move_cmd sent to gym: "+str(self.next_action))
            self.last_observation, self.reward, self.done, self.info = self.gym_env.step(self.next_action)

            self.step_num = self.step_num + 1

    def reset(self):
        print("Env:reset()")
        self.gym_env.reset()
        self.last_observation, self.reward, self.done, self.info = self.gym_env.step(self.next_action)
        self.step_num = 0

    def close(self):
        self.gym_env.close()
