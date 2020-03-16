# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginQDialog.ui'
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
        self.app_logo = QtWidgets.QLabel(Dialog)
        self.app_logo.setGeometry(QtCore.QRect(70, 20, 135, 114))
        self.app_logo.setText("")
        self.app_logo.setPixmap(QtGui.QPixmap("../Resources/aids_logo.png"))
        self.app_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.app_logo.setObjectName("app_logo")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 40, 293, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.aids_logo_2 = QtWidgets.QLabel(self.layoutWidget)
        self.aids_logo_2.setMinimumSize(QtCore.QSize(291, 43))
        self.aids_logo_2.setMaximumSize(QtCore.QSize(291, 43))
        font = QtGui.QFont()
        font.setFamily("Audiowide")
        font.setPointSize(28)
        font.setKerning(True)
        self.aids_logo_2.setFont(font)
        self.aids_logo_2.setObjectName("aids_logo_2")
        self.verticalLayout_2.addWidget(self.aids_logo_2)
        self.app_name_2 = QtWidgets.QLabel(self.layoutWidget)
        self.app_name_2.setMinimumSize(QtCore.QSize(291, 20))
        self.app_name_2.setMaximumSize(QtCore.QSize(291, 20))
        font = QtGui.QFont()
        font.setFamily("Barlow Medium")
        font.setPointSize(12)
        font.setKerning(True)
        self.app_name_2.setFont(font)
        self.app_name_2.setObjectName("app_name_2")
        self.verticalLayout_2.addWidget(self.app_name_2)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(110, 340, 364, 33))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.forgotpass_layout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.forgotpass_layout_2.setContentsMargins(0, 0, 0, 0)
        self.forgotpass_layout_2.setObjectName("forgotpass_layout_2")
        self.lbl_forgot_2 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_forgot_2.sizePolicy().hasHeightForWidth())
        self.lbl_forgot_2.setSizePolicy(sizePolicy)
        self.lbl_forgot_2.setMinimumSize(QtCore.QSize(187, 31))
        self.lbl_forgot_2.setMaximumSize(QtCore.QSize(187, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_forgot_2.setFont(font)
        self.lbl_forgot_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_forgot_2.setObjectName("lbl_forgot_2")
        self.forgotpass_layout_2.addWidget(self.lbl_forgot_2)
        self.btn_forgot_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_forgot_2.sizePolicy().hasHeightForWidth())
        self.btn_forgot_2.setSizePolicy(sizePolicy)
        self.btn_forgot_2.setMinimumSize(QtCore.QSize(169, 31))
        self.btn_forgot_2.setMaximumSize(QtCore.QSize(169, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.btn_forgot_2.setFont(font)
        self.btn_forgot_2.setStyleSheet("QPushButton {\n"
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
        self.btn_forgot_2.setObjectName("btn_forgot_2")
        self.forgotpass_layout_2.addWidget(self.btn_forgot_2)
        self.hline = QtWidgets.QFrame(Dialog)
        self.hline.setGeometry(QtCore.QRect(30, 310, 531, 20))
        self.hline.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline.setObjectName("hline")
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(150, 210, 321, 33))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.password_layout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.password_layout_2.setContentsMargins(0, 0, 0, 0)
        self.password_layout_2.setObjectName("password_layout_2")
        self.password_icon_2 = QtWidgets.QLabel(self.layoutWidget_3)
        self.password_icon_2.setText("")
        self.password_icon_2.setPixmap(QtGui.QPixmap("../Resources/padlock_icon.png"))
        self.password_icon_2.setObjectName("password_icon_2")
        self.password_layout_2.addWidget(self.password_icon_2)
        self.txt_password_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.txt_password_2.sizePolicy().hasHeightForWidth())
        self.txt_password_2.setSizePolicy(sizePolicy)
        self.txt_password_2.setMinimumSize(QtCore.QSize(270, 31))
        self.txt_password_2.setMaximumSize(QtCore.QSize(270, 31))
        self.txt_password_2.setSizeIncrement(QtCore.QSize(5, 0))
        self.txt_password_2.setBaseSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.txt_password_2.setFont(font)
        self.txt_password_2.setStyleSheet("padding-left: 4px;")
        self.txt_password_2.setText("")
        self.txt_password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password_2.setObjectName("txt_password_2")
        self.password_layout_2.addWidget(self.txt_password_2)
        self.layoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_4.setGeometry(QtCore.QRect(130, 157, 344, 33))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.username_layout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.username_layout_2.setContentsMargins(0, 0, 0, 0)
        self.username_layout_2.setObjectName("username_layout_2")
        self.user_icon_2 = QtWidgets.QLabel(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_icon_2.sizePolicy().hasHeightForWidth())
        self.user_icon_2.setSizePolicy(sizePolicy)
        self.user_icon_2.setMinimumSize(QtCore.QSize(66, 31))
        self.user_icon_2.setMaximumSize(QtCore.QSize(66, 31))
        self.user_icon_2.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.user_icon_2.setFont(font)
        self.user_icon_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_icon_2.setText("")
        self.user_icon_2.setPixmap(QtGui.QPixmap("../Resources/user_icon.png"))
        self.user_icon_2.setAlignment(QtCore.Qt.AlignCenter)
        self.user_icon_2.setObjectName("user_icon_2")
        self.username_layout_2.addWidget(self.user_icon_2)
        self.txt_username_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_username_2.sizePolicy().hasHeightForWidth())
        self.txt_username_2.setSizePolicy(sizePolicy)
        self.txt_username_2.setMinimumSize(QtCore.QSize(270, 31))
        self.txt_username_2.setMaximumSize(QtCore.QSize(270, 31))
        self.txt_username_2.setSizeIncrement(QtCore.QSize(5, 0))
        self.txt_username_2.setBaseSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.txt_username_2.setFont(font)
        self.txt_username_2.setStyleSheet("padding-left: 4px;")
        self.txt_username_2.setObjectName("txt_username_2")
        self.username_layout_2.addWidget(self.txt_username_2)
        self.btn_login = QtWidgets.QPushButton(Dialog)
        self.btn_login.setGeometry(QtCore.QRect(370, 270, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton {\n"
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
        self.btn_login.setObjectName("btn_login")
        self.lbl_response = QtWidgets.QLabel(Dialog)
        self.lbl_response.setGeometry(QtCore.QRect(180, 130, 311, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.lbl_response.sizePolicy().hasHeightForWidth())
        self.lbl_response.setSizePolicy(sizePolicy)
        self.lbl_response.setMinimumSize(QtCore.QSize(311, 20))
        self.lbl_response.setMaximumSize(QtCore.QSize(311, 20))
        self.lbl_response.setBaseSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_response.setFont(font)
        self.lbl_response.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_response.setObjectName("lbl_response")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AIDS Login"))
        self.aids_logo_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#2c365d;\">AIDS</span></p></body></html>"))
        self.app_name_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#2c365d;\">Air-based Inspection Deployment System</span></p></body></html>"))
        self.lbl_forgot_2.setText(_translate("Dialog", "Forgot Password?"))
        self.btn_forgot_2.setText(_translate("Dialog", "Reset Password"))
        self.txt_password_2.setPlaceholderText(_translate("Dialog", "Password"))
        self.txt_username_2.setPlaceholderText(_translate("Dialog", "User ID"))
        self.btn_login.setText(_translate("Dialog", "Login"))
        self.lbl_response.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
