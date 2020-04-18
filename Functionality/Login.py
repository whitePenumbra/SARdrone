import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from PyQt5.QtWidgets import QDialog
from Gui.Login import LoginAlt
from Gui.ForgotPassword.ForgotPasswordQDialog import Ui_Dialog
from Gui.Administrator.Homepage import HomepageAlt
from Forgot import forgotClass
from AdminHomepage import adminhomepageClass
from PilotHomepage import pilothomepageClass
from Encryption import AESCipher
import MySQLdb as mdb

print("asd")
class loginClass(QtWidgets.QMainWindow, LoginAlt.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btn_login.clicked.connect(self.login)
        self.btn_forgot.clicked.connect(self.forgot)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.login()

    def login(self):
        conn = self.connectToDB()
        cur = conn.cursor()

        user = self.txt_username.text()
        password = self.txt_password.text()
        # print(user + " " + password)

        cur.execute('SELECT username,password,user_type FROM users WHERE username = "%s"' % (user))
        self.result = cur.fetchall()

        # print(result)

        if (not self.result):
            print('NOT TODAY BOIII')
            self.lbl_response.setStyleSheet("QLabel {\ncolor: red}")
            self.lbl_response.setText('Invalid username/password')
            self.txt_username.setStyleSheet("QLineEdit {\nborder: 1.2px solid red }")
            self.txt_password.setStyleSheet("QLineEdit {\nborder: 1.2px solid red }")
        else:
            dbuser = self.result[0][0]
            dbuserType = self.result[0][2]
            dbpass = self.result[0][1]
            strpass = (AESCipher('aids').decrypt(dbpass)).decode()
            if (dbuserType == 0 and password == strpass):
                print('YEHEEEEEY')
                self.homepage = adminhomepageClass(parent=self)
                self.close()
                self.homepage.show()
            elif (dbuserType == 1 and password == strpass):
                print('Pilot logging in')
                self.homepage = pilothomepageClass(parent=self)
                self.close()
                self.homepage.show()

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
        self.txt_username.clear()
        self.txt_password.clear()
        self.show()

    def getUser(self):
        self.currentUser = self.result
        print('GET USER!!!')
        print(self.currentUser)
        return (self.currentUser)
    
    def connectToDB(self):
        try:
            db = mdb.connect('localhost', 'root', '', 'aids')
            return (db)

        except mdb.Error as e:
            print('Connection failed!')
            sys.exit(1)