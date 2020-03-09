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
        # print(user + " " + password)

        cur.execute('SELECT username,password,user_type FROM users WHERE username = "%s"' % (user))
        result = cur.fetchall()

        # print(result)

        dbuser = result[0][0]
        dbuserType = result[0][2]
        dbpass = result[0][1]
        strpass = (AESCipher('aids').decrypt(dbpass[2:(len(dbpass)-1)])).decode()

        if (dbuserType == 0 and password == strpass):
            print('YEHEEEEEY')
            self.homepage = homepageClass(parent=self)
            self.close()
            self.homepage.show()
        else:
            print('NOT TODAY BOIII')

        # if user == 'admin' and password == 'admin':
        #     print('Cheheck')
        #     self.homepage = homepageClass(parent=self)
        #     self.close()
        #     self.homepage.show()

    def forgot(self):
        print('testttttt')
        self.forgotform = forgotClass(parent=self)
        self.forgotform.show()
        self.hide()


    def showself(self):
        self.show()