import os
import time
import importlib
from inspect import getmembers, isfunction

from metaverse.architectures.arch_factory import \
    AbstractFactory,\
    AbstractModel,\
    AbstractWorkingMemory, \
    AbstractDeclarativeMemory, \
    AbstractProceduralMemory, \
    AbstractPerception,\
    AbstractMotor

import ccm
import ccm.lib.actr as actr
from ccm.lib.actr import *
import metaverse.architectures.actr_ccmsuite as ccmsuite

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# ********************************************
#        Implemented Factory
# ********************************************

class CcmFactory(AbstractFactory):
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


class CCMAgent(ACTR): #TODO: move this to external model file

    goal = Buffer()
    perception = Buffer()
    motor = Motor()
    retrieve = Buffer()
    memory = Memory(retrieve)
    next_action = 0

    def init():
        print(f"--Model init--")


    #insert dynamic function definitions here....

    # def initializeAddition(goal='add ?num1 ?num2 count:None?count sum:None?sum'):
    #     goal.modify(count=0, sum=num1)
    #     memory.request('count ?num1 ?next')
    #
    # def terminateAddition(goal='add ?num1 ?num2 count:?num2 sum:?sum'):
    #     goal.set('result ?sum')
    #     print(sum)
    #     #goal.set('add 5 2 count:None sum:None')
    #
    # def incrementSum(goal='add ?num1 ?num2 count:?count!?num2 sum:?sum',
    #                  retrieve='count ?sum ?next'):
    #     goal.modify(sum=next)
    #     memory.request('count ?count ?n2')

    # def incrementCount(goal='add ?num1 ?num2 count:?count sum:?sum',
    #                    retrieve='count ?count ?next'):
    #     goal.modify(count=next)
    #     memory.request('count ?sum ?n2')

class MyEnvironment(ccm.Model):

    key = None #gym_env interprets this as NO_OP (no operation)

    def key_pressed(self, key):
        self.key = key
        print(f"MyEnvironment():key pressed is {key}")


class Model(AbstractModel):

    def __init__(self):
        print(f"Model:__init__()")
        self.ccm_env = MyEnvironment()


        #(sgp :esc t:lf .05:trace-detail high)

    def load(self, prodFile="") -> str:

        #load all the production function names from prodFile
        self.prodFile = prodFile
        prodMod = importlib.import_module(prodFile)
        functions_list = [o for o in getmembers(prodMod) if isfunction(o[1])]

        #for each production, add name and reference to CCMAgent class
        for x in functions_list:
            name = x[0]
            print(f"Adding Production: {name}")
            setattr(CCMAgent, f'{name}', x[1])

        self.agent = CCMAgent()
        self.ccm_env.agent = self.agent

        # self.load(self)

        self.perception = Perception(self.agent)
        self.working = WorkingMemory(self.agent)
        self.declarative = DeclarativeMemory(self.agent)
        self.procedural = ProceduralMemory(self.agent)
        self.motor = Motor(self.ccm_env)
        # generate a default file

        #set default options

        ccm.log_everything(self.agent)

        # This is how to dynamically load production rules

        result = "stub: load ccm actr model"
        # self.agent.goal.set('add 5 2 count:None sum:None')

        return result

    def step(self) -> str:

        # self.agent.run(0.05)
        self.ccm_env.run(0.05)
        # next_action = self.agent.next_action
        # self.motor.next_action = next_action
        next_action = self.motor.update()
        print(f"Model:step() Next Action is: {next_action}")
        # actr.run(1, True)
        #return "The result of CmuActrModel:step()"

    def run(self, seconds) -> str:
        # actr.run(seconds,True)

        # agent.run(seconds)

        self.agent.run()

        return "The result of CmuActrModel:run()"

    def reset(self) -> str:

        self.agent.reset()
        return "The result of CmuActrModel:reset()"

    def shutdown(self) -> str:
        ccm.finished()
        return "The result of CmuActrModel:shutdown()"



class WorkingMemory(AbstractWorkingMemory):

    def __init__(self, agent):
        self.agent = agent

    def addWME(self, memory) -> str:
        self.agent.goal.set(memory)

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

    def __init__(self, agent):
        self.agent = agent


    def addWME(self, memory) -> str:

        self.agent.memory.add(memory)

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

    def __init__(self, agent):
        self.agent = agent

    def addPM(self) -> str:
        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

class Perception(AbstractPerception):

    def __init__(self, agent):
        self.agent = agent

    def addPerception(self, obs) -> str:
        self.obs = obs
        print(f"CCMSuite3 Perception sees: {self.obs}")
        self.update_model_action(obs)
        return True

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

    def transduce(self, obs):

        chunks = ""
        # TODO: read these from a config file for different environments
        #chunknames = ['cart_pos', 'cart_vel', 'pole_pos', 'pole_vel']
        # these aren't strictly necessary for CCMSuite

        num_features = 0

        if self.obs_map is not None:
            num_features = len(self.obs_map)
        else:
            num_features = self.observation_shape

        print(f"num features: {num_features}")
        #chunks.append(chunknames[0])
        chunks += f"{obs[0]}"

        for i in range(1, num_features):
            #chunks.append(chunknames[i])
            chunks += f" {obs[i]}"

        print(f"Transduction: {chunks}")

        return chunks

    def setObservationSpace(self, space, map=None):
        self.observation_space = space

        #transduce the shape size into state space
        self.observation_shape = space.shape[0]

        self.obs_map = []

        if map is not None:
            self.obs_map = map
        else:
            for i in range(self.observation_shape):
                self.obs_map += f"obs_{i}"

    def update_model_action(self, obs):

        self.last_obs = obs
        print(f"CCMSuite3 Perception sees: {self.last_obs}")

        if obs is not None:
            self.last_obs = obs

            temp = self.transduce(obs)
            print("Updating perceptual buffer: "+temp)
            self.agent.perception.set(temp)

class Motor(AbstractMotor):

    model_action = None
    human_action = None

    def __init__(self, ccm_env, default=None):
        self.ccm_env = ccm_env
        #self.next_action = 0

        self.next_action = default #NO_OP test for SC
        print(f"Initializing Motor Module...")

    def setActionSpace(self, space):
        self.action_space = space

    def addMotor(self) -> str:
        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

    def update(self):
        # next_action = self.agent.motor.get()

        key = self.ccm_env.key
        if key is not None:
            print(f"Motor():update key to {key}")
            self.next_action = key

        return self.next_action


    def update_model_selection(self) -> str:
        pass


if __name__ == '__main__':

    # import metaverse.architectures.actr_ccmsuite.prods_test as prods
    print("Pre-run")
    model = Model()
    model.load('metaverse.architectures.actr_ccmsuite.cartpole_prods')

    # log = ccm.log(html=True)
    # self.agent.log = log
    # ccm.log_everything(model.agent)
    # agent.run()
    # model.agent.run(0)
    model.agent.keepAlive = True

    while model.agent.keepAlive:

        model.perception.update_model_action(['1','2','3','4'])
        # model.agent.run(0.05) #time from agent perspective
        model.step()
        print(f"next action: {model.motor.next_action}")
        print("TICK...................")
        time.sleep(1) #time from our perspective

    print("post run")