# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewUserQDialog.ui'
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
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(130, 164, 353, 141))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl_error = QtWidgets.QLabel(self.layoutWidget_2)
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
        self.lbl_newpass = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_newpass.setFont(font)
        self.lbl_newpass.setStyleSheet("")
        self.lbl_newpass.setObjectName("lbl_newpass")
        self.verticalLayout_3.addWidget(self.lbl_newpass)
        self.txtNewPass = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtNewPass.setMinimumSize(QtCore.QSize(347, 31))
        self.txtNewPass.setMaximumSize(QtCore.QSize(347, 31))
        self.txtNewPass.setStyleSheet("")
        self.txtNewPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtNewPass.setObjectName("txtNewPass")
        self.verticalLayout_3.addWidget(self.txtNewPass)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_confirmPass = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_confirmPass.setFont(font)
        self.lbl_confirmPass.setStyleSheet("")
        self.lbl_confirmPass.setObjectName("lbl_confirmPass")
        self.verticalLayout_4.addWidget(self.lbl_confirmPass)
        self.txtConfirmPass = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtConfirmPass.setMinimumSize(QtCore.QSize(247, 31))
        self.txtConfirmPass.setMaximumSize(QtCore.QSize(347, 31))
        self.txtConfirmPass.setStyleSheet("")
        self.txtConfirmPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtConfirmPass.setObjectName("txtConfirmPass")
        self.verticalLayout_4.addWidget(self.txtConfirmPass)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.btnReset = QtWidgets.QPushButton(Dialog)
        self.btnReset.setGeometry(QtCore.QRect(130, 330, 351, 31))
        self.btnReset.setStyleSheet("QPushButton {\n"
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
        self.btnReset.setObjectName("btnReset")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AIDS – Reset Password"))
        self.lbl_verification_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#2c365d;\">Change Password</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Password must have at least 8 characters, an upper case (A-Z),"))
        self.label_2.setText(_translate("Dialog", "and a number (0-9). Special Characters are optional"))
        self.lbl_newpass.setText(_translate("Dialog", "New Password"))
        self.lbl_confirmPass.setText(_translate("Dialog", "Re-enter Password"))
        self.btnReset.setText(_translate("Dialog", "Change Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
