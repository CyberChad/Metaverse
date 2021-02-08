
from .metamind import getEClassifier, eClassifiers
from .metamind import name, nsURI, nsPrefix, eClass
from .metamind import Model, Module, Buffer, DeclarativeMemory, ProceduralMemory, Motor, Visual, Rule, Chunk, Condition, Environment, Action, WorkingMemory, Slot


from . import metamind

__all__ = ['Model', 'Module', 'Buffer', 'DeclarativeMemory', 'ProceduralMemory', 'Motor',
           'Visual', 'Rule', 'Chunk', 'Condition', 'Environment', 'Action', 'WorkingMemory', 'Slot']

eSubpackages = []
eSuperPackage = None
metamind.eSubpackages = eSubpackages
metamind.eSuperPackage = eSuperPackage

Model.modules.eType = Module
Model.environment.eType = Environment
Module.buffer.eType = Buffer
Buffer.bufferchunk.eType = Chunk
DeclarativeMemory.dmchunks.eType = Chunk
ProceduralMemory.rules.eType = Rule
Rule.conditions.eType = Condition
Rule.actions.eType = Action
Chunk.slot.eType = Slot
Condition.LHSbuffers.eType = Buffer
Action.RHSbuffers.eType = Buffer
WorkingMemory.wmchunks.eType = Chunk

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
