import utils
from PyQt5 import QtCore, QtGui
from collection import UICollection
from PyQt5.QtWidgets import QPushButton, QWidget, QCompleter, QLineEdit, QFrame


## Create Ui of Maps Direction
class UIMapsDirection(QWidget):
    def __init__(self, parent=None):

        super(UIMapsDirection, self).__init__(parent)

        self.map = QWidget(self)
        self.map.setGeometry(QtCore.QRect(0, 0, 1080, 1920))
        self.map.setStyleSheet('QWidget { background: url(\"images/map.png\");}')

        ## Create Navigation Bar
        utils.initNavigationBar("", self)

        ## Create Back's QPushButton
        utils.initBackQPushButton(self)

        self.viewSearch = QFrame(self)
        self.viewSearch.setGeometry(QtCore.QRect(200, 10, 800, 60))
        self.viewSearch.setStyleSheet('QWidget {border-radius: 10px; background: white;}')

        ## Create Back's QPushButton
        self.mic = QPushButton("", self.viewSearch)
        self.mic.setGeometry(QtCore.QRect(750, 0, 40, 60))
        self.mic.setIcon(QtGui.QIcon("icons/mic.png"))
        self.mic.setIconSize(QtCore.QSize(25, 25))

        ## Config SearchBar
        listIntro = QtCore.QStringListModel()
        listIntro.setStringList(
            ['Overview', 'Mission', 'Traditions', 'Our Campuses', 'Key Dates', 'Programs and Degrees',
             'Study Environment', 'DTU Facilities', 'Research', 'Scholarships', 'Faculty'])
        completer = QCompleter()
        completer.setModel(listIntro)
        self.searchBar = QLineEdit("", self.viewSearch)
        self.searchBar.setGeometry(QtCore.QRect(30, 0, 700, 60))
        self.searchBar.setCompleter(completer)
        self.searchBar.setFont(utils.font_15)

        ## Config zoom out, zoom in Button
        self.btZoomIn = QPushButton("+", self.map)
        self.btZoomIn.setGeometry(QtCore.QRect(850, 150, 80, 80))
        self.btZoomIn.setStyleSheet('QPushButton { background: white;}')
        self.btZoomIn.setFont(utils.font_16)

        self.btZoomOut = QPushButton("-", self.map)
        self.btZoomOut.setGeometry(QtCore.QRect(850, 250, 80, 80))
        self.btZoomOut.setStyleSheet('QPushButton { background: white;}')
        self.btZoomOut.setFont(utils.font_16)


