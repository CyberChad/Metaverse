from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pysc2.agents import base_agent
from pysc2.env import sc2_env
from pysc2.lib import actions, features, units
from absl import app
import random

#import scripted_actr_agent as scripted

import logging
import sys

from pysc2.agents import base_agent
from pysc2.lib import actions


import numpy
import ccm

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

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

class GameScreen(ccm.Model):
    pass

class GameInput(ccm.Model):
    pass

class ActrAgent(ACTR):
    focus = Buffer()
    visual = Buffer()
    vision_module=SOSVision(visual,delay=0)

    retrieve = Buffer()
    memory = Memory(retrieve)

    def init():
        print('actr init')

    def initializeActrAgent(focus='add ?num1 ?num2 count:None?count sum:None?sum'):
        focus.modify(count=0, sum=num1)
        memory.request('count ?num1 ?next')
        print('initializeActrAgent')

    def newMarine(focus='marine:yes'):
        focus.modify('marine:no')
        print('newMarine')


class BeaconAgent(base_agent.BaseAgent):
  """An agent specifically for solving the MoveToBeacon map."""
  model = ActrAgent()
  actr_env =
  def __init__(self):
      super(BeaconAgent, self).__init__()
      self.model.focus.set('attack marines need:10 count:None')
      self.model.run()
  #def nextAction(actions.FUNCTIONS func):


  def step(self, obs):
    super(BeaconAgent, self).step(obs)
    if FUNCTIONS.Move_screen.id in obs.observation.available_actions:

      player_relative = obs.observation.feature_screen.player_relative

      beacon = _xy_locs(player_relative == _PLAYER_NEUTRAL)

      if not beacon:
        return FUNCTIONS.no_op()

      beacon_center = numpy.mean(beacon, axis=0).round()

      return FUNCTIONS.Move_screen("now", beacon_center)

    else:
      return FUNCTIONS.select_army("select")


def main(unused_argv):

    agent = BeaconAgent()

    try:
        while True:
            with sc2_env.SC2Env(
                    map_name="MoveToBeacon",
                    #players=[sc2_env.Agent(sc2_env.Race.terran),
                    #         sc2_env.Bot(sc2_env.Race.random,
                    #                     sc2_env.Difficulty.very_easy)],
                    players=[sc2_env.Agent(sc2_env.Race.terran)],

                    agent_interface_format=features.AgentInterfaceFormat(
                        feature_dimensions=features.Dimensions(screen=84, minimap=64),
                        use_feature_units=True),
                    step_mul=1,
                    game_steps_per_episode=0,
                    visualize=True) as env:

                agent.setup(env.observation_spec(), env.action_spec())

                timesteps = env.reset()
                agent.reset()



                while True:
                    step_actions = [agent.step(timesteps[0])]
                    if timesteps[0].last():
                        break
                    timesteps = env.step(step_actions)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    app.run(main)