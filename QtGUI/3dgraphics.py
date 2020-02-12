## build a QApplication before building other widgets
from pyqtgraph import *
import pyqtgraph as pg
pg.mkQApp()

## make a widget for displaying 3D objects

from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, qApp, QApplication, QTextEdit, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)

import pyqtgraph.opengl as gl

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        view = gl.GLViewWidget()

        ## create three grids, add each to the view
        xgrid = gl.GLGridItem()
        ygrid = gl.GLGridItem()
        zgrid = gl.GLGridItem()
        view.addItem(xgrid)
        view.addItem(ygrid)
        view.addItem(zgrid)

        ## rotate x and y grids to face the correct direction
        xgrid.rotate(90, 0, 1, 0)
        ygrid.rotate(90, 1, 0, 0)

        ## scale each grid differently
        xgrid.scale(0.2, 0.1, 0.1)
        ygrid.scale(0.2, 0.1, 0.1)
        zgrid.scale(0.1, 0.2, 0.1)

        view.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = MainWindow()

    sys.exit(app.exec_())