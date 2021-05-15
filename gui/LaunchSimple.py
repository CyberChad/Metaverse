# from __future__ import print_function

import logging
#from pysc2.agents import base_agent
#from pysc2.lib import actions

# from ccm import *
# from ccm.lib.actr import *
import sys

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

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

from pyqtgraph.dockarea import *


app = QtGui.QApplication([])

#win = pg.GraphicsLayoutWidget(show=True)\
win = QtGui.QMainWindow()
#area = DockArea()
#win.setCentralWidget(area)
# Main window object and top frame
win.setWindowTitle('Metaverse Launcher')
win.setWindowIcon(QIcon('QtGUI/cyberbrain.jfif'))
win.setObjectName("MainWindow")
win.resize(1000,500)

cw = QtGui.QWidget()
win.setCentralWidget(cw)
grid = QtGui.QGridLayout()
cw.setLayout(grid)

#panel = QVBoxLayout()

#layout.addWidget(panel,0,0,1,1)
tree = pg.TreeWidget
#i1 = QtGui.QTreeWidgetItem(["Item 1"])
#tree.addTopLevelItem(i1)



win.show() # render window

win.col = QColor(0, 0, 0)
actrBtn = QPushButton('ACT-R')
actrBtn.setCheckable(True)
actrBtn.move(10, 10)

#actrBtn.clicked[bool].connect(setColor())

soarBtn = QPushButton('Soar')
soarBtn.setCheckable(True)
soarBtn.move(10, 60)

#soarBtn.clicked[bool].connect(setColor())

sigmaBtn = QPushButton('Sigma')
sigmaBtn.setCheckable(True)
sigmaBtn.move(10, 110)

grid.addWidget(tree,1,0,1,1)

import numpy as np

# 3) Plot in chunks, adding one new plot curve for every 100 samples
chunkSize = 100
# Remove chunks after we have 10
maxChunks = 10
startTime = pg.ptime.time()

# Working Memory
win.nextRow()
workMem = win.addPlot(colspan=2, title="Working Memory")
workMem.setLabel('bottom', 'Time', 's')
workMem.setXRange(-10, 0)
vbWM = workMem.getViewBox()
colorWM = (100, 10, 34)
# vbWM.set    # (colorWM)
curvesWM = []
dataWM = np.empty((chunkSize + 1, 2))
ptrWM = 0

# Declarative Memory
win.nextRow()
decMem = win.addPlot(colspan=2, title="Declarative Memory")
decMem.setLabel('bottom', 'Time', 's')
decMem.setXRange(-10, 0)
curvesDM = []
dataDM = np.empty((chunkSize + 1, 2))
ptrDM = 0

def setColor(pressed):

    source = win.sender()

    if pressed:
        val = 255
    else:
        val = 0

    if source.text() == "ACT-R":
        win.col.setRed(val)
    elif source.text() == "Soar":
        win.col.setGreen(val)
    else:
        win.col.setBlue(val)

    win.square.setStyleSheet("QFrame { background-color: %s }" %
                              win.col.name())


def contextMenuEvent(event):
    cmenu = QMenu(win)

    newAct = cmenu.addAction("New")
    opnAct = cmenu.addAction("Open")
    quitAct = cmenu.addAction("Quit")
    action = cmenu.exec_(win.mapToGlobal(event.pos()))

    if action == quitAct:
        qApp.quit()

def toggleMenu(state):

    if state:
        win.statusbar.show()
    else:
        win.statusbar.hide()




# win.nextRow()
# win.figure = Figure()
# win.addItem(win.figure)
# ax = win.figure.add_subplot(111)
# ax.imshow(brain_top)

def updateWM():
    global workMem, dataWM, ptrWM, curvesWM
    now = pg.ptime.time()
    for c in curvesWM:
        c.setPos(-(now - startTime), 0)

    i = ptrWM % chunkSize
    if i == 0:
        curve = workMem.plot(pen='w')
        curvesWM.append(curve)
        last = dataWM[-1]
        dataWM = np.empty((chunkSize + 1, 2))
        dataWM[0] = last
        while len(curvesWM) > maxChunks:
            c = curvesWM.pop(0)
            workMem.removeItem(c)
    else:
        curve = curvesWM[-1]
    dataWM[i + 1, 0] = now - startTime
    dataWM[i + 1, 1] = np.random.normal()
    curve.setData(x=dataWM[:i + 2, 0], y=dataWM[:i + 2, 1])
    ptrWM += 1

def updateDM():
    global decMem, dataDM, ptrDM, curvesDM
    now = pg.ptime.time()
    for c in curvesDM:
        c.setPos(-(now - startTime), 0)

    i = ptrDM % chunkSize
    if i == 0:
        curve = decMem.plot(pen='r')
        curvesDM.append(curve)
        last = dataDM[-1]
        dataDM = np.empty((chunkSize + 1, 2))
        dataDM[0] = last
        while len(curvesDM) > maxChunks:
            c = curvesDM.pop(0)
            decMem.removeItem(c)
    else:
        curve = curvesDM[-1]
    dataDM[i + 1, 0] = now - startTime
    dataDM[i + 1, 1] = np.random.normal()
    curve.setData(x=dataDM[:i + 2, 0], y=dataDM[:i + 2, 1])
    ptrDM += 1

    # update all plots
def update():
    updateWM()
    updateDM()


# def main():

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

    # app = pg.mkQApp()
    # loader = MainWindow()
    # app.exec_()


if __name__ == "__main__":

    # app = QApplication(sys.argv)
    # launcher = MainWindow()
    # sys.exit(app.exec_())


    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
       QtGui.QApplication.instance().exec_()

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

    # *************************************
    # Configure Experiment Type:
    # *************************************
    #
    #     > number of agents per environment??
    #
    #     > number of runs per agent??





