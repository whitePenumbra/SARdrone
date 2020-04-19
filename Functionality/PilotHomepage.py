import sys, os, cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, 
                             QLabel, QVBoxLayout)
sys.path.append('..')
from Gui.Pilot.Homepage import Homepage
import MySQLdb as mdb
from Encryption import AESCipher
from Gui.NewUser.NewUserQDialog import Ui_Dialog


class pilothomepageClass(QtWidgets.QMainWindow, Homepage.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.btn_profile.clicked.connect(self.view)
        self.btn_pastOps.clicked.connect(self.operations)
        self.btn_logout.clicked.connect(self.logout)
        self.btn_Launch.clicked.connect(self.start_webcam)
        self.btn_endOps.clicked.connect(self.endOperation)
        self.btn_PDF.clicked.connect(self.printPDF)

        self.droneStream.setScaledContents(True)

        self.cap = None                                        #  -capture <-> +cap

        self.timer = QtCore.QTimer(self, interval=5)
        self.timer.timeout.connect(self.update_frame)
        self._image_counter = 0

        self.getPilot()
        print("Current User: ")
        print(self.currentUser)
        

    @QtCore.pyqtSlot()
    def start_webcam(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
        self.timer.start()

    @QtCore.pyqtSlot()
    def update_frame(self):
        ret, image = self.cap.read()
        simage     = cv2.flip(image, 1)
        self.displayImage(image, True)

    @QtCore.pyqtSlot()
    def capture_image(self):
        flag, frame = self.cap.read()
        path = r'D:\_Qt\Test\testtest'                         # 
        if flag:
            QtWidgets.QApplication.beep()
            name = "my_image.jpg"
            cv2.imwrite(os.path.join(path, name), frame)
            self._image_counter += 1

    def displayImage(self, img, window=True):
        qformat = QtGui.QImage.Format_Indexed8
        if len(img.shape)==3 :
            if img.shape[2]==4:
                qformat = QtGui.QImage.Format_RGBA8888
            else:
                qformat = QtGui.QImage.Format_RGB888
        outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        if window:
            self.droneStream.setPixmap(QtGui.QPixmap.fromImage(outImage))

    def view(self):
        print('Pilot View button')
    
    def operations(self):
        print('Pilot Operations button')
    
    def logout(self):
        self.close()
        self.parent.showself()
    
    def launch(self):
        print('Pilot Launch button')

    def endOperation(self):
        print('Pilot End Operations button')

    def printPDF(self):
        print('Pilot PDF button')
    
    def getPilot(self):
        self.currentUser = self.parent.getUser()

    def connectToDB(self):
        try:
            db = mdb.connect('localhost', 'root', '', 'aids')
            return (db)

        except mdb.Error as e:
            print('Connection failed!')
            sys.exit(1)

    def getPilotInfo(self):
        conn = self.connectToDB()
        cur = conn.cursor()

        cur.execute('SELECT * FROM users WHERE username = "%s" AND user_type = "%s"' % (self.currentUser[0][0], self.currentUser[0][2]))
        currentUserInfo = cur.fetchall()

        return (currentUserInfo)
    
    def getPilotAddress(self, userInfo):
        if (not userInfo):
            cur.execute('SELECT * FROM address WHERE address_id = "%s"' % (userInfo[0][1],))
            currentUserAddress = cur.fetchall()

            return (currentUserAddress)