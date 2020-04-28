import sys, os, cv2, datetime
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, 
                             QLabel, QVBoxLayout)
sys.path.append('..')
from Gui.Pilot.Homepage import Homepage
import MySQLdb as mdb
from Encryption import AESCipher
from Gui.NewUser import NewUserQDialog


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
        self.btn_endOps.setEnabled(False)
        self.btn_PDF.setEnabled(False)

        self.cap = None                                        #  -capture <-> +cap

        self.timer = QtCore.QTimer(self, interval=5)
        self.timer.timeout.connect(self.update_frame)
        self._image_counter = 0

        self.getPilot()
        print("Current User: ")
        print(self.currentUser)

        self.firstLogin()
        

    @QtCore.pyqtSlot()
    def start_webcam(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
        self.timer.start()

        self.btn_Launch.setEnabled(False)
        self.btn_endOps.setEnabled(True)

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
    
    def stop_webcam(self):
        self.timer.stop()
        self.cap.release()

        self.btn_Launch.setEnabled(True)
        self.btn_endOps.setEnabled(False)

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
        self.stop_webcam()

    def printPDF(self):
        print('Pilot PDF button')
    
    def getPilot(self):
        self.currentUser = self.parent.getUser()
        return(self.currentUser)

    def connectToDB(self):
        try:
            db = mdb.connect('localhost', 'root', '', 'aids')
            return (db)

        except mdb.Error as e:
            print('Connection failed!')
            sys.exit(1)

    # def getPilotInfo(self):
    #     conn = self.connectToDB()
    #     cur = conn.cursor()

    #     query = "SELECT * FROM users WHERE user_id = %s AND user_type = %s"
    #     values = (self.currentUser[0][0], self.currentUser[0][2])

    #     cur.execute(query,values)
    #     currentUserInfo = cur.fetchall()

    #     return (currentUserInfo)
    
    # def getPilotAddress(self, userInfo):
    #     if (not userInfo):
    #         cur.execute('SELECT * FROM address WHERE address_id = "%s"' % (userInfo[0][1],))
    #         currentUserAddress = cur.fetchall()

    #         return (currentUserAddress)

    def firstLogin(self):
        self.getPilot()

        conn = self.connectToDB()
        cur = conn.cursor()

        cur.execute("SELECT * FROM audit WHERE user_id = %s" % (self.currentUser[0][0],))
        result = cur.fetchall()

        print(len(result))

        if (len(result) == 0):
            self.changePassword = changePasswordClass(parent=self)
            self.changePassword.setModal(True)

    def audit(self, message):
        uid = self.currentUser[0][0]
        currentTime = datetime.datetime.now()

        query = "INSERT INTO audit(user_id, time, actions_made) VALUES (%s, %s, %s)"
        values = (str(uid), currentTime, str(message))

        conn = self.connectToDB()
        cur = conn.cursor()

        cur.execute(query,values)
        conn.commit()

class changePasswordClass(QtWidgets.QDialog, NewUserQDialog.Ui_Dialog):
    def __init__(self,parent):
        super(QtWidgets.QDialog,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        
        self.currentUser = self.parent.getPilot()
        print("THIS IS IN DIALOG")
        print(self.currentUser[0][0])

        self.btnReset.clicked.connect(self.resetPassword)
        self.txtConfirmPass.editingFinished.connect(self.checkSimilar)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.resetPassword()

    def checkSimilar(self):
        newPass = self.txtNewPass.text()
        retypePass = self.txtConfirmPass.text()

        font = QtGui.QFont()
        font.setPointSize(8)
        font.setFamily("Helvetica")

        if (newPass != retypePass):
            self.lbl_error.setStyleSheet("QLabel {\ncolor: red; padding-left: 4px}")
            self.lbl_error.setText('Password does not match')
            self.txtNewPass.setFont(font)
            self.txtNewPass.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
            self.txtConfirmPass.setFont(font)
            self.txtConfirmPass.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px;}")
        else:
            self.txtNewPass.setFont(font)
            self.txtNewPass.setStyleSheet("padding-left: 4px;")
            self.txtConfirmPass.setFont(font)
            self.txtConfirmPass.setStyleSheet("padding-left: 4px;")
            self.lbl_error.setText('')
    
    def resetPassword(self):
        conn = self.parent.connectToDB()
        cur = conn.cursor()

        user = self.parent.getPilot()
        print(user)

        if (self.txtNewPass.text() == self.txtConfirmPass.text()):
            password = AESCipher('aids').encrypt(self.txtNewPass.text())
            encpass = password.decode("utf-8")

            query = "UPDATE users SET password = %s WHERE user_id = %s"
            value = (encpass, user[0][0])

            cur.execute(query,value)
            conn.commit()

            self.parent.audit("Pilot " + str(user[0][0]) + " changed his password.")
        
        self.close()




