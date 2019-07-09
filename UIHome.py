import cv2
import sys, utils
import paho.mqtt.client as mqtt
import UIIntroduction, UIMapsDirection, UIAppointmentConfirmation, UISupporting, UIServices
import time
import logging
import datetime
import threading
import numpy as np
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QFontDialog, QFrame
# initialize the log settings
logging.basicConfig(filename = 'app.log', level = logging.INFO)

## Creat instance for MQTT connection
broker_url = "10.20.44.169"
#broker_url = "69.51.177.91"
broker_port = 1883

## Variable store string got from Server to Display
w=0
scrollLen=0
scrollpointLeft=0
dataString=""
Gate=0
Number=0
previousGate=0
qImg=0
cap = cv2.VideoCapture("images/v1.divx")

## This is Home of User interface of project
class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)

        ## Create Navitation Bar
        ##utils.initNavigationBar("Home", self)

        ## Create Top/Bottom/Horizontal Image Label
        self.topImg = QLabel(self)
        self.topImg.setGeometry(QtCore.QRect(0, 0, 1366, 120))
        self.topImg.setStyleSheet('QLabel { background-color: white; background: url(\"images/ImgTopLeft.jpg\") center no-repeat;}')
        self.topLine = QLabel(self)
        self.topLine.setGeometry(QtCore.QRect(0, 121, 1920, 10))
        self.topLine.setStyleSheet('QLabel { background-color: orange; center no-repeat;}')

        self.bottomLine = QLabel(self)
        self.bottomLine.setGeometry(QtCore.QRect(0, 980, 1920, 110))
        self.bottomLine.setStyleSheet('QLabel { background-color: green; center no-repeat;}')

        self.horizoneLine = QLabel(self)
        self.horizoneLine.setGeometry(QtCore.QRect(700, 121, 10, 859))
        self.horizoneLine.setStyleSheet('QLabel { background-color: orange; center no-repeat;}')

        ## Create scroll text Right to Left at the bottom screen
        global scrollLen
        self.scrollText = QLabel(self)
        self.scrollText.setFont(utils.font_48)
        self.scrollText.setAlignment(QtCore.Qt.AlignLeft)
        self.scrollText.setText("Bệnh Viện Đa Khoa Hoàn Mỹ Kính Chào Quý Khách. Kính Chúc Quý Khách An Khang Thịnh Vượn.")
        scrollLen = len(self.scrollText.text())
        self.scrollText.setGeometry(QtCore.QRect(0, 990, scrollLen*40, 120))
        self.scrollText.setStyleSheet('QLabel { background-color: transparent; color : white; center no-repeat; font-weight: bold;}')

        ## Create Pixmap Frame
        self.videoZone = QLabel(self)
        self.videoZone.setGeometry(QtCore.QRect(720, 140, 1280, 720))
        self.videoZone.setStyleSheet('QLabel { background-color: black; center no-repeat;}')

        ## Create timer show one UI Window
        self.timerUI = QLabel(self)
        self.timerUI.setGeometry(QtCore.QRect(1180, 860, 450, 120))
        self.timerUI.setFont(utils.font_75)
        self.timerUI.setAlignment(QtCore.Qt.AlignLeft)
        self.timerUI.setStyleSheet('QLabel { background-color: transparent; color : green; center no-repeat; font-weight: bold;}')
        self.timerUI.setText(time.strftime("%H:%M"))
        #self.timerUI.setText(time.strftime("%m/%d/%Y %H:%M"))

        ## Create 7 Guest Couter Number -----------------------------------------------------------------------------------------
        self.numberOne = QLabel(self)
        self.numberOne.setGeometry(QtCore.QRect(20, 140, 450, 120))
        self.numberOne.setFont(utils.font_75)
        self.numberOne.setAlignment(QtCore.Qt.AlignLeft)
        self.numberOne.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberOne.setText("0001")

        self.numberTwo = QLabel(self)
        self.numberTwo.setGeometry(QtCore.QRect(20, 280, 450, 120))
        self.numberTwo.setFont(utils.font_75)
        self.numberTwo.setAlignment(QtCore.Qt.AlignLeft)
        self.numberTwo.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberTwo.setText("0002")

        self.numberThree = QLabel(self)
        self.numberThree.setGeometry(QtCore.QRect(20, 420, 450, 120))
        self.numberThree.setFont(utils.font_75)
        self.numberThree.setAlignment(QtCore.Qt.AlignLeft)
        self.numberThree.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberThree.setText("0003")

        self.numberFour = QLabel(self)
        self.numberFour.setGeometry(QtCore.QRect(20, 560, 450, 120))
        self.numberFour.setFont(utils.font_75)
        self.numberFour.setAlignment(QtCore.Qt.AlignLeft)
        self.numberFour.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberFour.setText("0004")

        self.numberFive = QLabel(self)
        self.numberFive.setGeometry(QtCore.QRect(20, 700, 450, 120))
        self.numberFive.setFont(utils.font_75)
        self.numberFive.setAlignment(QtCore.Qt.AlignLeft)
        self.numberFive.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberFive.setText("0005")

        self.numberSix = QLabel(self)
        self.numberSix.setGeometry(QtCore.QRect(20, 840, 450, 120))
        self.numberSix.setFont(utils.font_75)
        self.numberSix.setAlignment(QtCore.Qt.AlignLeft)
        self.numberSix.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberSix.setText("0006")

        ## Create 7 Gate Number -------------------------------------------------------------------------------------------------
        self.numberGate1 = QLabel(self)
        self.numberGate1.setGeometry(QtCore.QRect(530, 140, 200, 120))
        self.numberGate1.setFont(utils.font_75)
        self.numberGate1.setAlignment(QtCore.Qt.AlignLeft)
        self.numberGate1.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberGate1.setText("1")

        self.numberGate2 = QLabel(self)
        self.numberGate2.setGeometry(QtCore.QRect(530, 280, 200, 120))
        self.numberGate2.setFont(utils.font_75)
        self.numberGate2.setAlignment(QtCore.Qt.AlignLeft)
        self.numberGate2.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberGate2.setText("2")

        self.numberGate3 = QLabel(self)
        self.numberGate3.setGeometry(QtCore.QRect(530, 420, 200, 120))
        self.numberGate3.setFont(utils.font_75)
        self.numberGate3.setAlignment(QtCore.Qt.AlignLeft)
        self.numberGate3.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberGate3.setText("3")

        self.numberGate4 = QLabel(self)
        self.numberGate4.setGeometry(QtCore.QRect(530, 560, 200, 120))
        self.numberGate4.setFont(utils.font_75)
        self.numberGate4.setAlignment(QtCore.Qt.AlignLeft)
        self.numberGate4.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberGate4.setText("4")

        self.numberGate5 = QLabel(self)
        self.numberGate5.setGeometry(QtCore.QRect(530, 700, 200, 120))
        self.numberGate5.setFont(utils.font_75)
        self.numberGate5.setAlignment(QtCore.Qt.AlignLeft)
        self.numberGate5.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberGate5.setText("5")

        self.numberGate6 = QLabel(self)
        self.numberGate6.setGeometry(QtCore.QRect(530, 840, 200, 120))
        self.numberGate6.setFont(utils.font_75)
        self.numberGate6.setAlignment(QtCore.Qt.AlignLeft)
        self.numberGate6.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        self.numberGate6.setText("6")

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowIcon(QtGui.QIcon("icons/icon.png"))
        self.setStyleSheet('QWidget { background-color: white;}')
        self.startUIWindow()

    def startUIWindow(self):
        self.Window = UIWindow(self)
        self.setWindowTitle("Py.QMS Display 3.0")
        self.setCentralWidget(self.Window)
        #self.Window.introduce.clicked.connect(self.on_click)
        self.showFullScreen()

    def showIntroduction(self):
        self.intro = UIIntroduction.UIIntroduction(self)
        self.setCentralWidget(self.intro)
        self.intro.back.clicked.connect(self.startUIWindow)
        self.show()

    def on_click(self):
        print('Click')

    def setQlbelText(self, Gate, Number):
        if(Gate==1):    self.Window.numberOne.setText(Number)
        elif(Gate==2):  self.Window.numberTwo.setText(Number)
        elif(Gate==3):  self.Window.numberThree.setText(Number)
        elif(Gate==4):  self.Window.numberFour.setText(Number)
        elif(Gate==5):  self.Window.numberFive.setText(Number)
        elif(Gate==6):  self.Window.numberSix.setText(Number)

    def setQlbelColor(self, Gate):
        if(Gate==1):    self.Window.numberOne.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}'), self.Window.numberGate1.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}')
        elif(Gate==2):  self.Window.numberTwo.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}'), self.Window.numberGate2.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}')
        elif(Gate==3):  self.Window.numberThree.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}'), self.Window.numberGate3.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}')
        elif(Gate==4):  self.Window.numberFour.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}'), self.Window.numberGate4.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}')
        elif(Gate==5):  self.Window.numberFive.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}'), self.Window.numberGate5.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}')
        elif(Gate==6):  self.Window.numberSix.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}'), self.Window.numberGate6.setStyleSheet('QLabel { background-color: transparent; color : red; center no-repeat; font-weight: bold;}')

    def setQlbelPreviousColor(self):
        global previousGate
        if(previousGate==1):    self.Window.numberOne.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}'), self.Window.numberGate1.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        elif(previousGate==2):  self.Window.numberTwo.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}'), self.Window.numberGate2.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        elif(previousGate==3):  self.Window.numberThree.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}'), self.Window.numberGate3.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        elif(previousGate==4):  self.Window.numberFour.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}'), self.Window.numberGate4.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        elif(previousGate==5):  self.Window.numberFive.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}'), self.Window.numberGate5.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')
        elif(previousGate==6):  self.Window.numberSix.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}'), self.Window.numberGate6.setStyleSheet('QLabel { background-color: transparent; color : blue; center no-repeat; font-weight: bold;}')

    def showVideo(self):
        global qImg, scrollLen, scrollpointLeft
        self.Window.videoZone.setPixmap(QPixmap.fromImage(qImg))
        self.Window.timerUI.setText(time.strftime("%H:%M"))
        """
        ## Scroll Text String
        if(scrollpointLeft<-scrollLen*40):
            self.Window.scrollText.setGeometry(QtCore.QRect(0, 990, scrollLen*40, 120))
        else:
            scrollpointLeft = scrollpointLeft - 10
            self.Window.scrollText.setGeometry(QtCore.QRect(scrollpointLeft, 990, scrollLen*40, 120))
        """
        qImg=0

## Level 1 function
def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " (rc))

def on_message_from_server_to_display(client, userdata, message):
    try:
        global dataString
        dataString = message.payload.decode()
        print("Message Recieved from Server: "+dataString)
        dataProcess(dataString)
        dataString=""
    except:
        logging.info("Function [on_message_from_server_to_display] has issue at: %s", str(datetime.datetime.now()))

def on_message_from_server_to_keypad(client, userdata, message):
    print("Message Recieved from Server: "+message.payload.decode())

def on_message(client, userdata, message):
    print("Message Recieved from Others: "+message.payload.decode())

def myMqttInit():
    client = mqtt.Client()
    client.on_connect = on_connect
    #To Process Every Other Message
    client.on_message = on_message
    client.connect(broker_url, broker_port)
    client.loop_start()
    client.subscribe("QMS/Display", qos=1)
    while True:
        try:
            client.message_callback_add("QMS/Display", on_message_from_server_to_display)
            time.sleep(0.5) # wait
        except IOError as e:
            logging.info("Function [myMqttInit] has issue at: %s", str(datetime.datetime.now()))
            logging.exception(str(e))

def autoRun():
    global qImg, w, cap
    ret=1
    while (cap.isOpened()):
        try:
            ret, frame = cap.read()
            if(ret):
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                ##frame = cv2.flip(frame, 1)
                qImg = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
                ##qImg = qimage2ndarray.array2qimage(frame)  #SOLUTION FOR MEMORY LEAK
                ##cv2.imshow('frame',frame)
                w.showVideo()
                time.sleep(0.05) # wait
            else:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        except IOError as e:
            logging.info("Function [autoRun] has issue at: %s", str(datetime.datetime.now()))
            logging.exception(str(e))

def dataProcess(dataInput):
    ## String Sample: $D01011002#  Floor (Zone) 1, Gate 1, Number 1002
    global  w, Gate, Number, previousGate
    previousGate = Gate
    a = dataInput.find("$D")
    if(a>=0):
        Gate = int(dataInput[a+4:a+4+2])
        Number = dataInput[a+6:a+6+4]
        w.setQlbelText(Gate, Number)
        changeColor(Gate)

def changeColor(Gate):
    w.setQlbelPreviousColor()
    w.setQlbelColor(Gate)

## Define main function
def main():
    global  w
    app = QApplication(sys.argv)
    w = MainWindow()
    d = threading.Thread(name='myMqttInit', target=myMqttInit)
    d.setDaemon(True)
    c = threading.Thread(name='autoRun', target=autoRun)
    c.setDaemon(True)
    ## Killing Python thread by setting it as daemon
    #d.daemon = True
    #c.daemon = True
    d.start()
    c.start()
    time.sleep(0.1)
    sys.exit(app.exec_())

if __name__ == '__main__':
    logging.info("App start at: %s", str(datetime.datetime.now()))
    main()
