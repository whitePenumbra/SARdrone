import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.ForgotPassword import ForgotPasswordAlt


class forgotClass(QtWidgets.QMainWindow, ForgotPasswordAlt.Ui_MainWindow):
    def __init__(self, parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_reset.clicked.connect(self.reset)
        self.btn_forgot.clicked.connect(self.logging)
        self.show()

    def reset(self):
        print('eyoooo')

    def logging(self):
        print('yoyoyoyoyo')
        self.parent.showself()
        self.close()