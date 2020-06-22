import sys
import logging
import time
import threading

import gym
import numpy as np

import ccm
from ccm.lib.actr import *

#from gym_http_client import Client


def heuristic(observation):
    #import numpy as np
    parameters = np.array([ \
        # [ 0.08718784,  0.71794107],
        [0.08718784, -0.71794107],
        [0.37608265, 0.66108118],
        [0.08718784, 0.71794107] \
        ])

    actions = np.zeros(3)

    observation[1] *= 2

    actions[0] = np.matmul(parameters[0], observation)
    actions[1] = np.matmul(parameters[1], observation)
    actions[2] = np.matmul(parameters[2], observation)


    next_action = np.argmax(actions)

    return next_action

#********************** ACT-R_CMU Stuff ******************
class ActrEnvModel(ccm.Model):

    #next_action=ccm.Model(isa='action',press='no_op')
    #screen=ccm.Model(isa='screen',event='none')

    next_action=0

    def start(self):
        #self.log.action=input
        print("start ActrEnvModel")
        # Set up local environment for testing
        # env_id = 'CartPole-v0'
        env_id = 'MountainCar-v0'
        # env_id = 'LunarLander-v2'
        # env_id = 'SpaceInvaders-v1'
        env = gym.make(env_id)
        self.state = env.reset()

        max_steps = 200
        reward = 0
        done = False
        total_reward = 0
        steps = 0

        reward = 0
        done = False
        episode_count = 100

        self.next_action=0 #to be updated by motor module

        while steps < 1000:
            # curr_state = self.parent.state

            #envModel.state = state
            # envModel.screen.event = 'update'

            self.state, reward, done, info = env.step(self.next_action)

            total_reward += reward

            # if steps % 20 == 0 or done:
            # output = ','.join(['%.2f' % num for num in s])
            output = ["{:+0.2f}".format(x) for x in self.state]
            output.append(self.next_action)
            # print(output)

            # print(["{:+0.2f}".format(x) for x in s]+"{:+0.2f}".format(a))
            # print("step {} total_reward {:+0.2f}".format(steps, total_reward))
            env.render()

            steps += 1

            yield 0.05

    def reset(self):
        self.state = self.env.reset()

class MotorModule(ccm.Model):
    beacons = 0
    next_action = ''

    def do_action(self):
        #print(f"do the action: {action}")

        next_action = heuristic(self.parent.parent.state)
        print("new best action:%s",next_action)
        self.parent.parent.next_action = next_action

        time.sleep(0.05)


class ActrAgent(ACTR):

    motor = MotorModule()

    focus = Buffer()  # goal buffer
    visual = Buffer()
    vision_module=SOSVision(visual,delay=0)

    retrieve = Buffer()
    memory = Memory(retrieve)

    def init():
        print("ACT-R_CMU agent init")
        focus.set('game:play')

    def action(focus='game:play'):
        motor.do_action()
        #print("action")


        # this is where we make all the hard decisions ;)

       #best_action = np.argmax(all_actions)

        #self.log.action=input

    def stop_production(self, focus="stop"):
        self.stop()


def gym_env(*args):

    # Set up local environment for testing
    # env_id = 'CartPole-v0'
    env_id = 'MountainCar-v0'
    #env_id = 'LunarLander-v2'
    # env_id = 'SpaceInvaders-v1'
    env = gym.make(env_id)
    state = env.reset()

    max_steps = 200
    reward = 0
    done = False
    total_reward = 0
    steps = 0


    reward = 0
    done = False
    episode_count = 100

    while steps < 1000:

        #curr_state = self.parent.state

        envModel.state = state
        #envModel.screen.event = 'update'

        all_actions = heuristic(state)

        # this is where we make all the hard decisions ;)
        best_action = np.argmax(all_actions)
        #yield 1

        #self.parent.press(best_action)


        state, reward, done, info = env.step(best_action)

        total_reward += reward

        # if steps % 20 == 0 or done:
        #output = ','.join(['%.2f' % num for num in s])
        output = ["{:+0.2f}".format(x) for x in state]
        output.append(best_action)
        #print(output)

        # print(["{:+0.2f}".format(x) for x in s]+"{:+0.2f}".format(a))
        # print("step {} total_reward {:+0.2f}".format(steps, total_reward))
        env.render()

        steps += 1



##############################################################
######################   MAIN   ##############################
##############################################################

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Set up agent
    envModel = ActrEnvModel()
    agent= ActrAgent()
    #ccm.log_everything(agent)
    #agent.focus.set('game:play')

    envModel.agent = ActrAgent()
    ccm.log_everything(envModel)

    # Run experiment, with monitor
    #outdir = '/tmp/random-agent-results'

    #env_thread = threading.Thread(target=gym_env, args=sys.argv)
    #env_thread.start()

    agent_thread = threading.Thread(target=envModel.run(), args=sys.argv)
    agent_thread.start()

