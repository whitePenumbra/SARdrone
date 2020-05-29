import sys, re
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.ForgotPassword import resetpassword
from ConnectToDB import connectToDB
from Encryption import AESCipher

class resetPassClass(QtWidgets.QMainWindow, resetpassword.Ui_MainWindow):
    def __init__(self, parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.email = self.parent.email

        self.txtNewPass.editingFinished.connect(self.checkpass)
        self.txtConfirmPass.editingFinished.connect(self.checkpass)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.updatePassword()

    def checkpass(self):
        if (self.txtNewPass.text() != self.txtConfirmPass.text()):
            self.txtNewPass.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
            self.txtConfirmPass.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px;}")

            self.lbl_error.setStyleSheet("QLabel {\ncolor: red; padding-left: 4px}")
            self.lbl_error.setText("Password does not match.")
        else:
            self.txtNewPass.setStyleSheet("padding-left: 4px;")
            self.txtConfirmPass.setStyleSheet("padding-left: 4px;")

            self.lbl_error.setText("")

    def updatePassword(self):
        conn = connectToDB()
        cur = conn.cursor()

        self.newPass = self.txtNewPass.text()
        if (self.validatePassword()):
            encpass = AESCipher('aids').encrypt(self.newPass)

            query = "UPDATE users SET password = %s WHERE email = %s"
            values = (encpass, self.email)

            cur.execute(query,values)
            conn.commit()

            self.parent.returnToHome()

    def validatePassword(self):
        password = self.txtNewPass.text()

        if len(password) < 8:
            self.lbl_error.setStyleSheet("QLabel {\ncolor: red; padding-left: 4px}")
            self.lbl_error.setText("Make sure your password is at lest 8 letters")
            return(False)
        elif re.search('[0-9]',password) is None:
            self.lbl_error.setStyleSheet("QLabel {\ncolor: red; padding-left: 4px}")
            self.lbl_error.setText("Make sure your password has a number in it")
            return(False)
        elif re.search('[A-Z]',password) is None: 
            self.lbl_error.setStyleSheet("QLabel {\ncolor: red; padding-left: 4px}")
            self.lbl_error.setText("Make sure your password has a capital letter in it")
            return(False)
        elif (' ' in password):
            self.lbl_error.setStyleSheet("QLabel {\ncolor: red; padding-left: 4px}")
            self.lbl_error.setText("Make sure your password doesn't have a space in it")
            return(False)
        else:
            return(True)