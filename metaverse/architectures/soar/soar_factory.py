from metaverse.architectures.arch_factory import AbstractFactory,AbstractModel,AbstractWorkingMemory

class SoarFactory(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def createModel(self) -> AbstractModel:
        return SoarModel()

    def createWorkingMemory(self) -> AbstractWorkingMemory:
        return SoarWorkingMemory()

"""
Concrete Products are created by corresponding Concrete Factories.
"""

class SoarModel(AbstractModel):

    def create(self) -> str:
        return "The result of SoarModel:create()"

    def step(self) -> str:
        return "The result of SoarModel:step()"

    def run(self) -> str:
        return "The result of SoarModel:run()"

    def reset(self) -> str:
        return "The result of SoarModel:reset()"

    def shutdown(self) -> str:
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
        result = collaborator.create()
        return f"The result of the Soar WorkingMemory collaborating with the ({result})"

