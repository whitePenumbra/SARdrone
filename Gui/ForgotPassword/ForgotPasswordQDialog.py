# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ForgotPasswordQDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        Dialog.setMinimumSize(QtCore.QSize(600, 400))
        Dialog.setMaximumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        #removes ? from title bar
        Dialog.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 170, 335, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.form_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setObjectName("form_layout")
        self.email_layout = QtWidgets.QVBoxLayout()
        self.email_layout.setObjectName("email_layout")
        self.lbl_error = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.lbl_error.setFont(font)
        self.lbl_error.setStyleSheet("")
        self.lbl_error.setText("")
        self.lbl_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_error.setObjectName("lbl_error")
        self.email_layout.addWidget(self.lbl_error)
        self.lbl_email = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_email.setFont(font)
        self.lbl_email.setStyleSheet("")
        self.lbl_email.setObjectName("lbl_email")
        self.email_layout.addWidget(self.lbl_email)
        self.txt_email = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_email.setMinimumSize(QtCore.QSize(331, 31))
        self.txt_email.setMaximumSize(QtCore.QSize(331, 31))
        self.txt_email.setStyleSheet("padding-left:4px;")
        self.txt_email.setObjectName("txt_email")
        self.email_layout.addWidget(self.txt_email)
        self.form_layout.addLayout(self.email_layout)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(40, 305, 521, 41))
        self.line.setStyleSheet("margin-top:4px;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(140, 50, 334, 111))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.title_layout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout.setObjectName("title_layout")
        self.lbl_forgot = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(26)
        self.lbl_forgot.setFont(font)
        self.lbl_forgot.setStyleSheet("")
        self.lbl_forgot.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_forgot.setObjectName("lbl_forgot")
        self.title_layout.addWidget(self.lbl_forgot)
        self.subtitle_layout = QtWidgets.QVBoxLayout()
        self.subtitle_layout.setObjectName("subtitle_layout")
        self.lbl_sub1 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_sub1.setFont(font)
        self.lbl_sub1.setStyleSheet("")
        self.lbl_sub1.setObjectName("lbl_sub1")
        self.subtitle_layout.addWidget(self.lbl_sub1)
        self.lbl_sub2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_sub2.setFont(font)
        self.lbl_sub2.setStyleSheet("")
        self.lbl_sub2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sub2.setObjectName("lbl_sub2")
        self.subtitle_layout.addWidget(self.lbl_sub2)
        self.title_layout.addLayout(self.subtitle_layout)
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(100, 350, 371, 33))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.remember_layout = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.remember_layout.setContentsMargins(0, 0, 0, 0)
        self.remember_layout.setObjectName("remember_layout")
        self.lbl_remember = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_remember.setFont(font)
        self.lbl_remember.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_remember.setObjectName("lbl_remember")
        self.remember_layout.addWidget(self.lbl_remember)
        self.btn_forgot = QtWidgets.QPushButton(self.layoutWidget_3)
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
        self.btn_reset = QtWidgets.QPushButton(Dialog)
        self.btn_reset.setGeometry(QtCore.QRect(140, 270, 331, 31))
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
        self.btn_reset.setObjectName("btn_reset")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AIDS – Forgot Password"))
        self.lbl_email.setText(_translate("Dialog", "Email"))
        self.lbl_forgot.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#2c365d;\">Forgot password?</span></p></body></html>"))
        self.lbl_sub1.setText(_translate("Dialog", "Enter the email address associated with your account below"))
        self.lbl_sub2.setText(_translate("Dialog", "and we will send you a password reset code"))
        self.lbl_remember.setText(_translate("Dialog", "Remembered your password?"))
        self.btn_forgot.setText(_translate("Dialog", "Try logging in"))
        self.btn_reset.setText(_translate("Dialog", "Request reset code"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
