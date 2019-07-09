import sys, utils
from models import Drinks
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QGroupBox, QGridLayout, QFrame

## Create Ui of Supporting
class UISupporting(QWidget):
    def __init__(self, parent=None):
        super(UISupporting, self).__init__(parent)

        ## Create Navigation Bar
        utils.initNavigationBar("Supporting", self)

        ## Create Back's QPushButton
        utils.initBackQPushButton(self)

        self.viewWater = QWidget(self)
        self.viewWater.setGeometry(QtCore.QRect(10, 50, 520, 810))
        self.viewWater.setStyleSheet('QFrame { background-color: #000;}')

        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100

        self.initUI()
        self.initData()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.viewWater.setLayout(windowLayout)

        self.show()

    def initData(self):
        self.listWater = []

        water = Drinks.Drinks("Sting", "st001", "Image", 10000, 10)

        self.listWater.append(water)

        print ("Element count: ", len(self.listWater))
        print("Element count: ", self.listWater[0].getName())



    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        layout.addWidget(QPushButton('1'), 0, 0)
        layout.addWidget(QPushButton('2'), 0, 1)
        layout.addWidget(QPushButton('3'), 0, 2)
        layout.addWidget(QPushButton('4'), 1, 0)
        layout.addWidget(QPushButton('5'), 1, 1)
        layout.addWidget(QPushButton('6'), 1, 2)
        layout.addWidget(QPushButton('7'), 2, 0)
        layout.addWidget(QPushButton('8'), 2, 1)
        layout.addWidget(QPushButton('9'), 2, 2)

        self.horizontalGroupBox.setLayout(layout)
