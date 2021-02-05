# Memory - from Laird et al 37t Soar Workshop

# Declarative and procedural LTMs contain symbol* structures and associated quantitative metadata
# Global communication is provided by a short-term WM
# Global control is provided by procedural LTM
# Composed of rule-like conditions and actions
# Exerts control by altering contents of WM
# Factual knowledge is provided by declarative LTM

#Learning  - from Laird et al 37t Soar Workshop

# All forms of LTM content are learnable
# Learning occurs online and incrementally, as a side effect of performance and is often based on an inversion of the flow of information from performance
# Procedural learning involves at least reinforcement learning and procedural composition
# Reinforcement learning yields weights over action selection
# Procedural composition yields behavioral automatization
# Declarative learning involves the acquisition of facts and tuning of their metadata
# More complex forms of learning involve combinations of the fixed set of simpler forms of learning

import

class Memory():
    def __init(self):
        pass

class LTM(Memory): #Long-term Memory
    def __init(self):
        pass

class WorkingMemory(Memory):
    def __init(self):
        pass

class Declarative(LTM): #
    def __init(self):
        retrievalBuffer = {}

    #one buffer named retrieval

class Procedural(LTM):
    def __init(self):
        pass

class Working(Memory): #also called Goal Module in ACT-R_CMU
    def __init(self):
        goalBuffer = {} #Dorsal Lateral Pre-Frontal Cortex#one buffer named goal, holds control info;

#only responds to request to create a new goal chunk, placing it in the goal buffer

class Chunk():
    def __init(self, chunkSlots):
        self.type = None #category for the knowledge represented in slots; not in CMC, only aids modeller
        self.slots = chunkSlots
