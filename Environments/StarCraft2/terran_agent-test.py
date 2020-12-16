from __future__ import print_function

import os
os.environ['MESA_GL_VERSION_OVERRIDE'] = '3.3'
os.environ['MESA_GLSL_VERSION_OVERRIDE'] = '330'

from pysc2.agents import base_agent
from pysc2.env import sc2_env
from pysc2.lib import actions, features, units
from absl import app
import random


import logging
import sys

from pysc2.agents import base_agent
from pysc2.lib import actions

#sys.path.append('../../')

class TerranAgent(base_agent.BaseAgent):
    def __init__(self):
        super(TerranAgent, self).__init__()

        self.attack_coordinates = None

        self.unit_task = 0

        self.building_supply = False

        self.xmean = 0
        self.ymean = 0

        self.cx = 0
        self.cy = 0

        self.radius = 10
        # 1 = build supply depot
        # 2 = build barracks
        # 3 = build marine
        # 4 = attack enemy

        # self.model = ActrAgent()
        # self.model.goal.set('attack marines need:10 count:None')
        # self.model.run()

    def unit_type_is_selected(self, obs, unit_type):
        if (len(obs.observation.single_select) > 0 and
                obs.observation.single_select[0].unit_type == unit_type):
            return True

        if (len(obs.observation.multi_select) > 0 and
                obs.observation.multi_select[0].unit_type == unit_type):
            return True

        return False

    def get_units_by_type(self, obs, unit_type):
        return [unit for unit in obs.observation.feature_units
                if unit.unit_type == unit_type]

    def can_do(self, obs, action):
        return action in obs.observation.available_actions



    def step(self, obs):
        super(TerranAgent, self).step(obs)

        #if this is the first look at the screen, remember where we are relative to the enemy

        if obs.first():
            player_y, player_x = (obs.observation.feature_minimap.player_relative ==
                                  features.PlayerRelative.SELF).nonzero()
            self.xmean = player_x.mean()
            self.ymean = player_y.mean()

            if self.xmean <= 31 and self.ymean <= 31:
                self.attack_coordinates = (49, 49)
            else:
                self.attack_coordinates = (12, 16)

            centers = self.get_units_by_type(obs, units.Terran.CommandCenter)
            center = random.choice(centers)
            self.cx = center.x
            self.cy = center.y



        depots = self.get_units_by_type(obs, units.Terran.SupplyDepot)
        free_supply = (obs.observation.player.food_cap -
                       obs.observation.player.food_used)
        if (free_supply == 0 or len(depots) == 0):
            if self.unit_type_is_selected(obs, units.Terran.SCV):
                if self.can_do(obs, actions.FUNCTIONS.Build_SupplyDepot_screen.id):

                    x = random.randint(self.cx - self.radius, self.cx + self.radius)
                    y = random.randint(self.cy - self.radius, self.cy + self.radius)
                    print("trying to build a supply depot at " + str(x) + " " + str(y))
                    #plan_unit = 0
                    #self.building_supply = True
                    return actions.FUNCTIONS.Build_SupplyDepot_screen("now", (x,y))

            scvs = self.get_units_by_type(obs, units.Terran.SCV)
            if len(scvs) > 0:
                scv = random.choice(scvs)
                self.unit_task = 1
                print("selecting SCV to build supply depot")
                return actions.FUNCTIONS.select_point("select_all_type", (scv.x, scv.y))



        #********** Building Logic **************
        barracks = self.get_units_by_type(obs, units.Terran.Barracks)
        if len(barracks) == 0:
            if self.unit_type_is_selected(obs, units.Terran.SCV):
                if self.can_do(obs, actions.FUNCTIONS.Build_Barracks_screen.id):
                    x = random.randint(self.cx - self.radius, self.cx + self.radius)
                    y = random.randint(self.cy - self.radius, self.cy + self.radius)

                    print("building barracks at "+ str(x) + " " + str(y))

                    # plan_unit = 0
                    return actions.FUNCTIONS.Build_Barracks_screen("now", (x, y))

            scvs = self.get_units_by_type(obs, units.Terran.SCV)
            if len(scvs) > 0:
                scv = random.choice(scvs)
                self.unit_task = 2
                print("selecting SCV to build barracks")
                return actions.FUNCTIONS.select_point("select_all_type", (scv.x, scv.y))

        #********** ATTACK LOGIC *************

        marines = self.get_units_by_type(obs, units.Terran.Marine)
        if len(marines) >= 10:
            self.unit_task = 4
            if self.unit_type_is_selected(obs, units.Terran.Marine):
                if self.can_do(obs, actions.FUNCTIONS.Attack_minimap.id):
                    return actions.FUNCTIONS.Attack_minimap("now",
                                                            self.attack_coordinates)

            if self.can_do(obs, actions.FUNCTIONS.select_army.id):
                return actions.FUNCTIONS.select_army("select")

        # else, build an attack unit (here larva = barracks)
        if self.unit_type_is_selected(obs, units.Terran.Barracks):
            free_supply = (obs.observation.player.food_cap -
                           obs.observation.player.food_used)
            if free_supply > 0:
                if self.can_do(obs, actions.FUNCTIONS.Train_Marine_quick.id):
                    return actions.FUNCTIONS.Train_Marine_quick("now")

        barracks = self.get_units_by_type(obs, units.Terran.Barracks)
        if len(barracks) > 0:
            barrack = random.choice(barracks)
            self.unit_task= 3 #train marines
            return actions.FUNCTIONS.select_point("select_all_type", (barrack.x,
                                                                      barrack.y))

        return actions.FUNCTIONS.no_op()


def main(unused_argv):
    agent = TerranAgent()
    try:
        while True:
            with sc2_env.SC2Env(
                    map_name="Simple64",
                    players=[sc2_env.Agent(sc2_env.Race.terran),
                             sc2_env.Bot(sc2_env.Race.random,
                                         sc2_env.Difficulty.very_easy)],
                    agent_interface_format=features.AgentInterfaceFormat(
                        feature_dimensions=features.Dimensions(screen=84, minimap=64),
                        use_feature_units=True,
                        rgb_dimensions=features.Dimensions(screen=124, minimap=124),
                        action_space=actions.ActionSpace.FEATURES,
                    ),
                    step_mul=16,
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