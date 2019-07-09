import sys, utils
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QPushButton, QWidget, QCompleter, QLineEdit

class UIIntroduction(QWidget):
    def __init__(self, parent=None):
        super(UIIntroduction, self).__init__(parent)

        ## Create Navigation Bar
        utils.initNavigationBar("Introduction",self)

        ## Create Back's QPushButton
        utils.initBackQPushButton(self)

        self.initVariable()
        self.initUI()

    def initVariable(self):
        self.xWith = 450
        self.maxWith = 1080
        self.yHeight = 280
        self.maxHeight = 1920
        self.margin = 60
        self.margin2 = 120

    def initUI(self):

        ## Config Label
        self.lbFind = QtWidgets.QLabel("Finding", self)
        self.lbFind.setGeometry(QtCore.QRect(self.margin, 260, self.maxWith, 80))
        self.lbFind.setFont(utils.font_56)
        self.lbFind.setAlignment(QtCore.Qt.AlignCenter)

        ## Config SearchBar
        listIntro = QStringListModel()
        listIntro.setStringList(
            ['Overview', 'Mission', 'Traditions', 'Our Campuses', 'Key Dates', 'Programs and Degrees',
             'Study Environment', 'DTU Facilities', 'Research', 'Scholarships', 'Faculty'])
        completer = QCompleter()
        completer.setModel(listIntro)
        self.searchBar = QLineEdit("", self)
        self.searchBar.setGeometry(QtCore.QRect(60, 380, self.maxWith - self.margin2, 80))
        self.searchBar.setCompleter(completer)
        self.searchBar.setFont(utils.font_30)

        ## Config Content
        self.overview = QtWidgets.QPushButton("Overview", self)
        self.overview.setGeometry(QtCore.QRect(60, 520, self.xWith, self.yHeight))
        self.overview.setFont(utils.font_15)
        self.overview.setStyleSheet(
            'QPushButton {border: 0px solid gray; background-color: #33313b; color: white; padding-bottom: 30px; padding-right: 30px;}')


        self.mission = QtWidgets.QPushButton("Mission", self)
        self.mission.setGeometry(QtCore.QRect(self.xWith + self.margin2, 520, self.xWith, self.yHeight))
        self.mission.setFont(utils.font_15)
        self.mission.setStyleSheet(
            'QPushButton {border: 0px solid gray; background-color: #d8eff0; color: black; padding-bottom: 30px; padding-right: 30px;}')

        self.tradition = QtWidgets.QPushButton("Traditions", self)
        self.tradition.setGeometry(QtCore.QRect(60, 860, self.xWith, self.yHeight))
        self.tradition.setFont(utils.font_15)
        self.tradition.setStyleSheet(
            'QPushButton {border: 0px solid gray; background-color: #4592af; color: white; padding-bottom: 30px; padding-right: 30px;}')

        self.campus = QtWidgets.QPushButton("Our Campuses", self)
        self.campus.setGeometry(QtCore.QRect(self.xWith + self.margin2, 860, self.xWith, self.yHeight))
        self.campus.setFont(utils.font_15)
        self.campus.setStyleSheet(
            'QPushButton {border: 0px solid gray; background-color: #5588a3; color: white; padding-bottom: 30px; padding-right: 30px;}')


        self.research = QtWidgets.QPushButton("Research", self)
        self.research.setGeometry(QtCore.QRect(60, 1200, self.xWith, self.yHeight))
        self.research.setFont(utils.font_15)
        self.research.setStyleSheet(
            'QPushButton {border: 0px solid gray; background-color: #e3c4a8; color: white; padding-bottom: 30px; padding-right: 30px;}')

        self.scholarship = QtWidgets.QPushButton("Scholarships", self)
        self.scholarship.setGeometry(QtCore.QRect(self.xWith + self.margin2, 1200, self.xWith, self.yHeight))
        self.scholarship.setFont(utils.font_15)
        self.scholarship.setStyleSheet(
            'QPushButton {border: 0px solid gray; background-color: #145374; color: white; padding-bottom: 30px; padding-right: 30px;}')

        self.faculty = QtWidgets.QPushButton("Faculty", self)
        self.faculty.setGeometry(QtCore.QRect(60, 1540, self.xWith, self.yHeight))
        self.faculty.setFont(utils.font_15)
        self.faculty.setStyleSheet(
            'QPushButton {border: 0px solid gray; background-color: #f6f5f5; color: black; padding-bottom: 30px; padding-right: 30px;}')

        self.program = QtWidgets.QPushButton("Programs\n and Degrees", self)
        self.program.setGeometry(QtCore.QRect(self.xWith + self.margin2, 1540, self.xWith, self.yHeight))
        self.program.setFont(utils.font_15)
        self.program.setStyleSheet(
            'QPushButton {border: 0px solid gray; background-color: #00334e; color: white; padding-bottom: 30px; padding-right: 30px;}')

