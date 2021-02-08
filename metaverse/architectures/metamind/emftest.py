import metaverse.architectures.metamind as metamind

import pyecore

from pyecore.utils import dispatch

from pyecore.resources import ResourceSet, URI

from pyecore.ecore import EClass, EObject, EAttribute
from pyecore import ecore, utils

rset = ResourceSet()
resource = rset.get_resource(URI('metamind.ecore'))
mm_root = resource.contents[0]
rset.metamodel_registry[mm_root.nsURI] = mm_root

# At this point, the .ecore is loaded in the 'rset' as a metamodel

resource = rset.get_resource(URI('counting_model.xmi'))
model_root = resource.contents[0]

#print(f"{model_root}")

#for x in EObject.allInstances():
#   print(x)

from metaverse.architectures.metamind import Chunk, Slot

class MetamindSwitch(object):

    @dispatch
    def env_switch(self, o):
        print('Visiting a ', o.eClass.name, ' named ', o.name)

    @dispatch
    def do_switch(self, o):
        print('Fallback for objects of kind ', o.eClass.name, 'value ', o.name)

    @do_switch.register(metamind.Environment)
    def chunk_switch(self, o):
        print('Visiting a ', o.eClass.name, ' named ', o.name)

    @do_switch.register(metamind.Chunk)
    def chunk_switch(self, o):
        print('Visiting a ', o.eClass.name, ' named ', o.name)

    @do_switch.register(metamind.Slot)
    def slot_switch(self, o):
        print('Reading a ', o.eClass.name, ' titled ', o.value)


switch = MetamindSwitch()
# assuming we have a Library instance in 'mylib'
for obj in model_root.eAllContents():

    value = None
    if "Environment" in str(type(obj)):
        name = obj.eClass.name
        if hasattr(obj.eClass,'value'):
            value = obj.value
        else:
            value = obj.name
        print (f"{name} {value}")

    if "Buffer" in str(type(obj)):
        name = obj.eClass.name
        if hasattr(obj.eClass,'value'):
            value = obj.value
        print (f"Buffer: {name} {value}")

    if "Chunk" in str(type(obj)):
        name = obj.eClass.name
        if hasattr(obj.eClass.name,'value'):
            value = obj.value
        print (f"Chunk: {name} {value}")



# At this point, the model instance is loaded!

# #define chunk slots
# slot1 = metamind.Slot("slotval1")
# slot2 = metamind.Slot("slotval2")
#
# #define chunks
# chunk1 = metamind.Chunk("chunk1name",)
# chunk1.slot.
# chunk2 = metamind.Chunk("name2","slot2")
#
# myDM = metamind.DeclarativeMemory()
# myModel = metamind.Model("testModel")


