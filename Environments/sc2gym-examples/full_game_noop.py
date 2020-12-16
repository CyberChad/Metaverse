"""
   Copyright 2017 Islam Elnabarawy

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import sys

import gym
from absl import flags
from pysc2.lib import actions

# noinspection PyUnresolvedReferences
import sc2gym.envs

from pysc2.env import sc2_env

__author__ = 'Islam Elnabarawy'

FLAGS = flags.FLAGS

_NO_OP = [actions.FUNCTIONS.no_op.id]


def main():
    FLAGS(sys.argv)

    env = gym.make("SC2Game-v0")
    env.settings['map_name'] = 'BuildMarines'
    env.settings['visualize'] = True
    env.settings['players'] = [sc2_env.Agent(sc2_env.Race.terran)]

    obs = env.reset()

    done = False
    while not done:
        action = _NO_OP
        obs, reward, done, _ = env.step(action)

    env.close()


if __name__ == "__main__":
    main()
