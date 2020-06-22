# from __future__ import print_function

import logging
#from pysc2.agents import base_agent
#from pysc2.lib import actions

# from ccm import *
# from ccm.lib.actr import *
import sys


# sys.path.append('../../')

#test update 3
#
# class SimpleAgent(base_agent.BaseAgent):
#     def step(self, obs):
#         super(SimpleAgent, self).step(obs)
#
#         return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])
#

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
#     def __init__.py(self, *args, **kwargs):
#         super(MainWindow, self).__init__.py(*args, **kwargs)
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

        #hbox = QHBoxLayout(self)
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        textEdit = QTextEdit()
        vbox.addWidget(textEdit)


        # Main window object and top frame
        self.setObjectName("MainWindow")
        self.setWindowTitle('Metaverse Launcher')
        self.setWindowIcon(QIcon('QtGUI/cyberbrain.jfif'))


        #self.setCentralWidget(textEdit)
        #self.setCentralWidget(vbox)
        self.setLayout(vbox)

        #self.setLayout(vbox)

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



if __name__ == "__main__":

    app = QApplication(sys.argv)
    launcher = MainWindow()
    sys.exit(app.exec_())

    #import sys
    #if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    #    QtGui.QApplication.instance().exec_()

    print("the start of something amazing...")

    # *************************************
    # Choose cognitive architecture
    # *************************************
    #
    #     > ACT-R_CMU
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





