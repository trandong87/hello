import utils
from PyQt5 import QtWidgets, QtCore

## Create Ui of Appointment Confirmation
class UIAppointmentConfirmation(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UIAppointmentConfirmation, self).__init__(parent)

        ## Create Navigation Bar
        utils.initNavigationBar("Appoitment Confirmation", self)

        ## Create Back's QPushButton
        utils.initBackQPushButton(self)

        ## Create background
        self.wgBackground = QtWidgets.QWidget(self)
        self.wgBackground.setGeometry(QtCore.QRect(120, 280, 840, 840)) #120, 280, 840, 840))
        self.wgBackground.setStyleSheet("background-color: gray");

        ## Create QR's view
        self.lbQr = QtWidgets.QLabel("", self)
        self.lbQr.setGeometry(QtCore.QRect(300, 460, 480, 480))
        self.lbQr.setStyleSheet('QLabel {border: 4px solid white; border-style: dashed; border-radius: 0px; background-color: gray;}')

        ## Create Confirm's Button
        self.btConfirm = QtWidgets.QPushButton("Check QR",self)
        self.btConfirm.setGeometry(QtCore.QRect(240, 1200, 600, 80))
        self.btConfirm.setStyleSheet('QPushButton {border: 0px solid gray; background-color: #33313b; color: white; font-weight: bold}')
        self.btConfirm.setFont(utils.font_28)
