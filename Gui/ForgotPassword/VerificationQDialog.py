# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VerificationQDialog.ui'
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
        icon.addPixmap(QtGui.QPixmap("../Gui/Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        #removes ? from title bar
        Dialog.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.lbl_error = QtWidgets.QLabel(Dialog)
        self.lbl_error.setGeometry(QtCore.QRect(140, 140, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.lbl_error.setFont(font)
        self.lbl_error.setStyleSheet("")
        self.lbl_error.setText("")
        self.lbl_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_error.setObjectName("lbl_error")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(40, 295, 521, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(110, 340, 361, 33))
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
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 170, 333, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.form_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setObjectName("form_layout")
        self.txt_verCode = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_verCode.setMinimumSize(QtCore.QSize(331, 31))
        self.txt_verCode.setMaximumSize(QtCore.QSize(331, 31))
        self.txt_verCode.setStyleSheet("padding-left: 4px;")
        self.txt_verCode.setObjectName("txt_verCode")
        self.form_layout.addWidget(self.txt_verCode)
        self.btn_verify = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_verify.sizePolicy().hasHeightForWidth())
        self.btn_verify.setSizePolicy(sizePolicy)
        self.btn_verify.setMinimumSize(QtCore.QSize(331, 31))
        self.btn_verify.setMaximumSize(QtCore.QSize(331, 31))
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
        self.form_layout.addWidget(self.btn_verify)
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(130, 80, 351, 71))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.title_layout = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout.setObjectName("title_layout")
        self.lbl_verification = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(26)
        self.lbl_verification.setFont(font)
        self.lbl_verification.setStyleSheet("")
        self.lbl_verification.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_verification.setObjectName("lbl_verification")
        self.title_layout.addWidget(self.lbl_verification)
        self.lbl_sub1 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_sub1.setFont(font)
        self.lbl_sub1.setStyleSheet("")
        self.lbl_sub1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sub1.setObjectName("lbl_sub1")
        self.title_layout.addWidget(self.lbl_sub1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AIDS – Verification"))
        self.lbl_remember.setText(_translate("Dialog", "Remembered your password?"))
        self.btn_forgot.setText(_translate("Dialog", "Try logging in"))
        self.btn_verify.setText(_translate("Dialog", "Verify"))
        self.lbl_verification.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#2c365d;\">Verification</span></p></body></html>"))
        self.lbl_sub1.setText(_translate("Dialog", "Enter the verification code we just sent to your email address"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
