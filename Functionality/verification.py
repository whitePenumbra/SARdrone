import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.ForgotPassword import Verification

class verifyClass(QtWidgets.QMainWindow, Verification.Ui_MainWindow):
    def __init__(self, parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        
        self.btn_forgot.clicked.connect(self.returnToHome)
        self.btn_verify.clicked.connect(self.verify)
    
    def returnToHome(self):
        self.close()
        self.parent.returnToHome()

    def verify(self):
        print('verify')