from __future__ import annotations
from abc import ABC, abstractmethod
import os
import gym
import sc2gym.envs
import argparse
from absl import flags
import logging

log = logging.getLogger("metaverse")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


last_run_passed = False
num_consecutive_passes = 0
is_paused = False
episode_num = 1

running = False

class AbstractEnvironment(ABC):
    """Interface for virtual environments. Currently supporting:

        Psychometrics (SimpleEnv):

        OpenAI (GymEnv):
            CartPole
            MountainCar
            LunarLander

        StarCraft mini-games (StarCraftEnv):
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
        self.sc2_envs = ['SC2MoveToBeacon-v1']  # TODO: replace with Gym versions

class SimpleEnvironment(AbstractEnvironment):

    def __init__(self, name="", adapter = "psych", maxsteps = -1):
        self.name = name
        self.adapter = adapter

        self.actions = []
        self.action_space = None
        self.observation_space = None
        self.observations = []

        self.last_observation = None

        self.done = False
        self.count = 0
        # self.target = target

        self.episode_reward = 0
        self.total_reward = 0
        self.episode = 0

        self.maxsteps = maxsteps

    def isDone(self):
        return self.done

    def getEspisodeReward(self):
        return self.episode_reward

    def getTotalRewards(self):
        return self.total_reward


    def setAdapter(self, adapter):
        self.adapter = adapter

    def getActionSpace(self):

        return self.action_space

    def getObservationSpace(self):

        return self.observation_space

    def getLastObservation(self):
        return self.last_observation

    def step(self):
        self.count = self.count + 1
        if self.count == self.maxsteps:
            self.done = True
        # if self.count == self.target:
        #     self.done = True

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

        self.action_space = self.gym_env.action_space
        self.observation_space = self.gym_env.observation_space

        self.done = False

        self.episode_reward = 0

        self.total_reward = 0

        self.episode = 0

    def isDone(self):
        return self.done

    def getEspisodeReward(self):
        return self.episode_reward

    def getTotalRewards(self):
        return self.total_reward

    def setAdapter(self, adapter):
        self.adapter = adapter

    def getActionSpace(self):

        return self.action_space

    def getObservationSpace(self):

        return self.observation_space

    def getLastObservation(self):
        return self.last_observation

    def nextAction(self, action):
        self.next_action = action

    def step(self):
        log.debug("Env:step()")
        self.gym_env.render()
        if self.next_action is not None:
            log.debug(f"Env:step() move_cmd: {str(self.next_action)}")
            self.last_observation, self.reward, self.done, self.info = self.gym_env.step(self.next_action)

            self.step_num = self.step_num + 1
            self.episode_reward += self.reward

    def reset(self):
        print("Env:reset()")
        self.gym_env.reset()
        self.last_observation, self.reward, self.done, self.info = self.gym_env.step(self.next_action)
        self.step_num = 0

        if self.episode > 0:
            print(f"Episode {self.episode} ended with reward {self.episode_reward} "
                  f"after {self.step_num} steps.")

        self.episode += 1
        self.total_reward += self.episode_reward
        self.episode_reward = 0

    def close(self):

        if self.episode > 0:
            print(f"Got {self.total_reward} total reward, with an average reward of "
                  f"{float(self.total_reward) / self.episode} per episode")

        self.gym_env.close()

class StarCraftEnvironment(AbstractEnvironment):


    _PLAYER_NEUTRAL = 3  # beacon/minerals
    _NO_OP = 0
    FLAGS = flags.FLAGS
    FLAGS([__file__])

    _ENV_NAME = "SC2MoveToBeacon-v1" #defaults to 2-D representation

    def __init__(self, name = _ENV_NAME, visualize=True, step_mul=None, random_seed=None, find_features=True):
        self.name = name
        # self.adapter = adapter
        self.env_name = name
        self.visualize = visualize
        self.step_mul = step_mul
        self.random_seed = random_seed
        self.find_features = find_features

        self.gym_env = gym.make(self.env_name)
        self.last_observation = self.gym_env.reset()
        if self.find_features:
            self.last_observation = self.get_features(self.last_observation)

        self.step_num = 0

        self.action_space = self.gym_env.action_space
        self.observation_space = self.gym_env.observation_space

        self.done = False

        self.episode_reward = 0

        self.total_reward = 0

        episodes_done = 0

        self.gym_env.settings['visualize'] = self.visualize
        self.gym_env.settings['step_mul'] = self.step_mul
        self.gym_env.settings['random_seed'] = self.random_seed

    def isDone(self):
        return self.done

    def getEspisodeReward(self):
        return self.episode_reward

    def getTotalRewards(self):
        return self.total_reward

    def setAdapter(self, adapter):
        self.adapter = adapter

    def getActionSpace(self):

        return self.action_space

    def getObservationSpace(self):

        return self.observation_space

    def getLastObservation(self):
        return self.last_observation

    def nextAction(self, action):
        self.next_action = action



    def step(self):
        print("Env:step()")
        #self.gym_env.render()
        if self.next_action is not None:
            print("move_cmd sent to gym: "+str(self.next_action))
            self.last_observation , self.reward, self.done, self.info = self.gym_env.step(self.next_action)

            if self.find_features:
                self.last_observation = self.get_features(self.last_observation)

            if self.visualize:
                pass

            self.step_num = self.step_num + 1

            self.episode_reward += self.reward


    def reset(self):
        print("Env:reset()")
        self.gym_env.reset()
        self.last_observation, self.reward, self.done, self.info = self.gym_env.step(self.next_action)
        if self.find_features:
            self.last_observation = self.get_features(self.last_observation)
        self.step_num = 0

        self.total_reward += self.episode_reward
        self.episode_reward = 0

    def close(self):
        self.gym_env.close()

    def get_features(self, obs):

        _PLAYER_NEUTRAL = 3  # beacon/minerals
        _NO_OP = 0

        #find location of beacon
        neutral_y, neutral_x = (obs[0] == _PLAYER_NEUTRAL).nonzero()
        if not neutral_y.any():
            raise Exception("Beacon not found!")
        target = [int(neutral_x.mean()), int(neutral_y.mean())]

        return target

if __name__ == '__main__':
    testenv = StarCraftEnvironment()
    spec = testenv.gym_env.spec
    print(f"spec: {spec}")