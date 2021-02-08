"""Definition of meta model 'metamind'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'metamind'
nsURI = 'http://www.chadpeters.net/metamind'
nsPrefix = 'metamind'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class Model(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    modules = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    environment = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, modules=None, name=None, environment=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if modules:
            self.modules.extend(modules)

        if environment is not None:
            self.environment = environment


@abstract
class Module(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    buffer = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, name=None, buffer=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if buffer is not None:
            self.buffer = buffer


class Buffer(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    bufferchunk = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, name=None, bufferchunk=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if bufferchunk is not None:
            self.bufferchunk = bufferchunk


class Rule(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    conditions = EReference(ordered=True, unique=True, containment=True, derived=False)
    actions = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, conditions=None, name=None, actions=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if conditions is not None:
            self.conditions = conditions

        if actions is not None:
            self.actions = actions


class Chunk(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    slot = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, slot=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if slot:
            self.slot.extend(slot)


class Condition(EObject, metaclass=MetaEClass):

    LHSbuffers = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, LHSbuffers=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if LHSbuffers:
            self.LHSbuffers.extend(LHSbuffers)


class Environment(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


class Action(EObject, metaclass=MetaEClass):

    RHSbuffers = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, RHSbuffers=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if RHSbuffers:
            self.RHSbuffers.extend(RHSbuffers)


class Slot(EObject, metaclass=MetaEClass):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value


class DeclarativeMemory(Module):

    dmchunks = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, dmchunks=None, **kwargs):

        super().__init__(**kwargs)

        if dmchunks:
            self.dmchunks.extend(dmchunks)


class ProceduralMemory(Module):

    rules = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, rules=None, **kwargs):

        super().__init__(**kwargs)

        if rules:
            self.rules.extend(rules)


class Motor(Module):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Visual(Module):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class WorkingMemory(Module):

    wmchunks = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, wmchunks=None, **kwargs):

        super().__init__(**kwargs)

        if wmchunks:
            self.wmchunks.extend(wmchunks)
