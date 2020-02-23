# from __future__ import print_function

import logging
from pysc2.agents import base_agent
from pysc2.lib import actions

# from ccm import *
# from ccm.lib.actr import *
import sys


# sys.path.append('../../')

class SimpleAgent(base_agent.BaseAgent):
    def step(self, obs):
        super(SimpleAgent, self).step(obs)

        return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])


# holds the different cognitive architectures that we have available
class Architectures:
    def __init__(self, cogArchConfig):
        self.cogArchConfig = cogArchConfig  # holds the configuration file


# the environments we can test our agents in
class Environments:
    def __init__(self, envConfig):
        self.envConfig = envConfig  # holds the configuration file


class Utilities:

    def readFile(file):

        f = open(file, "r")  # here we open file "input.txt". Second argument used to identify that we want to read file
        # Note: if you want to write to the file use "w" as second argument

        for line in f.readlines():  # read lines
            print(line)

        f.close()  # It's important to close the file to free up any system resources.

    def writeFile(fileName):

        logging.info('Calling write file')

        if len(fileName) is 0:
            logging.warning("file is null")

        f = open(file, "a")

        for i in range(5):
            f.write(i)

        f.close()


from pyqtgraph import PlotWidget

# class MainWindow(QtWidgets.QMainWindow):
#
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#
#         #Load the UI Page
#         uic.loadUi('LauncherMain.ui', self)
#
#         #self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])
#
#         self.PlotWidget.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])
#
#     #def plot(self, hour, temperature):
#        #self.GraphWidget.plot(hour, temperature)

from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, qApp, QApplication, QTextEdit, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # Main window object and top frame
        self.setObjectName("MainWindow")
        self.setWindowTitle('Metaverse Launcher')
        self.setWindowIcon(QIcon('QtGUI/cyberbrain.jfif'))

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # init bottom status bar
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        # init Main Menu

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        newAct = QAction('New', self)
        fileMenu.addAction(newAct)

        impMenu = QMenu('Import', self)
        impAct = QAction('Import configuration', self)
        impMenu.addAction(impAct)
        fileMenu.addMenu(impMenu)

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)

        # View menu
        viewMenu = menubar.addMenu('View')
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        # init size, position
        self.resize(800, 600)
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.console
import numpy as np

from pyqtgraph.dockarea import *

app = QtGui.QApplication([])
win = QtGui.QMainWindow()
area = DockArea()
win.setCentralWidget(area)
win.resize(1000,500)

win.setWindowTitle('Metaverse')

#dTop = Dock("dTop", size=(1000, 250))
dBottom = Dock("dBottom", size=(1000, 250))
dLeft = Dock("dLeft", size=(500, 250))
dRight = Dock("dRight", size=(500, 250))


area.addDock(dLeft, 'left')      ## place d1 at left edge of dock area (it will fill the whole space since there are no other docks yet)
area.addDock(dRight, 'right')     ## place d2 at right edge of dock area
area.addDock(dBottom, 'bottom')     ## place d2 at right edge of dock area

## Add widgets into each dock

import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType


## test subclassing parameters
## This parameter automatically generates two child parameters which are always reciprocals of each other
class ComplexParameter(pTypes.GroupParameter):
    def __init__(self, **opts):
        opts['type'] = 'bool'
        opts['value'] = True
        pTypes.GroupParameter.__init__(self, **opts)

        self.addChild({'name': 'A = 1/B', 'type': 'float', 'value': 7, 'suffix': 'Hz', 'siPrefix': True})
        self.addChild({'name': 'B = 1/A', 'type': 'float', 'value': 1 / 7., 'suffix': 's', 'siPrefix': True})
        self.a = self.param('A = 1/B')
        self.b = self.param('B = 1/A')
        self.a.sigValueChanged.connect(self.aChanged)
        self.b.sigValueChanged.connect(self.bChanged)

    def aChanged(self):
        self.b.setValue(1.0 / self.a.value(), blockSignal=self.bChanged)

    def bChanged(self):
        self.a.setValue(1.0 / self.b.value(), blockSignal=self.aChanged)


## test add/remove
## this group includes a menu allowing the user to add new parameters into its child list
class ScalableGroup(pTypes.GroupParameter):
    def __init__(self, **opts):
        opts['type'] = 'group'
        opts['addText'] = "Add"
        opts['addList'] = ['str', 'float', 'int']
        pTypes.GroupParameter.__init__(self, **opts)

    def addNew(self, typ):
        val = {
            'str': '',
            'float': 0.0,
            'int': 0
        }[typ]
        self.addChild(
            dict(name="ScalableParam %d" % (len(self.childs) + 1), type=typ, value=val, removable=True, renamable=True))


params = [
    {'name': 'Agent', 'type': 'group', 'children': [
        {'name': 'Architecture', 'type': 'list', 'values': ["ACT-R","SOAR","Sigma"], 'value': 1},
        {'name': 'Integer', 'type': 'int', 'value': 10},
        {'name': 'Float', 'type': 'float', 'value': 10.5, 'step': 0.1},
        {'name': 'String', 'type': 'str', 'value': "hi"},
        {'name': 'List', 'type': 'list', 'values': [1, 2, 3], 'value': 2},
        {'name': 'Named List', 'type': 'list', 'values': {"one": 1, "two": "twosies", "three": [3, 3, 3]}, 'value': 2},
        {'name': 'Boolean', 'type': 'bool', 'value': True, 'tip': "This is a checkbox"},
        {'name': 'Color', 'type': 'color', 'value': "FF0", 'tip': "This is a color button"},
        {'name': 'Gradient', 'type': 'colormap'},
        {'name': 'Subgroup', 'type': 'group', 'children': [
            {'name': 'Sub-param 1', 'type': 'int', 'value': 10},
            {'name': 'Sub-param 2', 'type': 'float', 'value': 1.2e6},
        ]},
        {'name': 'Text Parameter', 'type': 'text', 'value': 'Some text...'},
        {'name': 'Action Parameter', 'type': 'action'},
    ]},
    {'name': 'Environment', 'type': 'group', 'children': [
        {'name': 'Units + SI prefix', 'type': 'float', 'value': 1.2e-6, 'step': 1e-6, 'siPrefix': True, 'suffix': 'V'},
        {'name': 'Limits (min=7;max=15)', 'type': 'int', 'value': 11, 'limits': (7, 15), 'default': -6},
        {'name': 'DEC stepping', 'type': 'float', 'value': 1.2e6, 'dec': True, 'step': 1, 'siPrefix': True,
         'suffix': 'Hz'},

    ]},
    {'name': 'Numerical Parameter Options', 'type': 'group', 'children': [
        {'name': 'Units + SI prefix', 'type': 'float', 'value': 1.2e-6, 'step': 1e-6, 'siPrefix': True, 'suffix': 'V'},
        {'name': 'Limits (min=7;max=15)', 'type': 'int', 'value': 11, 'limits': (7, 15), 'default': -6},
        {'name': 'DEC stepping', 'type': 'float', 'value': 1.2e6, 'dec': True, 'step': 1, 'siPrefix': True,
         'suffix': 'Hz'},

    ]},
    {'name': 'Save/Restore functionality', 'type': 'group', 'children': [
        {'name': 'Save State', 'type': 'action'},
        {'name': 'Restore State', 'type': 'action', 'children': [
            {'name': 'Add missing items', 'type': 'bool', 'value': True},
            {'name': 'Remove extra items', 'type': 'bool', 'value': True},
        ]},
    ]},
    {'name': 'Extra Parameter Options', 'type': 'group', 'children': [
        {'name': 'Read-only', 'type': 'float', 'value': 1.2e6, 'siPrefix': True, 'suffix': 'Hz', 'readonly': True},
        {'name': 'Renamable', 'type': 'float', 'value': 1.2e6, 'siPrefix': True, 'suffix': 'Hz', 'renamable': True},
        {'name': 'Removable', 'type': 'float', 'value': 1.2e6, 'siPrefix': True, 'suffix': 'Hz', 'removable': True},
    ]},
    ComplexParameter(name='Custom parameter group (reciprocal values)'),
    ScalableGroup(name="Expandable Parameter Group", children=[
        {'name': 'ScalableParam 1', 'type': 'str', 'value': "default param 1"},
        {'name': 'ScalableParam 2', 'type': 'str', 'value': "default param 2"},
    ]),
]

## Create tree of Parameter objects
p = Parameter.create(name='params', type='group', children=params)


## If anything changes in the tree, print a message
def change(param, changes):
    print("tree changes:")
    for param, change, data in changes:
        path = p.childPath(param)
        if path is not None:
            childName = '.'.join(path)
        else:
            childName = param.name()
        print('  parameter: %s' % childName)
        print('  change:    %s' % change)
        print('  data:      %s' % str(data))
        print('  ----------')


p.sigTreeStateChanged.connect(change)


def valueChanging(param, value):
    print("Value changing (not finalized): %s %s" % (param, value))


# Too lazy for recursion:
for child in p.children():
    child.sigValueChanging.connect(valueChanging)
    for ch2 in child.children():
        ch2.sigValueChanging.connect(valueChanging)


def save():
    global state
    state = p.saveState()


def restore():
    global state
    add = p['Save/Restore functionality', 'Restore State', 'Add missing items']
    rem = p['Save/Restore functionality', 'Restore State', 'Remove extra items']
    p.restoreState(state, addChildren=add, removeChildren=rem)


p.param('Save/Restore functionality', 'Save State').sigActivated.connect(save)
p.param('Save/Restore functionality', 'Restore State').sigActivated.connect(restore)

tree = ParameterTree()
tree.setParameters(p, showTop=False)
tree.setWindowTitle('pyqtgraph example: Parameter Tree')

dLeft.addWidget(tree)
state = None

## test save/restore
s = p.saveState()
p.restoreState(s)

wWorking = pg.PlotWidget(title="Working/Processing Memory plot")
wWorking.plot(np.random.normal(size=100))

wProcMem = pg.PlotWidget(title="Procedural Memory plot")
wProcMem.plot(np.random.normal(size=100))

wDeclMem = pg.PlotWidget(title="Declarative Memory plot")
wDeclMem.plot(np.random.normal(size=100))

wMotor = pg.PlotWidget(title="Motor plot")
wMotor.plot(np.random.normal(size=100))

wPerc = pg.PlotWidget(title="Perception plot")
wPerc.plot(np.random.normal(size=100))

dRight.addWidget(wWorking)
dRight.addWidget(wProcMem)
dRight.addWidget(wDeclMem)
dRight.addWidget(wMotor)
dRight.addWidget(wPerc)

win.show()


if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #launcher = MainWindow()
    #sys.exit(app.exec_())

    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

    print("the start of something amazing...")

    # *************************************
    # Choose cognitive architecture
    # *************************************
    #
    #     > ACT-R
    #     > SOAR
    #     > SIGMA?
    #
    #     Choose architecture sub-options for:
    #
    #         > Declarative Memory
    #
    #         > Procedural Memory
    #
    #         > Others??
    #
    # *************************************
    # Choose Environment:
    # *************************************
    #     > Gym
    #     > StarCraft2
    #     > HELK or Qemu machine?
    #
    #     Configure environment-specific options:
    #
    #         > map or challenge
    #
    #         > single or multi-agent
    #
    #         > difficulty rating
    #
    # *************************************
    # Configure Experiment Type:
    # *************************************
    #
    #     > number of agents per environment??
    #
    #     > number of runs per agent??





