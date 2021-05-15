# -*- coding: utf-8 -*-
"""
Various methods of drawing scrolling plots.
"""
#import initExample  ## Add path to library (just for examples; you do not need this)

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import cm
from matplotlib.colors import ListedColormap,LinearSegmentedColormap
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from PIL import Image

import numpy as np

win = pg.GraphicsWindow()
win.setWindowTitle('Metaverse Activity by Buffer')

class BOLDstuff():


    #2D Gaussian function
    def twoD_Gaussian(x, y, xo, yo, sigma_x, sigma_y):
        a = 1./(2*sigma_x**2) + 1./(2*sigma_y**2)
        c = 1./(2*sigma_x**2) + 1./(2*sigma_y**2)
        g = np.exp( - (a*((x-xo)**2) + c*((y-yo)**2)))
        return g.ravel()


    def transparent_cmap(cmap, N=255):
        "Copy colormap and set alpha values"

        mycmap = cmap
        mycmap._init()
        mycmap._lut[:,-1] = np.linspace(0, 0.8, N+4)
        return mycmap


    #Use base cmap to create transparent
    DM_cmap = transparent_cmap(plt.cm.Reds) #Red
    PM_cmap = transparent_cmap(plt.cm.Blues) #Blue
    WM_cmap = transparent_cmap(plt.cm.Oranges) #Brownish

    # create yellow colormaps
    N = 256
    yellow = np.ones((N, 4))
    yellow[:, 0] = np.linspace(255/256, 1, N) # R = 255
    yellow[:, 1] = np.linspace(232/256, 1, N) # G = 232
    yellow[:, 2] = np.linspace(11/256, 1, N)  # B = 11

    yellow_cmp = ListedColormap(yellow)
    yellow_cmp2 = ListedColormap(yellow)

    Visual_cmap = transparent_cmap(yellow_cmp) #Yellow

    Motor_cmap = transparent_cmap(plt.cm.Greens) #Green

    # Import image and get x and y extents
    brain_top = Image.open('./brain.jpg')
    #brain_side = Image.open('./brain_side.jpg')
    p = np.asarray(brain_top).astype('float')
    w, h = brain_top.size
    y, x = np.mgrid[0:h, 0:w]

    #Plot image and overlay colormap
    fig, ax = plt.subplots(1, 1)
    ax.imshow(brain_top)

    DMGaussL = twoD_Gaussian(x, y, .3*x.max(), .3*y.max(), .05*x.max(), .05*y.max())
    DMGaussR = twoD_Gaussian(x, y, .7*x.max(), .3*y.max(), .05*x.max(), .05*y.max())

    PMGaussL = twoD_Gaussian(x, y, .4*x.max(), .4*y.max(), .05*x.max(), .05*y.max())
    PMGaussR = twoD_Gaussian(x, y, .6*x.max(), .4*y.max(), .05*x.max(), .05*y.max())

    WMGaussL = twoD_Gaussian(x, y, .45*x.max(), .5*y.max(), .05*x.max(), .05*y.max())
    WMGaussR = twoD_Gaussian(x, y, .55*x.max(), .5*y.max(), .05*x.max(), .05*y.max())

    MotorGaussL = twoD_Gaussian(x, y, .4*x.max(), .7*y.max(), .05*x.max(), .05*y.max())
    MotorGaussR = twoD_Gaussian(x, y, .6*x.max(), .7*y.max(), .05*x.max(), .05*y.max())

    VisualGaussL = twoD_Gaussian(x, y, .45*x.max(), .9*y.max(), .05*x.max(), .05*y.max())
    VisualGaussR = twoD_Gaussian(x, y, .55*x.max(), .9*y.max(), .05*x.max(), .05*y.max())

    DM_cbL = ax.contourf(x, y, DMGaussL.reshape(x.shape[0], y.shape[1]), 15, cmap=DM_cmap)
    DM_cbR = ax.contourf(x, y, DMGaussR.reshape(x.shape[0], y.shape[1]), 15, cmap=DM_cmap)

    PM_cbL = ax.contourf(x, y, PMGaussL.reshape(x.shape[0], y.shape[1]), 15, cmap=PM_cmap)
    PM_cbR = ax.contourf(x, y, PMGaussR.reshape(x.shape[0], y.shape[1]), 15, cmap=PM_cmap)

    WM_cbL = ax.contourf(x, y, WMGaussL.reshape(x.shape[0], y.shape[1]), 15, cmap=WM_cmap)
    WM_cbR = ax.contourf(x, y, WMGaussR.reshape(x.shape[0], y.shape[1]), 15, cmap=WM_cmap)

    Motor_cbL = ax.contourf(x, y, MotorGaussL.reshape(x.shape[0], y.shape[1]), 15, cmap=Motor_cmap)
    Motor_cbR = ax.contourf(x, y, MotorGaussR.reshape(x.shape[0], y.shape[1]), 15, cmap=Motor_cmap)

    Vis_cbL = ax.contourf(x, y, VisualGaussL.reshape(x.shape[0], y.shape[1]), 15, cmap=Visual_cmap)
    Vis_cbR = ax.contourf(x, y, VisualGaussR.reshape(x.shape[0], y.shape[1]), 15, cmap=Visual_cmap)


# # 1) Simplest approach -- update data in the array such that plot appears to scroll
# #    In these examples, the array size is fixed.
# #p1 = win.addPlot()
# #p2 = win.addPlot()
# data1 = np.random.normal(size=300)
# curve1 = p1.plot(data1)
# curve2 = p2.plot(data1)
# ptr1 = 0


# def update1():
#     global data1, curve1, ptr1
#     data1[:-1] = data1[1:]  # shift data in the array one sample left
#     # (see also: np.roll)
#     data1[-1] = np.random.normal()
#     curve1.setData(data1)
#
#     ptr1 += 1
#     curve2.setData(data1)
#     curve2.setPos(ptr1, 0)


# 2) Allow data to accumulate. In these examples, the array doubles in length
# #    whenever it is full.
# win.nextRow()
# p3 = win.addPlot()
# p4 = win.addPlot()
# # Use automatic downsampling and clipping to reduce the drawing load
# p3.setDownsampling(mode='peak')
# p4.setDownsampling(mode='peak')
# p3.setClipToView(True)
# p4.setClipToView(True)
# p3.setRange(xRange=[-100, 0])
# p3.setLimits(xMax=0)
# curve3 = p3.plot()
# curve4 = p4.plot()
#
# data3 = np.empty(100)
# ptr3 = 0
#
#
# def update2():
#     global data3, ptr3
#     data3[ptr3] = np.random.normal()
#     ptr3 += 1
#     if ptr3 >= data3.shape[0]:
#         tmp = data3
#         data3 = np.empty(data3.shape[0] * 2)
#         data3[:tmp.shape[0]] = tmp
#     curve3.setData(data3[:ptr3])
#     curve3.setPos(-ptr3, 0)
#     curve4.setData(data3[:ptr3])


# 3) Plot in chunks, adding one new plot curve for every 100 samples
chunkSize = 100
# Remove chunks after we have 10
maxChunks = 10
startTime = pg.ptime.time()


#Working Memory
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

#Declarative Memory
win.nextRow()
decMem = win.addPlot(colspan=2, title="Declarative Memory")
decMem.setLabel('bottom', 'Time', 's')
decMem.setXRange(-10, 0)
curvesDM = []
dataDM = np.empty((chunkSize + 1, 2))
ptrDM = 0

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


timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
