import os
import time

from metaverse.architectures.arch_factory import \
    AbstractFactory,\
    AbstractModel,\
    AbstractWorkingMemory, \
    AbstractDeclarativeMemory, \
    AbstractProceduralMemory, \
    AbstractPerception,\
    AbstractMotor

import metaverse.architectures.actr_cmu.cmuactr
import metaverse.architectures.actr_cmu.cmuactr as cmuactr

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# ********************************************
#        Implemented Factory
# ********************************************

class CmuActrFactory(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def createModel(self) -> AbstractModel:
        return Model()

    def createWorkingMemory(self) -> AbstractWorkingMemory:
        return WorkingMemory()

    def createDeclarativeMemory(self) -> AbstractDeclarativeMemory:
        return DeclarativeMemory()

    def createProceduralMemory(self) -> AbstractProceduralMemory:
        return ProceduralMemory()

    def createPerception(self) -> AbstractPerception:
        return Perception()

    def createMotor(self) -> AbstractMotor:
        return Motor()

# ********************************************
#        Implemented Products
# ********************************************

import threading

class ModelThread(threading.Thread):

    def __init__(self):
        #self.queue_main = q_main_thread
        threading.Thread.__init__(self)

    def run(self):
        cmuactr.run(10)

    def step(self):
        cmuactr.run(1)

class Model(AbstractModel):

    # Create the ACT-R agent

    # add_key_monitor() #TODO hook this up to the SC2 env.ACTIONS
    # add_mouse_monitor()  # TODO hook this up to the SC2 env.ACTIONS

    def __init__(self):

        cmuactr.reset()

        #self.model_thread = ModelThread()
        self.perception = Perception(self)
        self.working = WorkingMemory(self)
        self.declarative = DeclarativeMemory(self)
        self.procedural = ProceduralMemory(self)
        self.motor = Motor(self)

        # generate a default file

        self.window = cmuactr.open_exp_window("Find Beacon")
        cmuactr.install_device(self.window)

        #set default options

        #(sgp :esc t:lf .05:trace-detail high)

    def load(self, modelFile="") -> str:
        self.modelFile = modelFile

        result = cmuactr.load_act_r_model(DIR_PATH + "/" + modelFile)

        return result

    def step(self) -> str:

        #self.obs = obs
        #print(f"Model step sees: {obs}")

        #pass observation to motor module
        #self.perception.addPerception(obs)
        #cmuactr.run(0.5, True) #TODO: determine correct running time
        # for i in range(0,10):
        #     cmuactr.current_connection.evaluate("run-step")
        # time.sleep(0.05)
        #self.model_thread.step()
        cmuactr.run(1)

        #return "The result of CmuActrModel:step()"

        return 0

    def run(self, seconds=999,realTime=False) -> str:
        """Run """
        #cmuactr.run(seconds,realTime)
        self.model_thread.start()
        return "The result of CmuActrModel:run()"

    def reset(self) -> str:
        cmuactr.reset()
        return "The result of CmuActrModel:reset()"

    def shutdown(self) -> str:
        return "The result of CmuActrModel:shutdown()"


class WorkingMemory(AbstractWorkingMemory):

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


class DeclarativeMemory(AbstractWorkingMemory):

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



class ProceduralMemory(AbstractProceduralMemory):

    def __init__(self, model=None):
        self.model = model

    def addPM(self) -> str:
        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

class Perception(AbstractPerception):

    #model_action = 0

    def __init__(self, model):
        self.observation = []
        self.model = model


    def transduce(self, obs):

        self.last_obs = obs
        chunks = []
        #TODO: read these from a config file for different environments
        #chunknames = ['cart_pos', 'cart_vel', 'pole_pos', 'pole_vel']
        chunknames = self.obs_map

        num_features = 0

        if self.obs_map is not None:
            num_features = len(self.obs_map)
        else:
            num_features = self.observation_shape

        chunks.append(chunknames[0])
        chunks.append(obs[0])

        for i in range(1, num_features):
            chunks.append(chunknames[i])
            chunks.append(obs[i])

        print(f"Transduction: {chunks}")

        return chunks

    def setObservationSpace(self, map=None):
        # self.observation_space = space
        #
        # #transduce the shape size into state space
        #
        # if space is not None:
        #     self.observation_shape = space
        # else:
        #     self.observation_shape = len(map)

        self.obs_map = []

        if map is not None:
            self.obs_map = map
        else:
            for i in range(self.observation_shape):
                self.obs_map += f"obs_{i}"

    def update_model_action(self, obs):

        print(f"Perception():update_model_action: {obs}")

        if obs is not None:

            #generic logic to present the "screen" to the agent
            focus_chunks = self.transduce(obs)

            window = self.model.window

            cmuactr.add_text_to_exp_window(window, "B", x=obs[0], y=obs[1])

            # if goal buffer has been defined, RPC mod-focus to update chunks
            if cmuactr.buffer_read('goal'):
                print("mod_focus")

                #cmuactr.mod_focus('cart_pos', obs[0], 'cart_vel', obs[1], 'pole_pos',
                               #obs[2], 'pole_vel', obs[3])
                cmuactr.mod_focus(focus_chunks)
            # otherwise init goal with current observation
            else:
                print("goal_focus")
                init_focus = ['isa', 'game-state']
                init_focus += focus_chunks
                init_focus += ['state', 'start']

                print(f"Init Focus: {init_focus}")

                cmuactr.goal_focus(cmuactr.define_chunks(init_focus)[0])

    def addPerception(self, obs) -> str:
        self.obs = obs
        print(f"CMU Perception sees: {self.obs}")
        self.update_model_action(obs)
        return True

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

class Sc2Perception(AbstractPerception):
    # model_action = 0

    def __init__(self, model):
        self.observation = []
        self.model = model

    def transduce(self, obs):

        chunks = []

        chunks.append(f"obs_{0}")
        chunks.append(obs[0])

        for i in range(1, self.observation_shape + 1):
            chunks.append(f"obs_{i}")
            chunks.append(obs[i])

        print(f"Transduction: {chunks}")

        return chunks

    def setObservationSpace(self, map=None):
        # self.observation_space = space
        #
        # # transduce the shape size into state space
        # if space is not None:
        #     shape = space.shape[0]
        #     self.observation_shape = space.shape[0]

        self.obs_map = []

        if map is not None:
            self.obs_map = map
        else:
            for i in range(self.observation_shape):
                self.obs_map += f"obs_{i}"

    def update_model_action(self, obs):

        print(f"Perception():update_model_action: {obs}")

        if obs is not None:

            # generic logic to present the "screen" to the agent
            focus_chunks = self.transduce(obs)

            # if goal buffer has been defined, RPC mod-focus to update chunks
            if cmuactr.buffer_read('goal'):
                print("mod_focus")

                # cmuactr.mod_focus('cart_pos', obs[0], 'cart_vel', obs[1], 'pole_pos',
                # obs[2], 'pole_vel', obs[3])
                cmuactr.mod_focus(focus_chunks)
            # otherwise init goal with current observation
            else:
                print("goal_focus")
                init_focus = ['isa', 'game-state']
                init_focus += focus_chunks
                init_focus += ['state', 'start']

                print(f"Init Focus: {init_focus}")

                cmuactr.goal_focus(cmuactr.define_chunks(init_focus)[0])


    def addPerception(self, obs) -> str:
        self.obs = obs
        print(f"CMU Perception sees: {self.obs}")
        self.update_model_action(obs)
        return True


class Motor(AbstractMotor):

    model_action = None
    human_action = None
    next_action = 0
    key_monitor_installed = False


    def __init__(self, model=None):

        self.model = model
        self.key_monitor_installed = self.add_key_monitor()
        self.busy = False

    def setActionSpace(self, space):
        self.action_space = space

    def respond_to_keypress(self, model, key):
        print(f"respond_to_keypress: {key}")
        global move_cmd
        global busy

        cursor = self.model.perception.last_obs

        if str(key) == 'c':
            print(f"force_mouseclick: {cursor}")
            self.next_action = cursor
        elif model:
            self.next_action = int(key)
        else:
            self.next_action = 0

    def force_mouseclick(self, click):  # TODO see if we can include a mouse move and click
        print("force_mouseclick: " + click)

    def add_key_monitor(self):

        if self.key_monitor_installed == False:
            cmuactr.add_command("cartpole-key-press", self.respond_to_keypress,
                                "cartpole task key output monitor")

            # "output-key" is the signal produced by the keyboard device

            cmuactr.monitor_command("output-key", "cartpole-key-press")
            key_monitor_installed = True
            print("key monitor installed")

            return True
        else:
            return False

    def respond_to_mouseclick(model, click, finger=None):  # TODO see if we can include a mouse move and click
        print("respond_to_mouseclick: " + click)
        global move_cmd

        if model:
            move_cmd = click
        else:
            move_cmd = 0

    def remove_key_monitor(self):

        cmuactr.remove_command_monitor("output-key", "cartpole-key-press")
        cmuactr.remove_command("cartpole-key-press")

        self.key_monitor_installed = False

    def add_mouse_monitor():
        global mouse_monitor_installed

        if mouse_monitor_installed == False:
            cmuactr.add_command("sc2-mouse-click", respond_to_mouseclick,
                             "sc2 task mouse output monitor")
            cmuactr.monitor_command("click-mouse", "sc2-mouse-click")
            mouse_monitor_installed = True
            print("mouse monitor installed")

            return True
        else:
            return False

    def remove_mouse_monitor():

        cmuactr.remove_command_monitor("click-mouse", "sc2-mouse-click")
        cmuactr.remove_command("sc2-mouse-click")

        global mouse_monitor_installed
        mouse_monitor_installed = False


    def addMotor(self) -> str:

        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

