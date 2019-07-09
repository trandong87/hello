from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton


def initNavigationBar(string, self):
    self.lbNavigation = QtWidgets.QLabel(string, self)
    self.lbNavigation.setGeometry(QtCore.QRect(0, 0, 1080, 80))
    self.lbNavigation.setAlignment(QtCore.Qt.AlignCenter)
    self.lbNavigation.setFont(font_26)
    self.lbNavigation.setStyleSheet('QLabel { background-color: #33313b; color: white; font-weight: bold;}')

def initBackQPushButton(self):
    self.back = QPushButton("Back", self)
    self.back.setGeometry(QtCore.QRect(60, 0, 120, 80))
    self.back.setIcon(QtGui.QIcon("icons/back.png"))
    self.back.setFont(font_20)
    self.back.setIconSize(QtCore.QSize(40, 40))
    self.back.setStyleSheet('QPushButton {border: 0px solid gray; border-radius: 0px; background-color: #33313b; color: white; font-weight: bold; text-align: left;}')

def configQLabel(label, x, y):
    label.setGeometry(QtCore.QRect(x, y, 225, 140))
    ##label.setStyleSheet('QLabel { background-color: white; border: 1px solid gray; border-radius: 5px;}')
    label.setStyleSheet(
        'QPushButton {border: 1px solid gray; border-radius: 5px; padding-bottom: 12px; background: url(\"/home/dom/Desktop/Pycharm/icons/services.png\") center no-repeat;}')
    label.setFont(font_15)
    ##label.setAlignment(QtCore.Qt.AlignCenter)
    ##self.mission.setPixmap(QtGui.QPixmap('/home/dom/Desktop/GUI-Robotics/icons/services.png'))

def setFontSize(x):
    font = QtGui.QFont()
    font.setPointSize(x)
    return font

font_13 = setFontSize(13)
font_14 = setFontSize(14)
font_15 = setFontSize(15)
font_16 = setFontSize(16)
font_17 = setFontSize(17)
font_18 = setFontSize(18)
font_19 = setFontSize(19)
font_20 = setFontSize(20)
font_24 = setFontSize(24)
font_26 = setFontSize(26)
font_28 = setFontSize(28)
font_30 = setFontSize(30)
font_48 = setFontSize(48)
font_56 = setFontSize(56)
font_70 = setFontSize(70)
font_75 = setFontSize(75)
