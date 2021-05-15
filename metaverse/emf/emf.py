from __future__ import annotations
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *

from abc import ABC, abstractmethod

name = 'metamind-emf'
nsURI = 'http://www.chadpeters.net/metamind'
nsPrefix = 'metamind'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)

@abstract
class Model(EObject, metaclass=MetaEClass):
    name = EAttribute(eType=EString)
    done = EAttribute(eType=EBoolean)
    modules = EReference(upper=-1, containment=True)
    environment = EReference(containment=True)
    buffer = EReference()
    _cycle = EAttribute(eType=EFloat)

    def __init__(self, modules=None, name=None, environment=None, buffer=None, done=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()
        if name is not None:
            self.name = name
        if done is not None:
            self.done = done
        if modules:
            self.modules.extend(modules)
        if environment is not None:
            self.environment = environment
        if buffer is not None:
            self.buffer = buffer


    @abstractmethod
    def step(self):
        raise NotImplementedError('Operation step(...) is not yet implemented')
    def run(self):
        raise NotImplementedError('Operation run(...) is not yet implemented')


@abstract
class Module(EObject, metaclass=MetaEClass):
    name = EAttribute(eType=EString)
    buffer = EReference(containment=True)

    def __init__(self, name=None, buffer=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()
        if name is not None:
            self.name = name
        if buffer is not None:
            self.buffer = buffer


class Buffer(EObject, metaclass=MetaEClass):
    name = EAttribute(eType=EString)
    bufferchunk = EReference(containment=True)

    def __init__(self, name=None, bufferchunk=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()
        if name is not None:
            self.name = name
        if bufferchunk is not None:
            self.bufferchunk = bufferchunk


class Rule(EObject, metaclass=MetaEClass):
    name = EAttribute(eType=EString)
    conditions = EReference(containment=True)
    actions = EReference(containment=True)

    def __init__(self, conditions=None, name=None, actions=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()
        if name is not None:
            self.name = name
        if conditions is not None:
            self.conditions = conditions
        if actions is not None:
            self.actions = actions


class Chunk(EObject, metaclass=MetaEClass):
    name = EAttribute(eType=EString)
    slot = EReference(upper=-1, containment=True)

    def __init__(self, name=None, slot=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()
        if name is not None:
            self.name = name
        if slot:
            self.slot.extend(slot)


class Condition(EObject, metaclass=MetaEClass):
    LHSbuffers = EReference(upper=-1, containment=True)

    def __init__(self, LHSbuffers=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()
        if LHSbuffers:
            self.LHSbuffers.extend(LHSbuffers)


class Environment(EObject, metaclass=MetaEClass):
    name = EAttribute(eType=EString)

    def __init__(self, name=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()
        if name is not None:
            self.name = name


class Action(EObject, metaclass=MetaEClass):
    RHSbuffers = EReference(upper=-1, containment=True)

    def __init__(self, RHSbuffers=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()
        if RHSbuffers:
            self.RHSbuffers.extend(RHSbuffers)


class Slot(EObject, metaclass=MetaEClass):
    value = EAttribute(eType=EString)

    def __init__(self, value=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()
        if value is not None:
            self.value = value


@abstract
class DeclarativeMemory(Module):
    dmchunks = EReference(upper=-1, containment=True)

    def __init__(self, dmchunks=None, **kwargs):
        super().__init__(**kwargs)
        if dmchunks:
            self.dmchunks.extend(dmchunks)
    def addDM(self):
        raise NotImplementedError('Operation addDM(...) is not yet implemented')


@abstract
class ProceduralMemory(Module):
    rules = EReference(upper=-1, containment=True)

    def __init__(self, rules=None, **kwargs):
        super().__init__(**kwargs)
        if rules:
            self.rules.extend(rules)
    def addPM(self):
        raise NotImplementedError('Operation addPM(...) is not yet implemented')
    def load(self):
        raise NotImplementedError('Operation load(...) is not yet implemented')


@abstract
class Motor(Module):
    nextaction = EAttribute(eType=EString)

    def __init__(self, nextaction=None, **kwargs):
        super().__init__(**kwargs)
        if nextaction is not None:
            self.nextaction = nextaction
    def setNextAction(self, action=None):
        raise NotImplementedError('Operation setNextAction(...) is not yet implemented')


@abstract
class Visual(Module):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


@abstract
class WorkingMemory(Module):
    wmchunks = EReference(upper=-1, containment=True)

    def __init__(self, wmchunks=None, **kwargs):
        super().__init__(**kwargs)
        if wmchunks:
            self.wmchunks.extend(wmchunks)
    def addWME(self):
        raise NotImplementedError('Operation addWME(...) is not yet implemented')
