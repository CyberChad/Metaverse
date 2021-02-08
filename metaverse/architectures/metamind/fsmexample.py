from pyecore.resources.resource import HttpURI, ResourceSet
from pyecore.utils import DynamicEPackage
from pyecore.ecore import EcoreUtils
import pyecore.behavior as behavior

# Load metamodel
rset = ResourceSet()
uri = HttpURI('https://raw.githubusercontent.com/gemoc/ale-lang/master/'
              'examples/minifsm/model/MiniFsm.ecore')
package_root = rset.get_resource(uri).contents[0]
rset.metamodel_registry[package_root.nsURI] = package_root

fsm = DynamicEPackage(package_root)


# Code for each overridden/added method
@fsm.Transition.behavior
def is_activated(self):
    return (self.fsm.currentEvent == self.event
            and self.incoming == self.fsm.currentState)


@fsm.State.behavior
def execute(self):
    print('Execute', self.name)


@fsm.FSM.behavior
def handle(self, event):
    print('Handle', event)
    self.currentEvent = event
    self.currentState = [t for t in self.transitions
                         if t.is_activated()][0].outgoing


@fsm.FSM.behavior
@behavior.main
def entry_point(self):
    print('Start')
    events = ['event1', 'event2']

    self.currentState = [s for s in self.states
                         if isinstance(s, fsm.Initial)][0]
    self.currentState.execute()

    for event in events:
        self.handle(event)
        self.currentState.execute()

    print('End')


# Load the model
uri = HttpURI('https://raw.githubusercontent.com/gemoc/ale-lang/master/'
              'examples/minifsm/model/FSM.xmi')
resource = rset.get_resource(uri)
root = resource.contents[0]

# Execute the model
behavior.run(root)