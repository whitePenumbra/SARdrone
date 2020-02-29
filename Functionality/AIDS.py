import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from PyQt5.QtWidgets import QDialog
from Gui.Login import LoginAlt
from Gui.ForgotPassword.ForgotPasswordQDialog import Ui_Dialog
from Gui.Administrator.Homepage import HomepageAlt
from Forgot import forgotClass
from Homepage import homepageClass
from Encryption import AESCipher
import MySQLdb as mdb

print("asd")
class loginClass(QtWidgets.QMainWindow, LoginAlt.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btn_login.clicked.connect(self.login)
        self.btn_forgot.clicked.connect(self.forgot)

    def login(self):
        con = mdb.connect('localhost', 'root', '', 'aids')
        cur = con.cursor()

        user = self.txt_username.text()
        password = self.txt_password.text()
        print(user + " " + password)

        # cur.execute('SELECT username,password FROM users WHERE username = "%s" AND user_type = "%s"' % (user,0))
        # result = cur.fetchall()

        # print(len(result[0][1]))
        # print(result[0][1])
        # print(AESCipher('aids').decrypt(result[0][1]))

        # dbuser = result[0][0]
        # dbpass = AESCipher('aids').decrypt(result[0][1])

        if user == 'admin' and password == 'admin':
            print('Cheheck')
            self.homepage = homepageClass(parent=self)
            self.close()
            self.homepage.show()

    def forgot(self):
        print('testttttt')
        self.forgotform = forgotClass(parent=self)
        self.forgotform.show()
        self.hide()


    def showself(self):
        self.show()