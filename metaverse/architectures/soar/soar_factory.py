import os
import time

from metaverse.architectures.arch_factory import \
    AbstractFactory,\
    AbstractModel,\
    AbstractWorkingMemory, \
    AbstractDeclarativeMemory, \
    AbstractProceduralMemory, \
    AbstractPerception, \
    AbstractMotor

from metaverse.architectures.soar.pysoarlib import \
    AgentConnector,\
    SoarAgent,\
    SoarWME

import metaverse.architectures.soar.SoarLibs.Python_sml_ClientInterface as sml

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

DEBUG = True

import metaverse.architectures.soar.pysoarlib
import metaverse.architectures.soar.SoarLibs
from metaverse.architectures.soar.pysoarlib import \
    AgentConnector, \
    SoarAgent, \
    SoarWME

# def create_input_wmes(agent):
#     gym_id = agent.GetInputLink().CreateIdWME('gym')
#     cart_pos = gym_id.CreateFloatWME('cart-position', 0.)
#     cart_vel = gym_id.CreateFloatWME('cart-velocity', 0.)
#     pole_pos = gym_id.CreateFloatWME('pole-angle', 0.)
#     pole_vel = gym_id.CreateFloatWME('pole-tip-velocity', 0.)
#
#     return (cart_pos, cart_vel, pole_pos, pole_vel)


class SimpleConnector(AgentConnector):
    def __init__(self, agent):
        AgentConnector.__init__(self, agent)
        self.add_output_command("increase-number")
        self.num = SoarWME("number", 0)
        self.target = SoarWME("target", 10)

    def on_input_phase(self, input_link):
        if not self.num.is_added():
            self.num.add_to_wm(input_link)
        else:
            self.num.update_wm()

    def on_init_soar(self):
        self.num.remove_from_wm()

    def on_output_event(self, command_name, root_id):
        if command_name == "increase-number":
            self.process_increase_command(root_id)

    def process_increase_command(self, root_id):
        number = root_id.GetChildInt("number")
        if number:
            self.num.set_value(self.num.val + number)
        root_id.AddStatusComplete()

class GymConnector(AgentConnector):
    """Handle arbitrary Gym inputput and output data

    Input:
        - on_input_phase will be automatically called before each input phase
        - adds observation vector to WMEs
    Output:
        - call add_output_command to add the name of an output-link command to look for
        - on_output_event will then be called if such a command is added by the agent
        - sends commands as actions
    """

    def __init__(self, agent, motor, perception):

        AgentConnector.__init__(self, agent)
        self.motor = motor
        self.perception = perception
        self.waiting = False

        #TODO: loop through obs and action space; for action in agent.actions[]:

        # self.add_output_command("increase-number")
        # self.num = SoarWME("number", 0)

        # self.add_output_command("direction")
        self.add_output_command("move-cart")

        self.cart_pos = SoarWME("cart-position", 0.)
        self.cart_vel = SoarWME("cart-velocity", 0.)
        self.pole_pos = SoarWME("pole-angle", 0.)
        self.pole_vel = SoarWME("pole-tip-velocity", 0.)

    def on_input_phase(self, input_link):
        """update working memory, automatically called before each input phase """

        print(f"on_input_phase()")

        #cycle through WMEs, add if missing, and update.

        #global input_wmes
        #(cart_pos, cart_vel, pole_pos, pole_vel) = input_wmes

        # if not self.waiting:

        observation = self.perception.observation
        self.cart_pos.set_value(observation[0])
        self.cart_vel.set_value(observation[1])
        self.pole_pos.set_value(observation[2])
        self.pole_vel.set_value(observation[3])

            # self.waiting = True

        #TODO: loop through collection of WMEs

        if not self.cart_pos.is_added():
            self.cart_pos.add_to_wm(input_link)
        else:
            self.cart_pos.update_wm()
        if not self.cart_vel.is_added():
            self.cart_vel.add_to_wm(input_link)
        else:
            self.cart_vel.update_wm()
        if not self.pole_pos.is_added():
            self.pole_pos.add_to_wm(input_link)
        else:
            self.pole_pos.update_wm()
        if not self.pole_vel.is_added():
            self.pole_vel.add_to_wm(input_link)
        else:
            self.pole_vel.update_wm()

        # if not self.num.is_added():
        #     self.num.add_to_wm(input_link)
        # else:
        #     self.num.update_wm()

    def on_init_soar(self):
        """handles an init-soar event (remove references to SML objects """

        print(f"Connector:on_init_soar()")

        # if self.current_observation != None:
        #     self.current_observation.remove_from_wm()
        # if self.next_action != None:
        #     self.next_action.remove_from_wm()

        if not self.cart_pos != None:
            self.cart_pos.remove_from_wm()

        if not self.cart_vel != None:
            self.cart_vel.remove_from_wm()

        if not self.pole_pos != None:
            self.pole_pos.remove_from_wm()

        if not self.pole_vel != None:
            self.pole_vel.remove_from_wm()

        # self.num.remove_from_wm()

    def on_output_event(self, command_name, root_id):
        """handle output commands with the given name (added by add_output_command)

        root_id is the root Identifier of the command (e.g. (<output-link> ^command_name <root_id>)
        """
        print(f"**** OUTPUT : {command_name}")

        # if command_name == "increase-number":
        #     self.process_increase_command(root_id)

        if command_name == "move-cart":
            self.process_move_direction(root_id)

    def process_move_direction(self, root_id):
        # next_action  = root_id.GetChildString("direction")
        next_action = root_id.GetChildInt("direction")
        # print(f"MOVE DIRECTION: {next_action}")
        if next_action:
            # self.motor.next_action = next_action
            print(f"MOVE DIRECTION: {next_action}")
            self.motor.next_action = next_action
        root_id.AddStatusComplete()

# ********************************************
#        Implemented Factory
# ********************************************

class SoarFactory(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def createModel(self) -> AbstractModel:
        return SoarModel()

    def createWorkingMemory(self) -> AbstractWorkingMemory:
        return SoarWorkingMemory()

    def createDeclarativeMemory(self) -> AbstractDeclarativeMemory:
        return SoarDeclarativeMemory()

    def createProceduralMemory(self) -> AbstractProceduralMemory:
        return SoarProceduralMemory()

    def createPerception(self) -> AbstractPerception:
        return SoarPerception()

    def createMotor(self) -> AbstractMotor:
        return SoarMotor()

# ********************************************
#        Implemented Products
# ********************************************


def register_print_callback(kernel, agent, function, user_data=None):
    agent.RegisterForPrintEvent(sml.smlEVENT_PRINT, function, user_data)


def callback_print_message(mid, user_data, agent, message):
    print(message.strip())

class SoarModel(AbstractModel):


    def __init__(self):
        print("SoarModel().__init__(self)")
        self.working = SoarWorkingMemory(self)
        self.declarative = SoarDeclarativeMemory(self)
        self.procedural = SoarProceduralMemory(self)
        self.perception = SoarPerception(self)
        self.motor = SoarMotor(self)

    def create_kernel(self):
        kernel = sml.Kernel.CreateKernelInCurrentThread()
        if not kernel or kernel.HadError():
            print("Error creating kernel: " + kernel.GetLastErrorDescription())
            exit(1)
        return kernel

    def create_agent(self, kernel, name):
        agent = kernel.CreateAgent("agent")
        if not agent:
            print("Error creating agent: " + kernel.GetLastErrorDescription())
            exit(1)
        return agent

    def load(self, modelFile="soar_agent.config", adapter="psych") -> str:

        self.config_path = "architectures/soar/tests/"+adapter+"/"+modelFile
        print(f"loading soar model from: {self.config_path}")

        global input_wmes
        self.adapter = adapter

        if adapter == "psych": #Uses new AgentConnector

            self.agent = SoarAgent(config_filename=self.config_path, write_to_stdout=True)
            self.modelFile = modelFile

            # connector_switch = {
            #     "psych": SimpleConnector(self.agent),
            #     "cart-pole": GymConnector(self.agent, self.motor, self.perception)
            # }

            self.agent.add_connector(adapter, SimpleConnector(self.agent))
            self.agent.connect()

        elif adapter == "cart-pole":
            self.kernel = self.create_kernel()
            self.agent = self.create_agent(self.kernel, "agent")
            register_print_callback(self.kernel, self.agent, callback_print_message, None)

            #TODO: move this to config file
            map = ['cart-position', 'cart-velocity', 'pole-angle', 'pole-tip-velocity']
            self.perception.create_input_wmes(self.agent, map)

            print(self.agent.ExecuteCommandLine("source architectures/soar/tests/cart-pole/cart-pole.soar"))

        elif adapter == "starcraft":
            self.kernel = self.create_kernel()
            self.agent = self.create_agent(self.kernel, "agent")
            register_print_callback(self.kernel, self.agent, callback_print_message, None)
            map = ['beacon_x', 'beacon_y']
            self.perception.create_input_wmes(self.agent, map)
            print(self.agent.ExecuteCommandLine("source architectures/soar/tests/StarCraft2/starcraft2.soar"))

        else: #shouldn't be here!
            print(f"ERROR: Couldn't find adapter {adapter}")

        return "The result of SoarModel:create()"



    def step(self) -> str:
        # self.agent.execute_command("print --depth 3 s1")
        # self.agent.execute_command("print --depth 3 i2")
        # self.agent.execute_command("print --depth 3 i3")

        #TODO: call update() for each registered module

        if self.adapter == "psych":
            self.agent.execute_command("run 1")  # runs for 1 decision cycles

        #if self.connector == "cart-pole":
        else:
            #self.update_input_wmes(self.perception.observation)
            self.kernel.RunAllAgents(1) #run for one decision cycle

            #TODO: move this to motor.update()
            move_cmd = self.motor.get_move_command(self.agent, self.adapter)
            if move_cmd is not None:
                self.motor.next_action = move_cmd

        # time.sleep(0.1)
        return "The result of SoarModel:step()"

    def run(self, steps=1) -> str:
        self.agent.execute_command("run "+str(steps))
        return "The result of SoarModel:run()"

    def reset(self) -> str:
        self.agent.ExecuteCommandLine("init-soar")
        return "The result of SoarModel:reset()"

    def shutdown(self) -> str:

        if self.adapter == "psych":
            self.agent.kill()
        else:
            self.kernel.DestroyAgent(self.agent)
            self.kernel.Shutdown()
            del self.kernel

        return "The result of SoarModel:shutdown()"

class SoarWorkingMemory(AbstractWorkingMemory):

    def __init__(self, model=None):
        self.model = model

    def addWME(self) -> str:
        return "The result of SoarWorkingMemory:addWME()."

    def removeWME(self, collaborator: AbstractModel):
        """
        The variant, SoarWorkingMemory, is only able to work correctly with the
        variant, Soar Model. Nevertheless, it accepts any instance of
        AbstractModel as an argument.
        """
        result = collaborator.load()
        return f"The result of the Soar WorkingMemory collaborating with the ({result})"

class SoarDeclarativeMemory(AbstractWorkingMemory):

    def __init__(self, model=None):
        self.model = model

    def addWME(self) -> str:
        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

    def removeWME(self, collaborator: AbstractModel) -> str:
        result = collaborator.create()
        return f"The result of the ACTr WorkingMemory collaborating with the ({result})"



class SoarProceduralMemory(AbstractProceduralMemory):

    def __init__(self, model=None):
        self.model = model

    def addPM(self) -> str:
        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

class SoarPerception(AbstractPerception):

    def __init__(self, model=None):
        self.model = model
        self.observation = [0,0,0,0]
        self.input_wmes = ()

    def create_input_wmes(self, agent, map=None):
        self.agent = agent
        gym_id = self.agent.GetInputLink().CreateIdWME('gym')

        self.input_wmes = []

        if map is not None:
            print("SoarPerception:create_input_wmes()")
            for ix in range(0,len(map)):
                wme_name = map[ix]
                print(f"wme_name: {wme_name}")
                wm_element = gym_id.CreateFloatWME(wme_name, 0.)
                self.input_wmes.append(wm_element)

    def update_input_wmes(self, observation):

        #global input_wmes

        if observation is not None:
            self.observation = observation
            print(f"observation: {observation}")
            print(f"obs length: {len(observation)}")
            for ix in range(0,len(observation)):
                self.input_wmes[ix].Update(observation[ix])

    def update_model_action(self, obs):
        print(f"Perception():update_model_action: {obs}")

        self.observation = obs

        if obs is not None:
            self.update_input_wmes(self.observation)


    def addPerception(self) -> str:
        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

    def setObservationSpace(self, map=None):

        self.obs_map = []

        if map is not None:
            self.obs_map = map
        else:
            for i in range(self.observation_shape):
                self.obs_map += f"obs_{i}"

class SoarMotor(AbstractMotor):

    def __init__(self, model=None):
        self.model = model
        self.next_action=0

    def addMotor(self) -> str:
        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

    def setActionSpace(self, space):
        self.action_space = space

    def parse_output_commands(self, agent, structure):
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

        # callback registry

    def get_move_command(self, agent, adapter):

        output_command_list = {}

        if adapter == 'cart-pole':
            output_command_list = {'move-cart': ['direction']}
        elif adapter == 'starcraft':
            output_command_list = {'move-marine': ['location']}
            move_cmd = self.model.perception.observation
            return move_cmd
        else: #shouldn't be here!!
            print("Error: invalid motor adapter")
        # Maps to: (<s> ^output-cmd <output-cmd>) // (<output-cmd> ^direction <dir>)

        if agent.Commands():
            (commands, mapping) = self.parse_output_commands(agent, output_command_list)
            print(f"commands: {commands}")
            print(f"mapping: {mapping}")

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