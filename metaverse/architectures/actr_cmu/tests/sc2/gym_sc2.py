from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import cmuactr as actr
import math
import numbers
from os import environ as env
import sys
import gym
import threading
import queue

import argparse
import numpy as np

__description__ = 'Run a scripted example using the SC2MoveToBeacon-v0 environment.'

import copy
import time
import threading
from pysc2.agents import base_agent
from pysc2.env import sc2_env
from pysc2.lib import actions, features, units
from absl import app
import random

#import scripted_actr_agent as scripted

import logging
import sys
import numpy
from absl import flags


#game setup
FLAGS = flags.FLAGS #for passing arguments
FLAGS([__file__])

steps = 400 # = 4 Episodes
step_mul = 1 #no frame skipping = realtime

#I think these are for the updated version of pysc2
from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

from pysc2.env import run_loop
from pysc2.env import sc2_env

import gym
from absl import flags
from pysc2.env import sc2_env

# noinspection PyUnresolvedReferences
import sc2gym.envs

#import metaverse.environments.

#from.base_example import BaseExample


_PLAYER_SELF = features.PlayerRelative.SELF
_PLAYER_NEUTRAL = features.PlayerRelative.NEUTRAL  # beacon/minerals
_PLAYER_ENEMY = features.PlayerRelative.ENEMY

FUNCTIONS = actions.FUNCTIONS
_NO_OP = 0
_ENV_NAME = "SC2MoveToBeacon-v0"


import os
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
print(DIR_PATH)

actr.load_act_r_model(DIR_PATH+"/sc2beacons.lisp")

ACTR_DIR = "/home/user/ACT-R/"

#actr.load_act_r_model("./sc2beacons.lisp")

last_run_passed = False
num_consecutive_passes = 0
is_paused = False
episode_num = 1

running = False

model_action = None
human_action = None
move_cmd = 0
key_monitor_installed = False
mouse_monitor_installed = False

############### Globals ######################

def _xy_locs(mask):
  """Mask should be a set of bools from comparison with a feature layer."""
  y, x = mask.nonzero()
  return list(zip(x, y))


#--------------------------- OLD StarCraft API Stuff ---------------------

class BeaconAgent(base_agent.BaseAgent):
  """An agent specifically for solving the MoveToBeacon map."""
  #actr_env =

  def __init__(self):
      super(BeaconAgent, self).__init__()

      self.status = 'none'
      self.target = numpy.zeros(2)

  def step(self, obs): #return the next action from FUNCTIONS

    super(BeaconAgent, self).step(obs)

    #self.response = [_NO_OP, []] #default response is to do nothing

    if FUNCTIONS.Move_screen.id in obs.observation.available_actions: #if we can move

      player_relative = obs.observation.feature_screen.player_relative

      beacon = _xy_locs(player_relative == _PLAYER_NEUTRAL)

      if not beacon: #The agent does not see a beacon
        #actrGameEnv.screen.event = 'beacon'
        return FUNCTIONS.no_op()

        #If we are still here, the beacon was found
      beacon_center = numpy.mean(beacon, axis=0).round()

      if numpy.array_equal(beacon_center,self.target): #we are standing on the beacon
          return FUNCTIONS.no_op()
      else:
        self.target = beacon_center #TODO update target coordinates
        #actrGameEnv.screen.event = 'beacon'
        self.status = 'moving' #TODO update state to moving
        return FUNCTIONS.Move_screen("now", beacon_center)

    else: #we can't move, so select a unit
      #actrGameEnv.screen.event = 'moving' #TODO update state to not moving
      return FUNCTIONS.select_army("select")


def sc2_thread(*args):

    FLAGS(args)

    sc2env = sc2_env.SC2Env(
        map_name="MoveToBeacon",
        # players=[sc2_env.Agent(sc2_env.Race.terran),
        #         sc2_env.Bot(sc2_env.Race.random,
        #                     sc2_env.Difficulty.very_easy)],
        players=[sc2_env.Agent(sc2_env.Race.terran)],

        agent_interface_format=features.AgentInterfaceFormat(
            feature_dimensions=features.Dimensions(screen=84, minimap=64),
            use_feature_units=True),
        step_mul=1,
        game_steps_per_episode=0,
        #screen_size_px=(128, 128),
        visualize=True)
        #visualize=False)

    sc2agent.setup(sc2env.observation_spec(), sc2env.action_spec())

    timesteps = sc2env.reset()

    sc2agent.reset()

    #    actrAgent.run()


    while True:
        step_actions = [sc2agent.step(timesteps[0])]
        if timesteps[0].last():
            break
        timesteps = sc2env.step(step_actions)

#----------------- ACT-R Stuff --------------------------

class CliThread(threading.Thread): #Client thread for human intervention

    def __init__(self, q_main_thread):
        self.queue_main = q_main_thread
        threading.Thread.__init__(self)

    def run(self):
        cmd = "None"
        while cmd not in ("exit", "quit"):
            cmd = input("CMC> ")
            self.queue_main.put(cmd)

def respond_to_keypress(model,key):#TODO see if we can include a mouse move and click
    print("respond_to_keypress: " +key)
    global move_cmd
    actr.clear_exp_window(window)
    if model:
        move_cmd = key
    else:
        move_cmd = 0

def add_key_monitor():
    global key_monitor_installed

    if key_monitor_installed == False:
        actr.add_command("sc2-key-press",respond_to_keypress,
                         "sc2 task key output monitor")
        actr.monitor_command("output-key","sc2-key-press")
        key_monitor_installed = True
        print("key monitor installed")

        return True
    else:
        return False

def remove_key_monitor():

    actr.remove_command_monitor("output-key","sc2-key-press")
    actr.remove_command("sc2-key-press")

    global key_monitor_installed
    key_monitor_installed = False

def respond_to_mouseclick(model,click,finger):#TODO see if we can include a mouse move and click
    print("respond_to_mouseclick: " +click)
    global move_cmd

    if model:
        move_cmd = click
    else:
        move_cmd = 0

def add_mouse_monitor():
    global mouse_monitor_installed

    if mouse_monitor_installed == False:
        actr.add_command("sc2-mouse-click",respond_to_mouseclick,
                         "sc2 task mouse output monitor")
        actr.monitor_command("click-mouse","sc2-mouse-click")
        mouse_monitor_installed = True
        print("mouse monitor installed")

        return True
    else:
        return False

def remove_mouse_monitor():

    actr.remove_command_monitor("click-mouse","sc2-mouse-click")
    actr.remove_command("sc2-mouse-click")

    global mouse_monitor_installed
    mouse_monitor_installed = False


def update_model_action(obs):

    #pre-process the observation, currently task-specific
    neutral_y, neutral_x = (obs[0] == _PLAYER_NEUTRAL).nonzero()

    target_x = int(neutral_x.mean())
    target_y = int(neutral_y.mean())

    if not neutral_y.any():
        raise Exception("Beacon not found!")

    print("update_model_action: " + str(target_x)+","+str(target_y))
    actr.add_text_to_exp_window(window, "B", x=target_x, y=target_y)

    #if goal buffer has been defined, RPC mod-focus to update chunks
    if actr.buffer_read('goal'):
        print("mod_focus")
        #update goal buffer chunks here
        actr.mod_focus('beacon_x',target_x,'beacon_y', target_y)

    #otherwise init goal with current observation
    else:
        print("goal_focus")
        actr.goal_focus(actr.define_chunks(['isa','game-state','beacon_x',target_x,
                                    'beacon_y', target_y,'state','start'])[0])

    global model_action
    model_action = 0 #replace with action space

    global running

    print("act-r running: "+str(running))
    actr.run(5)
    return model_action

class BaseExample(object):
    def __init__(self, env_name, visualize=False, step_mul=None, random_seed=None) -> None:
        super().__init__()
        self.env_name = env_name
        self.visualize = visualize
        self.step_mul = step_mul
        self.random_seed = random_seed

    def run(self, num_episodes=1):
        env = gym.make(self.env_name)
        env.settings['visualize'] = self.visualize
        env.settings['step_mul'] = self.step_mul
        env.settings['random_seed'] = self.random_seed
        env.settings['players'] = [sc2_env.Agent(sc2_env.Race.terran)]

        episode_rewards = np.zeros((num_episodes,), dtype=np.int32)
        episodes_done = 0
        for ix in range(num_episodes):
            obs = env.reset()

            done = False
            while not done:
                action = self.get_action(env, obs)
                obs, reward, done, _ = env.step(action)
                obs_s = str(obs)
                reward_s = str(reward)
                done_s = str(done)
                print("Obs: "+obs_s)
                print("Reward: "+reward_s)
                print("Done: " +done_s)

                update_model_action(obs)

            # stop if the environment was interrupted for any reason
            if obs is None:
                break

            episodes_done += 1
            episode_rewards[ix] = env.episode_reward

        env.close()

        return episode_rewards[:episodes_done]

    def get_action(self, env, obs):
        raise NotImplementedError('Inherited classes must override get_action() method')


class MoveToBeacon1d(BaseExample):
    def __init__(self, visualize=True, step_mul=None, random_seed=None) -> None:
        super().__init__(_ENV_NAME, visualize, step_mul, random_seed)

    def get_action(self, env, obs):
        # print("Observation: "+obs[0])

        # action logic...
        neutral_y, neutral_x = (obs[0] == _PLAYER_NEUTRAL).nonzero()
        if not neutral_y.any():
            raise Exception('Beacon not found!')
        target = [int(neutral_x.mean()), int(neutral_y.mean())]
        target = np.ravel_multi_index(target, obs.shape[1:])
        # print("Target: "+target)

        return target

#============================================
#=================  MAIN  ===================
#============================================

if __name__ == "__main__":

    # Create the user input thread and queue for return commands
    queue_user_cmds = queue.Queue()
    user_cmd_thread = CliThread(queue_user_cmds)
    user_cmd_thread.start()

    # Create the ACT-R agent
    window = actr.open_exp_window("Find Beacon")
    actr.install_device(window)
    add_key_monitor() #TODO hook this up to the SC2 env.ACTIONS
    add_mouse_monitor()  # TODO hook this up to the SC2 env.ACTIONS
    #
    # sc2agent = BeaconAgent()
    #
    # game_thread = threading.Thread(target=sc2_thread, args=sys.argv)
    # game_thread.start()

    #TODO update to work ACT-R dispatch service
    #model_thread = Process(target=actr_thread, args=sys.argv)
    #model_thread = threading.Thread(target=actrGameEnv.run(), args=sys.argv)
    #model_thread.start()

    ## example from sc2gameenv

    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('--visualize', type=bool, default=True,
                        help='show the pysc2 visualizer')
    parser.add_argument('--num-episodes', type=int, default=10,
                        help='number of episodes to run')
    parser.add_argument('--step-mul', type=int, default=None,
                        help='number of game steps to take per turn')
    parser.add_argument('--random-seed', type=int, default=None,
                        help='the random seed to pass to the game environment')
    args = parser.parse_args()

    example = MoveToBeacon1d(args.visualize, args.step_mul, args.random_seed)
    rewards = example.run(args.num_episodes)

    if rewards:
        print('Total reward: {}'.format(rewards.sum()))
        print('Average reward: {} +/- {}'.format(rewards.mean(), rewards.std()))
        print('Minimum reward: {}'.format(rewards.min()))
        print('Maximum reward: {}'.format(rewards.max()))

