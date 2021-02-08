import os

from metaverse.architectures.arch_factory import \
    AbstractFactory,\
    AbstractModel,\
    AbstractWorkingMemory, \
    AbstractDeclarativeMemory, \
    AbstractProceduralMemory, \
    AbstractPerception, \
    AbstractMotor

import metaverse.architectures.soar.SoarLibs.Python_sml_ClientInterface as sml

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

DEBUG = True


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
        return SoarWorkingMemory()

    def createProceduralMemory(self) -> AbstractProceduralMemory:
        return ProceduralMemory()

    def createPerception(self) -> AbstractPerception:
        return Perception()

    def createMotor(self) -> AbstractMotor:
        return Motor()

# ********************************************
#        Implemented Products
# ********************************************

class SoarModel(AbstractModel):

    def __init__(self):
        #kernel = create_kernel_current_thread()
        self.kernel = create_kernel_new_thread()
        self.agent = create_agent(self.kernel, "agent")

    def load(self, modelFile) -> str:

        self.modelFile = modelFile

        return "The result of SoarModel:create()"

    def step(self) -> str:
        return "The result of SoarModel:step()"

    def run(self, steps=1) -> str:
        self.agent.RunSelf(1)
        #return "The result of SoarModel:run()"

    def reset(self) -> str:
        return "The result of SoarModel:reset()"

    def shutdown(self) -> str:
        self.kernel.DestroyAgent(self.agent)
        self.kernel.Shutdown()
        del self.kernel

        return "The result of SoarModel:shutdown()"



class SoarWorkingMemory(AbstractWorkingMemory):

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

class DeclarativeMemory(AbstractWorkingMemory):

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

    def addPM(self) -> str:
        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

class Perception(AbstractPerception):

    def addPerception(self) -> str:
        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """

class Motor(AbstractMotor):

    def addMotor(self) -> str:
        return "The result of CmuACTrWorkingMemory:addWME()."

    """
    The variant, ACTr WorkingMemory, is only able to work correctly with the variant,
    ACTr Model. Nevertheless, it accepts any instance of AbstractModel as an
    argument.
    """