from metaverse.architectures.arch_factory import AbstractFactory,AbstractModel,AbstractWorkingMemory

class CmuActrFactory(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def createModel(self) -> AbstractModel:
        return CmuActrModel()

    def createWorkingMemory(self) -> AbstractWorkingMemory:
        return CmuACTrWorkingMemory()


class CmuActrModel(AbstractModel):

    def create(self) -> str:
        return "The result of CmuActrModel:create()"

    def step(self) -> str:
        return "The result of CmuActrModel:step()"

    def run(self) -> str:
        return "The result of CmuActrModel:run()"

    def reset(self) -> str:
        return "The result of CmuActrModel:reset()"

    def shutdown(self) -> str:
        return "The result of CmuActrModel:shutdown()"


class CmuACTrWorkingMemory(AbstractWorkingMemory):

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
