"""
Carleton Cognitive Modeling implementation of ACT-R by Terry Stewart et al.

"""

import metaverse.architectures.cmc as cmc
import numpy as np


class ActrCcmSuite(cmc.CommonModel):

    """
    Description:
        short intro to this version of ACT-R

    Source:
        Where this implementation came from

    Usage:
        How the architecture is typically launched

    """

    def __init__(self):
        #add custom init here

        pass

    def create(self, name):
        #creation implementation code here
        pass

    def step(self, action):
        #action implementation code here
        pass

    def reset(self):
        #return model to initial state
        pass

    def close(self):
        #graceful shutdown of model and any dispatcher/kernel
        pass