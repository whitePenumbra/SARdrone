import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Login import LoginAlt
from Gui.ForgotPassword import ForgotPasswordAlt
from Gui.Administator.Homepage import HomepageAlt
from Forgot import forgotClass
from Homepage import homepageClass



print("asd")
class loginClass(QtWidgets.QMainWindow, LoginAlt.Ui_MainWindow):
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
            self.homepage = homepageClass()
            self.hide()
            self.homepage.show()

    def forgot(self):
        print('testttttt')
        self.forgotForm = forgotClass()
        self.hide()
        self.forgotForm.show()
   
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = loginClass()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()