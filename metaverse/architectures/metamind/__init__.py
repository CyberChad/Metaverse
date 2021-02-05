# """
# Module metamind
#
# Sample usage :
# 	>>> from metamind import Model
# 		>>> model = Model()
# 		>>> model.name = "..."
# 			>>> model.modules.append(Module())
# 			>>> module  = model.modules[0]
#
# 			>>> model.environment.append(Environment())
# 			>>> environment  = model.environment[0]
# """
from . import *

from metaverse.metamind import *

from .__factory__ import Metamindfactory
"""
Initialize the default instances factory
"""
factory = Metamindfactory()
# here you may redefine the module singletons or do some special tricks

from __common__ import Metamindresourcefactory
resourceFactory = Metamindresourcefactory()
