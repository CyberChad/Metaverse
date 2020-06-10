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

############### Globals ######################

def _xy_locs(mask):
  """Mask should be a set of bools from comparison with a feature layer."""
  y, x = mask.nonzero()
  return list(zip(x, y))

#********************* ACT-R Stuff **********************
class GameEnvModel(ccm.Model):
    next_action=ccm.Model(isa='action',press='no_op')
    screen=ccm.Model(isa='screen',event='none')

class MotorModule(ccm.Model):
    beacons = 0
    next_action = ''

    def do_action(self,action):
        print(f"do the action: {action}")
        self.parent.parent.next_action = action
        self.parent.parent.screen.event='none'
        time.sleep(0.1)

class ActrAgent(ACTR):
    focus = Buffer()
    motor = MotorModule()
    visual = Buffer()
    vision_module=SOSVision(visual,delay=0)

    retrieve = Buffer()
    memory = Memory(retrieve)

    def init(self):
        print('actr init')
        self.focus.set('find_beacon')

    #def noOp(screen="event:none"):
    def seeBeacon(screen='event:?beacon'):
        print('found the beacon!')
        motor.do_action(beacon)
        self.focus.clear()

    def moveToBeacon(screen='event:?event'):
        motor.do_action(event)
        #print(f'production:{moving}')
        self.focus.clear()

#--------------------------- StarCraft Stuff ---------------------
class BeaconAgent(base_agent.BaseAgent):
  """An agent specifically for solving the MoveToBeacon map."""
  #actr_env =
  def __init__(self):
      super(BeaconAgent, self).__init__()

      self.status = 'none'
      self.target = numpy.zeros(2)
  #def nextAction(actions.FUNCTIONS func):


  def step(self, obs):

    super(BeaconAgent, self).step(obs)

    #self.response = [_NO_OP, []] #default response is to do nothing

    if FUNCTIONS.Move_screen.id in obs.observation.available_actions:

      player_relative = obs.observation.feature_screen.player_relative

      beacon = _xy_locs(player_relative == _PLAYER_NEUTRAL)

      if not beacon:
        actrGameEnv.screen.event = 'none'
        return FUNCTIONS.no_op()

      beacon_center = numpy.mean(beacon, axis=0).round()

      if numpy.array_equal(beacon_center,self.target):
          return FUNCTIONS.no_op()
      else:
        self.target = beacon_center
        actrGameEnv.screen.event = 'beacon'
        self.status = 'moving'
        return FUNCTIONS.Move_screen("now", beacon_center)

    else:
      actrGameEnv.screen.event = 'moving'
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

def actr_thread2(*args): #not currently used

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

def actr_thread(*args): #not currently used

    FLAGS(args)

    env = StarCraftEnvironment()
    env.model = actr_agent
    env.model.focus.set('no_op')

    ccm.log(env)

    env.run()

#common_model = SimpleModel()
actrGameEnv = GameEnvModel()

if __name__ == "__main__":
    #app.run(main)

    sc2agent = BeaconAgent()

    actrGameEnv.agent = ActrAgent()

    #actr_agent.focus.set('no_op')
    #sc2agent.actr_setup(deepcopy(actr_agent))

    ccm.log_everything(actrGameEnv)
    #ccm.log(actrGameEnv)

    game_thread = threading.Thread(target=sc2_thread, args=sys.argv)
    game_thread.start()

    #model_thread = Process(target=actr_thread, args=sys.argv)
    model_thread = threading.Thread(target=actrGameEnv.run(), args=sys.argv)
    model_thread.start()

    #time.sleep(25)

    # game_thread = Process(target=sc2_thread, args=sys.argv)







