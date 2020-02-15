import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
sys.path.append('..')
from Gui.ForgotPassword import forgotpassword
from verification import verifyClass


class forgotClass(QtWidgets.QMainWindow, forgotpassword.Ui_MainWindow):
    def __init__(self, parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_reset.clicked.connect(self.reset)
        self.btn_forgot.clicked.connect(self.logging)
        self.show()

    def reset(self):
        print('eyoooo')
        self.verifyForm = verifyClass(parent=self)
        self.verifyForm.show()
        self.hide()

    def logging(self):
        print('yoyoyoyoyo')
        self.close()
        self.returnToHome()
    
    def returnToHome(self):
        self.parent.showself()