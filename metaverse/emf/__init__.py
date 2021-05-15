from metaverse.emf.emf import getEClassifier, eClassifiers
from metaverse.emf.emf import name, nsURI, nsPrefix, eClass
from metaverse.emf.emf import Model, Module, Buffer, DeclarativeMemory, ProceduralMemory, Motor, Visual, Rule, Chunk, Condition, Environment, Action, WorkingMemory, Slot

__all__ = ['Model', 'Module', 'Buffer', 'DeclarativeMemory', 'ProceduralMemory', 'Motor', 'Visual', 'Rule', 'Chunk', 'Condition', 'Environment', 'Action', 'WorkingMemory', 'Slot']

eSubpackages = []
eSuperPackage = None

# Non opposite EReferences
Model.modules.eType = Module
Model.environment.eType = Environment
Model.buffer.eType = Buffer
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


# Manage all other EClassifiers (EEnum, EDatatypes...)
otherClassifiers = []
for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif._container = emf

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
