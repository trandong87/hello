from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton

## Define MQTT variable     -----------------------------------------------------------------------
#broker_url = "10.20.44.169"     #At School
broker_url = "69.51.177.91"    #At Dom
broker_port = 1883

## Define Global Variable   -----------------------------------------------------------------------
scrollText = "Bệnh Viện Đa Khoa Hoàn Mỹ Kính Chào Quý Khách. Kính Chúc Quý Khách An Khang Thịnh Vượn."
qmsNumberList = []

## Define font size         -----------------------------------------------------------------------
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
