from os import environ as env
import sys
import gym
import threading
import queue

DEBUG = False

# if "DYLD_LIBRARY_PATH" in env:
#     LIB_PATH = env["DYLD_LIBRARY_PATH"]
# elif "LD_LIBRARY_PATH" in env:
#     LIB_PATH = env["LD_LIBRARY_PATH"]
# elif "PATH" in env:
#     LIB_PATH = env["SOAR"]
# else:
#     print("Soar LIBRARY_PATH environment variable not set; quitting")
#     exit(1)
# sys.path.append(LIB_PATH)

import Python_sml_ClientInterface as sml

last_run_passed = False
num_consecutive_passes = 0
is_paused = False
episode_num = 1


class CliThread(threading.Thread):

    def __init__(self, q_main_thread):
        if DEBUG: print("CliThread().__init__()")
        self.queue_main = q_main_thread
        threading.Thread.__init__(self)

    def run(self):
        if DEBUG: print("CliThread().run()")
        cmd = "None"
        while cmd not in ("exit", "quit"):
            cmd = input("soar> ")
            self.queue_main.put(cmd)


def create_kernel_current_thread():
    if DEBUG: print("create_kernel()")
    kernel = sml.Kernel.CreateKernelInCurrentThread()
    if not kernel or kernel.HadError():
        print("Error creating kernel: " + kernel.GetLastErrorDescription())
        exit(1)
    return kernel

def create_kernel_new_thread():
    if DEBUG: print("create_kernel()")
    kernel = sml.Kernel.CreateKernelInNewThread()
    if not kernel or kernel.HadError():
        print("Error creating kernel: " + kernel.GetLastErrorDescription())
        exit(1)
    return kernel


def create_agent(kernel, name):
    if DEBUG: print("create_agent()")
    agent = kernel.CreateAgent("agent")
    if not agent:
        print("Error creating agent: " + kernel.GetLastErrorDescription())
        exit(1)
    return agent



# This is standard debug output, might want to consider using XML
def callback_print_message(mid, user_data, agent, message):
    if DEBUG: print("callback_print_message()")
    print(message.strip())

# This is standard debug output, might want to consider using XML
def callback_xml_message(mid, user_data, agent, message):
    if DEBUG: print("callback_xml_message()")
    print("XML Message: <"+message.strip()+">")

def register_print_callback(kernel, agent, function, user_data=None):
    agent.RegisterForPrintEvent(sml.smlEVENT_PRINT, function, user_data)

def register_xml_callback(kernel, agent, function, user_data=None):
    agent.RegisterForPrintEvent(sml.smlEVENT_XML_TRACE_OUTPUT, function, user_data)


# called by get_move_command()
def parse_output_commands(agent, structure):
    commands = {}
    mapping = {}
    for cmd in range(0, agent.GetNumberCommands()):
        error = False
        command = agent.GetCommand(cmd)
        cmd_name = command.GetCommandName()
        if cmd_name in structure:
            parameters = {}
            for param_name in structure[cmd_name]:
                param_value = command.GetParameterValue(param_name)
                if param_value:
                    parameters[param_name] = param_value
            if not error:
                commands[cmd_name] = parameters
                mapping[cmd_name] = command
        else:
            error = True
        if error:
            command.AddStatusError()
    return commands, mapping


def get_move_command(agent):
    if DEBUG: print("get_move_command()")
    output_command_list = {'move-cart': ['direction']}
    # Maps to: (<s> ^output-cmd <output-cmd>) // (<output-cmd> ^direction <dir>)

    if agent.Commands():
        (commands, mapping) = parse_output_commands(agent, output_command_list)

        move_cart_cmd = commands['move-cart']
        direction = move_cart_cmd['direction']

        mapping['move-cart'].CreateStringWME('status', 'complete')

        if direction == 'left':
            move_cmd = 0
        else:
            move_cmd = 1

        print("Soar agent key press: " + str(move_cmd))
        return move_cmd

    return None

def test_get_all_commands(agent):
    if DEBUG: print("test_get_all_commands()")

    if agent.Commands():

        for cmd in range(0, agent.GetNumberCommands()):
            error = False
            command = agent.GetCommand(cmd)
            cmd_name = command.GetCommandName()
            # if cmd_name in structure:
            #     parameters = {}
            #     for param_name in structure[cmd_name]:
            param_value_x = command.GetParameterValue('valx')
            param_value_y = command.GetParameterValue('valy')
            #         if param_value:
            #             parameters[param_name] = param_value
            #     if not error:
            #         commands[cmd_name] = parameters
            #         mapping[cmd_name] = command
            # else:
            #     error = True
            # if error:
            #     command.AddStatusError()

            print("Soar agent command: " + str(cmd_name))
            print("Soar agent values: " + str(param_value_x)+" "+str(param_value_y))
            move_cmd = param_value_x, param_value_y
        return move_cmd

    return None



# Initialize the observation space as Working Memory Elements
# This should mirror the obs returned from the environment.

def create_input_wmes(agent):
    if DEBUG: print("create_input_wmes()")

    gym_id = agent.GetInputLink().CreateIdWME('gym')
    loc_x = gym_id.CreateFloatWME('x', 0.)
    loc_y = gym_id.CreateFloatWME('y', 0.)


    return (loc_x, loc_y)

# Update the observation space in Working Memory Elements

def update_input_wmes(observation):
    if DEBUG: print("update_input_wmes()")

    global input_wmes
    (pos_x, pos_y) = input_wmes

    neutral_y, neutral_x = (obs[0] == _PLAYER_NEUTRAL).nonzero()

    target_x = int(neutral_x.mean())
    target_y = int(neutral_y.mean())

    pos_x.Update(target_x)
    pos_y.Update(target_y)


def print_agent_stats(agent):
    print("-Print S1:")
    print(agent.ExecuteCommandLine("print s1"))  # print topstate
    # print(agent.ExecuteCommandLine("print i1")) # print I/O links
    print("-Print I2:")
    print(agent.ExecuteCommandLine("print --depth 3 i2"))  # print input-link
    print("-Print I3:")
    print(agent.ExecuteCommandLine("print --depth 3 i3"))  # print output-link
    print("-Print I4:")
    print(agent.ExecuteCommandLine("print --depth 3 i4"))  # print output-link
    # print(agent.ExecuteCommandLine("print --depth 3 M1"))  # print output-link

#============================================
#=================  MAIN  ===================
#============================================

if __name__ == "__main__":

    # Create the user input thread and queue for return commands

    #queue_user_cmds = queue.Queue()
    #user_cmd_thread = CliThread(queue_user_cmds)
    #user_cmd_thread.start()

    # Create the soar agent
    kernel = create_kernel_current_thread()
    #kernel = create_kernel_new_thread()

    agent = create_agent(kernel, "agent")
    register_print_callback(kernel, agent, callback_print_message, None)

    register_xml_callback(kernel, agent, callback_xml_message, None)

    print("autoCommit: "+str(kernel.IsAutoCommitEnabled()))

    print(agent.ExecuteCommandLine("source soar-basic-example.soar"))  # TODO: Why does sub-goaling run out of memory?
    #print(agent.LoadProductions("soar-basic-example.soar"))
    #print(agent.ExecuteCommandLine("print propose*initialize-agent"))

    # Interact with the virtual environment

    #kernel.RunAllAgents(1)


    """
    Example command usages:
        print(agent.ExecuteCommandLine("print s1"))
        print(agent.ExecuteCommandLine("stats"))
        print(agent.ExecuteCommandLine("epmem --stats"))
        print(agent.ExecuteCommandLine("sp {test (state <s> ^superstate nil) --> (<s> ^foo bar)}"))
        print(agent.ExecuteCommandLine("print test"))  
    
    """

    print("*** Init-Soar ***")
    agent.ExecuteCommandLine("init-soar")

    print("-Print S1:")
    print(agent.ExecuteCommandLine("print s1"))  # print topstate

    #agent.RunSelf(2)
    print("-Print I2:")
    print(agent.ExecuteCommandLine("print --depth 3 i2"))  # print input-link

    print("*** Populate Input Link ***")
    testInputLink = agent.GetInputLink()
    testOutputLink = agent.GetOutputLink()
    attribs_id = testInputLink.CreateIdWME('gym')
    #stringElem = attribs_id.CreateStringWME('string_attrib', 'chad')
    #floatElem = attribs_id.CreateFloatWME('float_attrib', 10.5)
    intElemx = attribs_id.CreateIntWME('x', 7)
    intElemy = attribs_id.CreateIntWME('y', 9)

    print(".Run 1.")
    agent.RunSelf(1)
    #agent.RunSelfTilOutput()

    print_agent_stats(agent)

    #print(agent.ExecuteCommandLine("print --depth 3 M1"))  # print output-link

    #agent.RunSelf(2)
    print(".Run 1.")
    agent.RunSelf(1)

    numCmd = agent.GetNumberCommands()
    print("Number Commands: " + str(numCmd))

    ### CMD HERE #####

    test_get_all_commands(agent)

    print(".Run 1.")
    agent.RunSelf(1)

    test_get_all_commands(agent)

    print_agent_stats(agent)

    # Read output-link WMEs and Feedback
    print("*** Test Out-link WME and Feedback ***")

    #testOutId = testOutputLink.get
    #outValId = testInputLink.CreateIdWME('gym')
    # stringElem = attribs_id.CreateStringWME('string_attrib', 'chad')
    # floatElem = attribs_id.CreateFloatWME('float_attrib', 10.5)
    #val = attribs_id.CreateIntWME('x', 7)

    print(".Run 1.")
    kernel.RunAllAgents(1)

    print("-Print I3:")
    print(agent.ExecuteCommandLine("print --depth 3 i3"))  # print output-link
    print("-Print I4:")
    print(agent.ExecuteCommandLine("print --depth 3 i4"))  # print output-link



    #test_get_all_commands(agent)

    numCmd = agent.GetNumberCommands()
    print("Number Commands: "+str(numCmd))
    testcmd = agent.GetCommand(numCmd)
    print("Get Command: " + str(testcmd))
    # – String = WMElement.GetAVribute();
    # – Int = Iden7fier.GetNumberChildren();
    # – WMElement = Iden7fier.GetChild(Int);
    # – WMElement = Iden7fier.FindByAVribute(String, Int)
    # – *Element = WMElement.ConvertTo * Element();
    # – Iden7fier.AddStatus << Complete Error >> ();

    #print(agent.ExecuteCommandLine("stats"))

    # Clean up environment and agent
    #gym_env.close()

    kernel.DestroyAgent(agent)
    kernel.Shutdown()
    del kernel
