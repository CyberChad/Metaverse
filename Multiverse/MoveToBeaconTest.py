from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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

from absl import flags

from pysc2.agents import base_agent
from pysc2.lib import actions

#game setup
FLAGS = flags.FLAGS #for passing arguments
steps = 400 # = 4 Episodes
step_mul = 1 #no frame skipping = realtime

import numpy
import ccm
log = ccm.log()

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

from pysc2.env import run_loop
from pysc2.env import sc2_env

_PLAYER_SELF = features.PlayerRelative.SELF
_PLAYER_NEUTRAL = features.PlayerRelative.NEUTRAL  # beacon/minerals
_PLAYER_ENEMY = features.PlayerRelative.ENEMY

FUNCTIONS = actions.FUNCTIONS

from ccm import model
from ccm.lib.actr import *

def _xy_locs(mask):
  """Mask should be a set of bools from comparison with a feature layer."""
  y, x = mask.nonzero()
  return list(zip(x, y))



def action(self,test):
        log.action=test
        if test=='A':
            self.reward=1
        else:
            self.reward=0


class GameInput(ccm.Model):
    pass

class ActrAgent(ACTR):
    focus = Buffer()
    visual = Buffer()
    vision_module=SOSVision(visual,delay=0)

    retrieve = Buffer()
    memory = Memory(retrieve)

    next_action='no_op'

    def init(self):
        #print('actr init')
        #self.focus.set('find_beacon')
        pass

    def findBeacon(focus='found_beacon'):
        print('found the beacon!')
        focus.set('no_op')

    def moveToBeacon(focus='move_to_beacon'):
        print('moving to beacon!')
        focus.set('no_op')

class SimpleModel(ccm.Model):
    pass

class BeaconAgent(base_agent.BaseAgent):
  """An agent specifically for solving the MoveToBeacon map."""
  #actr_env =
  def __init__(self):
      super(BeaconAgent, self).__init__()

  #def nextAction(actions.FUNCTIONS func):


  def actr_setup(self,actr):
      self.myAgent = actr


  def step(self, obs):

    super(BeaconAgent, self).step(obs)

    #self.response = [_NO_OP, []] #default response is to do nothing


    if FUNCTIONS.Move_screen.id in obs.observation.available_actions:

      player_relative = obs.observation.feature_screen.player_relative

      beacon = _xy_locs(player_relative == _PLAYER_NEUTRAL)

      if not beacon:
        self.myAgent.focus.set('no_op')
        return FUNCTIONS.no_op()

      beacon_center = numpy.mean(beacon, axis=0).round()

      self.myAgent.focus.set('found_beacon')

      return FUNCTIONS.Move_screen("now", beacon_center)

    else:
      self.myAgent.focus.set('move_to_beacon')
      return FUNCTIONS.select_army("select")

class StarCraftEnvironment(ccm.Model):
    beacons=0
    def start(self):
        pass
#    except KeyboardInterrupt:
#        pass

#def actr_thread(*args):
    #actrEnv.run()

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
        # visualize=True) as env:
        visualize=False)

    sc2agent.setup(sc2env.observation_spec(), sc2env.action_spec())

    timesteps = sc2env.reset()

    sc2agent.reset()

    #    actrAgent.run()


    while True:
        step_actions = [sc2agent.step(timesteps[0])]
        if timesteps[0].last():
            break
        timesteps = sc2env.step(step_actions)

class MatchEnvironment(ccm.Model):
    def start(self):
        self.count=1
        yield 1   # wait one second
        self.letter=ccm.Model(isa='letter',x=0.5,y=0.5,visible=True)
        self.letter.text=self.random.choice('BCDFGHJKLMNPQRSTVWXYZ')
        self.target=self.letter.text

    def press(self,key):
        self.pressed=key
        if key==self.target:
            log.success=True
        else:
            log.success=False
        self.letter.visible=False
        self.count+=1
        if self.count==0:
            self.stop()
        else:
            yield 1
            self.letter.text=self.random.choice('BCDFGHJKLMNPQRSTVWXYZ')
            self.letter.visible=True
            self.target=self.letter.text


class Model(ACTR):
    goal = Buffer()
    visual = Buffer()
    vision = SOSVision(visual)

    def findUnattendedLetter(goal='attend', vision='busy:False'):
        vision.request('isa:letter')
        goal.set('attend')

    def encodeLetter(goal='attend', visual='isa:letter text:?letter'):
        goal.set('respond ?letter')

    def respond(goal='respond ?letter'):
        self.parent.press(letter)
        visual.clear()
        goal.set('attend')


def actr_thread2(*args):

    FLAGS(args)

    env = MatchEnvironment()
    env.model = actr_model
    env.model.goal.set('attend')

    ccm.display(env)

    #actr_agent = ActrAgent()
    #actrEnv = StarCraftEnvironment()
    #actrEnv.agent = actr_agent

    #ccm.log_everything(env)

    env.run()

def actr_thread(*args):

    FLAGS(args)

    env = StarCraftEnvironment()
    env.model = actr_agent
    env.model.focus.set('no_op')

    ccm.log(env)

    env.run()

if __name__ == "__main__":
    #app.run(main)

    #model = Addition()
    #model.goal.set('add 5 2 count:None sum:None')
    #model.run()

    sc2agent = BeaconAgent()
    actr_model = Model()
    actr_agent = ActrAgent()
    actr_agent.focus.set('no_op')
    sc2agent.actr_setup(deepcopy(actr_agent))

    #model_thread = Process(target=actr_thread, args=sys.argv)
    model_thread = threading.Thread(target=sc2agent.myAgent.run(), args=sys.argv)
    model_thread.start()

    #time.sleep(25)

    # game_thread = Process(target=sc2_thread, args=sys.argv)
    game_thread = threading.Thread(target=sc2_thread, args=sys.argv)

    game_thread.start()







