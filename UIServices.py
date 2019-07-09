import utils
from models import Drinks

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFrame

font_14 = utils.setFontSize(14)
viewWaterIsActive = None
viewFoodIsActive = None

## Create Ui of Services
class UIServices(QWidget):
    def __init__(self, parent=None):
        super(UIServices, self).__init__(parent)

        ## Create Navitation Bar
        utils.initNavigationBar("Services", self)

        ## Create Back's QPushButton
        utils.initBackQPushButton(self)

        self.initVariable()
        self.initUI()
        self.initData()

    def initVariable(self):
        self.listDrinks = []

    def initUI(self):
        ## Create QPushButton of Water's tab
        self.btWater = QPushButton("Drinks", self)
        self.btWater.setGeometry(QtCore.QRect(20, 100, 520, 80))
        self.btWater.setFont(utils.font_24)
        self.btWater.clicked.connect(self.onClickWater)

        ## Create QPushButton of Food's tab
        self.btFood = QPushButton("Food", self)
        self.btFood.setGeometry(QtCore.QRect(540, 100, 520, 80))
        self.btFood.setFont(utils.font_24)
        self.btFood.clicked.connect(self.onClickFood)

        ## Create a line under Water's QPushButton
        self.wgWater = QtWidgets.QLabel(self)
        self.wgWater.setGeometry(QtCore.QRect(540, 180, 520, 20))

        ## Create a line under Food's QPushButton
        self.wgFood = QtWidgets.QLabel(self)
        self.wgFood.setGeometry(QtCore.QRect(20, 180, 520, 20))

        self.initViewWater()
        self.initViewFood()

    def initData(self):
        sting = Drinks.Drinks("Sting", "st001", "Image", 10000, 10)
        revine = Drinks.Drinks("Revine", "rv001", "Image", 10000, 10)
        number1 = Drinks.Drinks("Number One", "nb001", "Image", 10000, 10)
        cocacola = Drinks.Drinks("Coca Cola", "cl001", "Image", 10000, 10)
        pepsi = Drinks.Drinks("Pepsi", "ps001", "Image", 10000, 10)

        self.listDrinks.append(sting)
        self.listDrinks.append(revine)
        self.listDrinks.append(number1)
        self.listDrinks.append(cocacola)
        self.listDrinks.append(pepsi)

        print(len(self.listDrinks))


    def initViewWater(self):
        ## Create view Water
        self.viewWater = QFrame(self)
        self.viewWater.setGeometry(QtCore.QRect(0, 200, 1080, 1620))
        ##self.viewWater.setStyleSheet('QFrame { background-color: #000;}')

        ## Create item
        self.water1 = QtWidgets.QLabel("Sting", self.viewWater)
        self.water1.setGeometry(QtCore.QRect(60, 60, 450, 450))
        self.water1.setAlignment(QtCore.Qt.AlignCenter)
        self.water1.setFont(utils.font_17)
        self.water1.setStyleSheet('QLabel {border: 0px solid white; border-radius: 0px; background-color: #33313b; color: white; font-weight: bold;}')

        self.water2 = QtWidgets.QLabel("Revine", self.viewWater)
        self.water2.setGeometry(QtCore.QRect(570, 60, 450, 450))
        self.water2.setAlignment(QtCore.Qt.AlignCenter)
        self.water2.setFont(utils.font_17)
        self.water2.setStyleSheet('QLabel {border: 0px solid white; border-radius: 0px; background-color: #33313b; color: white; font-weight: bold;}')

        self.water3 = QtWidgets.QLabel("Number One", self.viewWater)
        self.water3.setGeometry(QtCore.QRect(60, 570, 450, 450))
        self.water3.setAlignment(QtCore.Qt.AlignCenter)
        self.water3.setFont(utils.font_17)
        self.water3.setStyleSheet('QLabel {border: 0px solid white; border-radius: 0px; background-color: #33313b; color: white; font-weight: bold;}')

        self.water4 = QtWidgets.QLabel("Aquafina", self.viewWater)
        self.water4.setGeometry(QtCore.QRect(570, 570, 450, 450))
        self.water4.setAlignment(QtCore.Qt.AlignCenter)
        self.water4.setFont(utils.font_17)
        self.water4.setStyleSheet('QLabel {border: 0px solid white; border-radius: 0px; background-color: #33313b; color: white; font-weight: bold;}')

    def initViewFood(self):
        ## Create view Water
        self.viewFood = QFrame(self)
        ##self.viewFood.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.viewFood.setGeometry(QtCore.QRect(0, 200, 1080, 1620))
        #self.viewFood.setStyleSheet('QFrame { background-color: #3e3e3e;}')

        ## Create item
        self.food1 = QtWidgets.QLabel("Donuts", self.viewFood)
        self.food1.setGeometry(QtCore.QRect(60, 60, 450, 450))
        self.food1.setAlignment(QtCore.Qt.AlignCenter)
        self.food1.setFont(utils.font_17)
        self.food1.setStyleSheet('QLabel {border: 0px solid white; border-radius: 0px; background-color: #f6f5f5; color: black; font-weight: bold;}')

        self.food2 = QtWidgets.QLabel("Sandwich", self.viewFood)
        self.food2.setGeometry(QtCore.QRect(570, 60, 450, 450))
        self.food2.setAlignment(QtCore.Qt.AlignCenter)
        self.food2.setFont(utils.font_17)
        self.food2.setStyleSheet('QLabel {border: 0px solid white; border-radius: 0px; background-color: #f6f5f5; color: black; font-weight: bold;}')

        self.food3 = QtWidgets.QLabel("Cheeseburger", self.viewFood)
        self.food3.setGeometry(QtCore.QRect(60, 570, 450, 450))
        self.food3.setAlignment(QtCore.Qt.AlignCenter)
        self.food3.setFont(utils.font_17)
        self.food3.setStyleSheet('QLabel {border: 0px solid white; border-radius: 0px; background-color: #f6f5f5; color: black; font-weight: bold;}')

        self.food4 = QtWidgets.QLabel("Hamberger", self.viewFood)
        self.food4.setGeometry(QtCore.QRect(570, 570, 450, 450))
        self.food4.setAlignment(QtCore.Qt.AlignCenter)
        self.food4.setFont(utils.font_17)
        self.food4.setStyleSheet('QLabel {border: 0px solid white; border-radius: 0px; background-color: #f6f5f5; color: black; font-weight: bold;}')

    def onClickWater(self):
        ##self.aniRightToLeft()
        self.wgWater.setStyleSheet('QLabel { background-color: #145374;}')
        self.btWater.setStyleSheet('QPushButton {border: 0px solid gray; background-color: #145374; color: white; font-weight: bold}')
        self.wgFood.setStyleSheet('QLabel { background-color: #fff;}')
        self.btFood.setStyleSheet('QPushButton {border: 0px solid gray; background-color: #145374; color: gray;}')

        self.viewWater.show()
        self.viewFood.hide()

    def onClickFood(self):
        ##self.aniLeftToRight()
        self.wgFood.setStyleSheet('QLabel { background-color: #145374;}')
        self.btFood.setStyleSheet('QPushButton {border: 0px solid gray; background-color: #145374; color: white; font-weight: bold}')
        self.wgWater.setStyleSheet('QLabel { background-color: #fff;}')
        self.btWater.setStyleSheet('QPushButton {border: 0px solid gray; background-color: #145374; color: gray;}')

        self.viewFood.show()
        self.viewWater.hide()

    def aniRightToLeft(self):
        self.aniRight = QtCore.QPropertyAnimation(self.viewWater, b"geometry")
        self.aniRight.setDuration(200)
        self.aniRight.setStartValue(QtCore.QRect(-50, 140, 520, 810))
        self.aniRight.setEndValue(QtCore.QRect(10, 140, 520, 810))
        self.aniRight.start()

    def aniLeftToRight(self):
        self.aniLeft = QtCore.QPropertyAnimation(self.viewFood, b"geometry")
        self.aniLeft.setDuration(200)
        self.aniLeft.setStartValue(QtCore.QRect(70, 140, 520, 810))
        self.aniLeft.setEndValue(QtCore.QRect(10, 140, 520, 810))
        self.aniLeft.start()



