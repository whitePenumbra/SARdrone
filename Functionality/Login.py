import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Login import LoginAlt
from Gui.ForgotPassword import ForgotPasswordAlt
from Gui.Administator.Homepage import HomepageAlt

print("asd")
class mainClass(QtWidgets.QMainWindow, LoginAlt.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btn_login.clicked.connect(self.login)
        self.btn_forgot.clicked.connect(self.forgot)

    def login(self):
        user = self.txt_username.text()
        password = self.txt_password.text()
        print(user + " " + password)

        if user == 'admin' and password == 'admin':
            print('Cheheck')
            self.window = QtWidgets.QMainWindow()
            self.ui = HomepageAlt.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()

    def forgot(self):
        print('testttttt')
        self.window = QtWidgets.QMainWindow()
        self.ui = ForgotPasswordAlt.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.hide()

class forgotClass(QtWidgets.QMainWindow, ForgotPasswordAlt.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btn_reset.clicked.connect(self.reset)

    def reset(self):
        print('eyoooo')

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = mainClass()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()