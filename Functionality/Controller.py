import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Login import loginClass
from Forgot import forgotClass
from AdminHomepage import homepageClass

class controllerClass():
    def __init__(self):
        pass

    def showForgot(self):
        self.forgot = forgotClass()
        self.forgot.show()
        self.parent.show()
    
    def showLogin(self):
        self.login = loginClass()
        self.login.show()



def main():
    app = QtWidgets.QApplication(sys.argv)
    form = loginClass()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()