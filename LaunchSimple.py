# from __future__ import print_function

import logging
#from pysc2.agents import base_agent
#from pysc2.lib import actions

# from ccm import *
# from ccm.lib.actr import *
import sys


from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, qApp, QApplication, QTextEdit, QFrame
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)

# holds the different cognitive architectures that we have available
class Architectures:
    def __init__(self, cogArchConfig):
        self.cogArchConfig = cogArchConfig  # holds the configuration file


# the environments we can test our agents in
class Environments:
    def __init__(self, envConfig):
        self.envConfig = envConfig  # holds the configuration file





class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # init Main Menu
        #
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        #
        # newAct = QAction('New', self)
        # fileMenu.addAction(newAct)
        #
        # impMenu = QMenu('Import', self)
        # impAct = QAction('Import configuration', self)
        # impMenu.addAction(impAct)
        # fileMenu.addMenu(impMenu)
        #
        # exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        # exitAct.setShortcut('Ctrl+Q')
        # exitAct.setStatusTip('Exit application')
        # exitAct.triggered.connect(qApp.quit)
        # fileMenu.addAction(exitAct)
        #
        # # View menu
        # viewMenu = menubar.addMenu('View')
        # viewStatAct = QAction('View statusbar', self, checkable=True)
        # viewStatAct.setStatusTip('View statusbar')
        # viewStatAct.setChecked(True)
        # viewStatAct.triggered.connect(self.toggleMenu)
        #
        # viewMenu.addAction(viewStatAct)
        #
        # self.toolbar = self.addToolBar('Exit')
        # self.toolbar.addAction(exitAct)
        #
        #


        self.col = QColor(0, 0, 0)

        actrBtn = QPushButton('ACT-R', self)
        actrBtn.setCheckable(True)
        actrBtn.move(10, 10)

        actrBtn.clicked[bool].connect(self.setColor)

        soarBtn = QPushButton('Soar', self)
        soarBtn.setCheckable(True)
        soarBtn.move(10, 60)

        soarBtn.clicked[bool].connect(self.setColor)

        sigmaBtn = QPushButton('Sigma', self)
        sigmaBtn.setCheckable(True)
        sigmaBtn.move(10, 110)

        sigmaBtn.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(300, 300, 280, 170)
        #self.setWindowTitle('Toggle button')

        # Main window object and top frame
        self.setObjectName("MainWindow")
        self.setWindowTitle('Metaverse Launcher')
        self.setWindowIcon(QIcon('QtGUI/cyberbrain.jfif'))

        self.resize(800, 600) # init size, position
        self.show() # render window


    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "ACT-R":
            self.col.setRed(val)
        elif source.text() == "Soar":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())




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





