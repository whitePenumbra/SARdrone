# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OfflineForgotPassword.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
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
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 60, 341, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_forgot = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(26)
        self.lbl_forgot.setFont(font)
        self.lbl_forgot.setStyleSheet("")
        self.lbl_forgot.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_forgot.setObjectName("lbl_forgot")
        self.verticalLayout_2.addWidget(self.lbl_forgot)
        self.lbl_sub1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_sub1.setFont(font)
        self.lbl_sub1.setStyleSheet("")
        self.lbl_sub1.setObjectName("lbl_sub1")
        self.verticalLayout_2.addWidget(self.lbl_sub1)
        self.lbl_sub2_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_sub2_3.setFont(font)
        self.lbl_sub2_3.setStyleSheet("")
        self.lbl_sub2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sub2_3.setObjectName("lbl_sub2_3")
        self.verticalLayout_2.addWidget(self.lbl_sub2_3)
        self.lbl_sub2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sub2.setGeometry(QtCore.QRect(90, 170, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl_sub2.setFont(font)
        self.lbl_sub2.setStyleSheet("")
        self.lbl_sub2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sub2.setObjectName("lbl_sub2")
        self.lbl_sub2_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sub2_2.setGeometry(QtCore.QRect(110, 250, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl_sub2_2.setFont(font)
        self.lbl_sub2_2.setStyleSheet("")
        self.lbl_sub2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sub2_2.setObjectName("lbl_sub2_2")
        self.lbl_adminEmail = QtWidgets.QLabel(self.centralwidget)
        self.lbl_adminEmail.setGeometry(QtCore.QRect(130, 210, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl_adminEmail.setFont(font)
        self.lbl_adminEmail.setStyleSheet("")
        self.lbl_adminEmail.setText("")
        self.lbl_adminEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_adminEmail.setObjectName("lbl_adminEmail")
        self.lbl_adminPhone = QtWidgets.QLabel(self.centralwidget)
        self.lbl_adminPhone.setGeometry(QtCore.QRect(390, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl_adminPhone.setFont(font)
        self.lbl_adminPhone.setStyleSheet("")
        self.lbl_adminPhone.setText("")
        self.lbl_adminPhone.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_adminPhone.setObjectName("lbl_adminPhone")
        self.lbl_devPhone = QtWidgets.QLabel(self.centralwidget)
        self.lbl_devPhone.setGeometry(QtCore.QRect(390, 290, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl_devPhone.setFont(font)
        self.lbl_devPhone.setStyleSheet("")
        self.lbl_devPhone.setText("")
        self.lbl_devPhone.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_devPhone.setObjectName("lbl_devPhone")
        self.lbl_devEmail = QtWidgets.QLabel(self.centralwidget)
        self.lbl_devEmail.setGeometry(QtCore.QRect(130, 290, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl_devEmail.setFont(font)
        self.lbl_devEmail.setStyleSheet("")
        self.lbl_devEmail.setText("")
        self.lbl_devEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_devEmail.setObjectName("lbl_devEmail")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(250, 340, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton {\n"
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
        self.btn_login.setObjectName("btn_login")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIDS – Forgot Password (Offline)"))
        self.lbl_forgot.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">Forgot password?</span></p></body></html>"))
        self.lbl_sub1.setText(_translate("MainWindow", "You are not connected to the internet. This computer\'s internet"))
        self.lbl_sub2_3.setText(_translate("MainWindow", "connection appears to be offline"))
        self.lbl_sub2.setText(_translate("MainWindow", "If you\'re a Pilot, contact your administrator :"))
        self.lbl_sub2_2.setText(_translate("MainWindow", "If you\'re an administrator, contact the developers :"))
        self.btn_login.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
