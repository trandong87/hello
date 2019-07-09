from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton, QWidget, QFrame

class UICollectionView(QFrame):

    bd = None

    def __init__(self, x = None, y = None, width = None, hight = None, background = None):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.background = background
        ##self.setStyleSheet('QFrame { background-color: #000;}')
    def setGeometry(self):
        #self.setStyleSheet('QFrame { background-color: #000;}')
        return self.setGeometry(QtCore.QRect(self.x, self.y, self.width, self.hight))

    def numberOfItemsInSection(listItems):
        return len(listItems)

    def cellForItemAt(indexPath):
        cell = UICollectionViewCell()
        return cell


class UICollectionViewCell(QPushButton):
    def __init__(self, x = None, y = None, width = None, hight = None, background = None):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.background = background