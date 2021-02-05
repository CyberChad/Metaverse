#This module should provide template classes that generalize abstract interfaces across all of CMC, to be implemented
#by each architecture.

import logging

class CognitiveCycle:
    pass

class CommonInterface:
    #abstract calls to highest components and modules
    pass

class WorkingMemory:
    pass

class CommonAgent:

    def __init__(self, architecture = None, name = None):
        self.name = name
        self.architecture = architecture

    def templateMethod(self) -> None:

    def description(self):
        return "{} is based on {}".format(self.name, self.architecture)

    #a common agent has interfaces for:
    # structure and processing;
    # memory and content;
    # learning; and
    # perception and motor (action)

    processing = CommonProcessor
    memory = CommonMemory



class AbsBuffer():
    def __init__(self):
        dict buffer = {}

    def get_buffer():
        pass



