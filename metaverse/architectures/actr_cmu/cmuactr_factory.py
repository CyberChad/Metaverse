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

    def __init__(self):

        cmuactr.reset()

        #self.model_thread = ModelThread()
        self.perception = Perception()
        self.working = WorkingMemory()
        self.declarative = DeclarativeMemory()
        self.procedural = ProceduralMemory()
        self.motor = Motor()

        # generate a default file

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

    def __init__(self):
        pass

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

    def __init__(self):
        pass

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

    def __init__(self):
        pass

    def addPM(self) -> str:
        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

class Perception(AbstractPerception):

    #model_action = 0

    def __init__(self):
        self.observation = [0,0,0,0]

    def update_model_action(self, obs):

        print(f"Perception():update_model_action: {obs}")

        if obs is not None:

            # if goal buffer has been defined, RPC mod-focus to update chunks
            if cmuactr.buffer_read('goal'):
                print("mod_focus")
                cmuactr.mod_focus('cart_pos', obs[0], 'cart_vel', obs[1], 'pole_pos',
                               obs[2], 'pole_vel', obs[3])
            # otherwise init goal with current observation
            else:
                print("goal_focus")
                cmuactr.goal_focus(cmuactr.define_chunks(['isa', 'game-state', 'cart_pos', obs[0],
                                                    'cart_vel', obs[1], 'pole_pos', obs[2], 'pole_vel', obs[3],
                                                    'state', 'start'])[0])

        #global model_action
        #model_action = 0  # replace with action space

        #global running

        #print("act-r running: " + str(running))
        #cmuactr.run(5)
        #return model_action

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

class Motor(AbstractMotor):

    model_action = None
    human_action = None
    next_action = 0
    key_monitor_installed = False


    def __init__(self):

        self.key_monitor_installed = self.add_key_monitor()

    def respond_to_keypress(self, model, key):
        print("respond_to_keypress: " + key)
        #global move_cmd

        if model:
            self.next_action = int(key)
        else:
            self.next_action = 0

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

    def remove_key_monitor(self):

        cmuactr.remove_command_monitor("output-key", "cartpole-key-press")
        cmuactr.remove_command("cartpole-key-press")

        self.key_monitor_installed = False


    def addMotor(self) -> str:

        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

