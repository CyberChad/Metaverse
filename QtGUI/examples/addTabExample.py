from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class mainForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('Let\'s Rock!')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setMaximumSize(QtCore.QSize(560, 522))
        self.setMinimumSize(QtCore.QSize(560, 522))

        layout = QtWidgets.QVBoxLayout(self)

        groupBoxGD = QtWidgets.QGroupBox('Click Button to add a Tab', self)

        layout2 = QtWidgets.QVBoxLayout(groupBoxGD)

        hrLWGDLink = QtWidgets.QWidget(groupBoxGD)
        hrLGD = QtWidgets.QVBoxLayout(hrLWGDLink)
        hrLGD.setContentsMargins(0, 0, 0, 0)
        btnAddTab = QtWidgets.QPushButton(hrLWGDLink)
        btnAddTab.setText('Add tab')

        hrLGD.addWidget(btnAddTab)
        self.tabWidget = QtWidgets.QTabWidget(hrLWGDLink)
        hrLGD.addWidget(self.tabWidget)
        layout2.addWidget(hrLWGDLink)
        layout.addWidget(groupBoxGD)
        btnAddTab.clicked.connect(self.addProjectTab)

    def addProjectTab(self):
        tab = QtWidgets.QWidget()
        self.tabWidget.addTab(tab, "tab")

app = QtWidgets.QApplication(sys.argv)
w = mainForm()
w.show()
sys.exit(app.exec_())