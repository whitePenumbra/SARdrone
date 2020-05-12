# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resetpassword.ui'
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
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(130, 330, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.btn_reset.setFont(font)
        self.btn_reset.setStyleSheet("QPushButton {\n"
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
        self.btn_reset.setObjectName("btnReset")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 50, 351, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_verification_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(26)
        self.lbl_verification_2.setFont(font)
        self.lbl_verification_2.setStyleSheet("")
        self.lbl_verification_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_verification_2.setObjectName("lbl_verification_2")
        self.verticalLayout_2.addWidget(self.lbl_verification_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 164, 353, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl_error = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.lbl_error.setFont(font)
        self.lbl_error.setStyleSheet("")
        self.lbl_error.setText("")
        self.lbl_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_error.setObjectName("lbl_error")
        self.verticalLayout_6.addWidget(self.lbl_error)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_newpass = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl_newpass.setFont(font)
        self.lbl_newpass.setStyleSheet("")
        self.lbl_newpass.setObjectName("lbl_newpass")
        self.verticalLayout_3.addWidget(self.lbl_newpass)
        self.txtNewPass = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txtNewPass.setMinimumSize(QtCore.QSize(347, 31))
        self.txtNewPass.setMaximumSize(QtCore.QSize(347, 31))
        self.txtNewPass.setStyleSheet("padding-left:4px;")
        self.txtNewPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtNewPass.setObjectName("txtNewPass")
        self.verticalLayout_3.addWidget(self.txtNewPass)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_confirmPass = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl_confirmPass.setFont(font)
        self.lbl_confirmPass.setStyleSheet("")
        self.lbl_confirmPass.setObjectName("lbl_confirmPass")
        self.verticalLayout_4.addWidget(self.lbl_confirmPass)
        self.txtConfirmPass = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txtConfirmPass.setMinimumSize(QtCore.QSize(247, 31))
        self.txtConfirmPass.setMaximumSize(QtCore.QSize(347, 31))
        self.txtConfirmPass.setStyleSheet("padding-left:4px;")
        self.txtConfirmPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtConfirmPass.setObjectName("txtConfirmPass")
        self.verticalLayout_4.addWidget(self.txtConfirmPass)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtConfirmPass, self.btn_reset)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIDS – Reset Password"))
        self.btn_reset.setText(_translate("MainWindow", "Reset Password"))
        self.lbl_verification_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">Reset Password</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Password must have at least 8 characters, an upper case (A-Z),"))
        self.label_2.setText(_translate("MainWindow", "and a number (0-9). Special Characters are optional"))
        self.lbl_newpass.setText(_translate("MainWindow", "New Password"))
        self.lbl_confirmPass.setText(_translate("MainWindow", "Re-enter Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
