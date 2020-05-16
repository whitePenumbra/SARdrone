import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.ForgotPassword import Verification
from ResetPassword import resetPassClass

class verifyClass(QtWidgets.QMainWindow, Verification.Ui_MainWindow):
    def __init__(self, parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.code = self.parent.code
        self.email = self.parent.txt_email.text()
        
        self.btn_forgot.clicked.connect(self.returnToHome)
        self.btn_verify.clicked.connect(self.verify)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.verify()
    
    def returnToHome(self):
        self.close()
        self.parent.returnToHome()

    def verify(self):
        if (self.txt_verCode.text() == self.code):
            self.lbl_error.setText("")

            self.resetpassword = resetPassClass(parent=self)
            self.resetpassword.show()
            self.close()
        else:
            self.lbl_error.setStyleSheet("QLabel {\ncolor: red; padding-left: 4px}")
            self.lbl_error.setText("Incorrect Code. The code is case sensitive.")
