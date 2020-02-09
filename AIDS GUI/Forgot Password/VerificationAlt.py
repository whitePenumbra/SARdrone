# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VerificationAlt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_verification = QtWidgets.QLabel(self.centralwidget)
        self.lbl_verification.setGeometry(QtCore.QRect(240, 110, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(19)
        self.lbl_verification.setFont(font)
        self.lbl_verification.setStyleSheet("padding-left:2px;\n"
"padding-bottom: 4px;")
        self.lbl_verification.setObjectName("lbl_verification")
        self.lbl_sub1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sub1.setGeometry(QtCore.QRect(140, 157, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_sub1.setFont(font)
        self.lbl_sub1.setStyleSheet("padding-left:4px;\n"
"padding-bottom:10px;")
        self.lbl_sub1.setObjectName("lbl_sub1")
        self.lbl_error = QtWidgets.QLabel(self.centralwidget)
        self.lbl_error.setGeometry(QtCore.QRect(150, 180, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.lbl_error.setFont(font)
        self.lbl_error.setStyleSheet("padding-bottom:3 rem;")
        self.lbl_error.setText("")
        self.lbl_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_error.setObjectName("lbl_error")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 320, 521, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.app_logo = QtWidgets.QLabel(self.centralwidget)
        self.app_logo.setGeometry(QtCore.QRect(70, 20, 135, 114))
        self.app_logo.setText("")
        self.app_logo.setPixmap(QtGui.QPixmap("../Resources/aids_logo.png"))
        self.app_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.app_logo.setObjectName("app_logo")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 40, 293, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.aids_logo = QtWidgets.QLabel(self.layoutWidget)
        self.aids_logo.setMinimumSize(QtCore.QSize(291, 43))
        self.aids_logo.setMaximumSize(QtCore.QSize(291, 43))
        font = QtGui.QFont()
        font.setFamily("Audiowide")
        font.setPointSize(28)
        font.setKerning(True)
        self.aids_logo.setFont(font)
        self.aids_logo.setObjectName("aids_logo")
        self.verticalLayout.addWidget(self.aids_logo)
        self.app_name = QtWidgets.QLabel(self.layoutWidget)
        self.app_name.setMinimumSize(QtCore.QSize(291, 20))
        self.app_name.setMaximumSize(QtCore.QSize(291, 20))
        font = QtGui.QFont()
        font.setFamily("Barlow Medium")
        font.setPointSize(12)
        font.setKerning(True)
        self.app_name.setFont(font)
        self.app_name.setObjectName("app_name")
        self.verticalLayout.addWidget(self.app_name)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(110, 350, 361, 33))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.remember_layout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.remember_layout.setContentsMargins(0, 0, 0, 0)
        self.remember_layout.setObjectName("remember_layout")
        self.lbl_remember = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_remember.setFont(font)
        self.lbl_remember.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_remember.setObjectName("lbl_remember")
        self.remember_layout.addWidget(self.lbl_remember)
        self.btn_forgot = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btn_forgot.setMinimumSize(QtCore.QSize(116, 31))
        self.btn_forgot.setMaximumSize(QtCore.QSize(116, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.btn_forgot.setFont(font)
        self.btn_forgot.setStyleSheet("QPushButton {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(201, 201, 201);\n"
"border: 1.2px solid #ABABAB;\n"
"outline: none;}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(171, 171, 171);\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(129, 129, 129);\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_forgot.setObjectName("btn_forgot")
        self.remember_layout.addWidget(self.btn_forgot)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 200, 323, 101))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verification_layout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verification_layout.setContentsMargins(0, 0, 0, 0)
        self.verification_layout.setObjectName("verification_layout")
        self.txt_verCode = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_verCode.setMinimumSize(QtCore.QSize(321, 31))
        self.txt_verCode.setMaximumSize(QtCore.QSize(321, 31))
        self.txt_verCode.setStyleSheet("padding-left: 4px;")
        self.txt_verCode.setObjectName("txt_verCode")
        self.verification_layout.addWidget(self.txt_verCode)
        self.btn_verify = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_verify.sizePolicy().hasHeightForWidth())
        self.btn_verify.setSizePolicy(sizePolicy)
        self.btn_verify.setMinimumSize(QtCore.QSize(321, 31))
        self.btn_verify.setMaximumSize(QtCore.QSize(321, 31))
        self.btn_verify.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 176, 6);\n"
"border: 1.2px solid #ff9d07;\n"
"outline: none;}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 157, 7);\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(254, 140, 8);\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_verify.setObjectName("btn_verify")
        self.verification_layout.addWidget(self.btn_verify)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_verCode, self.btn_verify)
        MainWindow.setTabOrder(self.btn_verify, self.btn_forgot)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIDS – Verification"))
        self.lbl_verification.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">Verification</span></p></body></html>"))
        self.lbl_sub1.setText(_translate("MainWindow", "Enter the verification code we just sent to your email address"))
        self.aids_logo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">AIDS</span></p></body></html>"))
        self.app_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">Air-based Inspection Deployment System</span></p></body></html>"))
        self.lbl_remember.setText(_translate("MainWindow", "Remembered your password?"))
        self.btn_forgot.setText(_translate("MainWindow", "Try logging in"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
