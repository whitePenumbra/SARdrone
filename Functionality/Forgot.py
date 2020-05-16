import sys, random, string, re, ssl, smtplib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
sys.path.append('..')
from Gui.ForgotPassword import forgotpassword
from verification import verifyClass
from Encryption import AESCipher
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class forgotClass(QtWidgets.QMainWindow, forgotpassword.Ui_MainWindow):
    def __init__(self, parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.btn_reset.clicked.connect(self.reset)
        self.btn_forgot.clicked.connect(self.logging)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.reset()
    
    def generateCode(self):
        generated = ''.join(random.choice(string.ascii_uppercase)for x in range(6))
        
        return (generated)

    def logging(self):
        print('yoyoyoyoyo')
        self.close()
        self.returnToHome()
    
    def returnToHome(self):
        self.parent.showself()

    def sendEmail(self):
        port = 465
        mypass = (AESCipher('my password').decrypt('oNp8RcyRuLep8XYQ1JOJl57azvNzmeIrQ9pEKp0cIHs=')).decode()
        context = ssl.create_default_context()
        Recipient = self.txt_email.text()

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
                server.login('airbaseddeploymentsystem@gmail.com', mypass)

                msg = MIMEMultipart('alternative')
                msg['Subject'] = 'Test Message'
                msg['To'] = self.txt_email.text()
                message = """
Code: %s
                """ % (self.code)
                msg.attach(MIMEText(message))

                server.sendmail('airbaseddeploymentsystem@gmail.com', Recipient, msg.as_string())
                server.quit()
                print('Email Sent!')
        except Exception as e:
            print(e)
        
    
    def reset(self):
        font = QtGui.QFont()
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        font.setPointSize(10)
        font.setFamily("Helvetica")

        if(re.search(regex, self.txt_email.text())):  
            self.txt_email.setFont(font)
            self.txt_email.setStyleSheet("padding-left: 4px;")
            print("Valid Email")

            self.code = self.generateCode()
            self.sendEmail()

            self.verifyForm = verifyClass(parent=self)
            self.verifyForm.show()
            self.close()       
        else:  
            print("Invalid Email")
            self.txt_email.setFont(font)
            self.txt_email.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px;}")