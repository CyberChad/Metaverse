import cmuactr as actr
import math
import numbers
from os import environ as env
import sys
import gym
import threading
import queue

actr.load_act_r_model("/home/user/github/Metaverse/Architectures/ACT-R_CMU/cartpole.lisp")

last_run_passed = False
num_consecutive_passes = 0
is_paused = False
episode_num = 1

running = False

model_action = None
human_action = None
move_cmd = 0
key_monitor_installed = False

#Client thread for human intervention
class CliThread(threading.Thread):

    def __init__(self, q_main_thread):
        self.queue_main = q_main_thread
        threading.Thread.__init__(self)

    def run(self):
        cmd = "None"
        while cmd not in ("exit", "quit"):
            cmd = input("CMC> ")
            self.queue_main.put(cmd)

def respond_to_keypress(model,key):
    print("respond_to_keypress: " +key)
    global move_cmd

    if model:
        move_cmd = int(key)
    else:
        move_cmd = 0

def add_key_monitor():
    global key_monitor_installed

    if key_monitor_installed == False:
        actr.add_command("cartpole-key-press",respond_to_keypress,
                         "cartpole task key output monitor")
        actr.monitor_command("output-key","cartpole-key-press")
        key_monitor_installed = True
        print("key monitor installed")

        return True
    else:
        return False

def remove_key_monitor():

    actr.remove_command_monitor("output-key","cartpole-key-press")
    actr.remove_command("cartpole-key-press")

    global key_monitor_installed
    key_monitor_installed = False


def update_model_action(obs):

    print("updat_model_action: ")
    print(obs)
    #if goal buffer has been defined, RPC mod-focus to update chunks
    if actr.buffer_read('goal'):
        print("mod_focus")
        actr.mod_focus('cart_pos',obs[0],'cart_vel', obs[1],'pole_pos',
                       obs[2],'pole_vel',obs[3])
    #otherwise init goal with current observation
    else:
        print("goal_focus")
        actr.goal_focus(actr.define_chunks(['isa','game-state','cart_pos',obs[0],
                                    'cart_vel', obs[1],'pole_pos',obs[2],'pole_vel',obs[3],
                                            'state','start'])[0])

    global model_action
    model_action = 0 #replace with action space

    global running

    print("act-r running: "+str(running))
    actr.run(5)
    return model_action

if __name__ == "__main__":
    # Create the user input thread and queue for return commands

    queue_user_cmds = queue.Queue()
    user_cmd_thread = CliThread(queue_user_cmds)
    user_cmd_thread.start()

    # Create the ACT-R agent
    need_to_remove = add_key_monitor()
    #agent_thread = threading.Thread(target=actr.run(10000), args=sys.argv)
    #agent_thread = threading.Thread(target=actr.run_full_time(1000))

    #agent_thread.start()

    # Create the gym environment
    gym_env = gym.make('CartPole-v0')
    observation = gym_env.reset()


    #model_thread = threading.Thread(target=actr.run(10000), args=sys.argv)
    #model_thread.start()

    step_num = 0

    #print(agent.ExecuteCommandLine("source cart-pole.soar"))

    while True:
        gym_env.render()

        try:
            user_cmd = queue_user_cmds.get(False)
        except queue.Empty:
            pass
        else:
            if user_cmd in ("exit", "quit"):
                break
            elif user_cmd == "pause":
                is_paused = True
            elif user_cmd == "continue":
                is_paused = False
            else:
                #print(actr.ExecuteCommandLine(user_cmd).strip())
                print("no user command")

        if is_paused:
            print("is paused..")
            continue

 #       move_cmd = get_move_command(agent)
        #print("move_cmd is " +str(move_cmd))

        if move_cmd is not None:
            print("move_cmd sent to gym: "+str(move_cmd))
            observation, reward, done, info = gym_env.step(move_cmd)

            step_num = step_num + 1
            update_model_action(observation)

            if done:
                if step_num >= 195:
                    if last_run_passed:
                        num_consecutive_passes = num_consecutive_passes + 1
                    else:
                        last_run_passed = True
                        num_consecutive_passes = 1
                else:
                    last_run_passed = False
                    num_consecutive_passes = 0

                print('Episode, {}, Number of steps, {}, Number of consecutive passes, {}'.format(episode_num, step_num,
                                                                                                  num_consecutive_passes))
                episode_num = episode_num + 1

                step_num = 0
                gym_env.reset()
#                agent.ExecuteCommandLine("init-soar")

    gym_env.close()
 #   kernel.DestroyAgent(agent)
#    kernel.Shutdown()
#    del kernel