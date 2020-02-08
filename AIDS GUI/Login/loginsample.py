# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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
        MainWindow.setBaseSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.app_logo = QtWidgets.QLabel(self.centralwidget)
        self.app_logo.setGeometry(QtCore.QRect(70, 20, 135, 114))
        self.app_logo.setText("")
        self.app_logo.setPixmap(QtGui.QPixmap("../Resources/aids_logo.png"))
        self.app_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.app_logo.setObjectName("app_logo")
        self.hline = QtWidgets.QFrame(self.centralwidget)
        self.hline.setGeometry(QtCore.QRect(30, 310, 531, 20))
        self.hline.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline.setObjectName("hline")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(200, 40, 291, 68))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.aids_logo = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Audiowide")
        font.setPointSize(28)
        font.setKerning(True)
        self.aids_logo.setFont(font)
        self.aids_logo.setObjectName("aids_logo")
        self.app_name = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Barlow Medium")
        font.setPointSize(12)
        font.setKerning(True)
        self.app_name.setFont(font)
        self.app_name.setObjectName("app_name")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(370, 270, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.lbl_response = QtWidgets.QLabel(self.centralwidget)
        self.lbl_response.setGeometry(QtCore.QRect(156, 123, 311, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.lbl_response.sizePolicy().hasHeightForWidth())
        self.lbl_response.setSizePolicy(sizePolicy)
        self.lbl_response.setMinimumSize(QtCore.QSize(311, 20))
        self.lbl_response.setMaximumSize(QtCore.QSize(311, 20))
        self.lbl_response.setBaseSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl_response.setFont(font)
        self.lbl_response.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_response.setObjectName("lbl_response")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(130, 157, 344, 33))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user_icon = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_icon.sizePolicy().hasHeightForWidth())
        self.user_icon.setSizePolicy(sizePolicy)
        self.user_icon.setMinimumSize(QtCore.QSize(66, 31))
        self.user_icon.setMaximumSize(QtCore.QSize(66, 31))
        self.user_icon.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.user_icon.setFont(font)
        self.user_icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_icon.setText("")
        self.user_icon.setPixmap(QtGui.QPixmap("../Resources/user_icon.png"))
        self.user_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.user_icon.setObjectName("user_icon")
        self.horizontalLayout.addWidget(self.user_icon)
        self.txt_username = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_username.sizePolicy().hasHeightForWidth())
        self.txt_username.setSizePolicy(sizePolicy)
        self.txt_username.setMinimumSize(QtCore.QSize(270, 31))
        self.txt_username.setMaximumSize(QtCore.QSize(270, 31))
        self.txt_username.setSizeIncrement(QtCore.QSize(5, 0))
        self.txt_username.setBaseSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.txt_username.setFont(font)
        self.txt_username.setStyleSheet("padding-left: 4px;")
        self.txt_username.setObjectName("txt_username")
        self.horizontalLayout.addWidget(self.txt_username)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(150, 210, 321, 33))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password_icon = QtWidgets.QLabel(self.widget1)
        self.password_icon.setText("")
        self.password_icon.setPixmap(QtGui.QPixmap("../Resources/padlock_icon.png"))
        self.password_icon.setObjectName("password_icon")
        self.horizontalLayout_2.addWidget(self.password_icon)
        self.txt_password = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.txt_password.sizePolicy().hasHeightForWidth())
        self.txt_password.setSizePolicy(sizePolicy)
        self.txt_password.setMinimumSize(QtCore.QSize(270, 31))
        self.txt_password.setMaximumSize(QtCore.QSize(270, 31))
        self.txt_password.setSizeIncrement(QtCore.QSize(5, 0))
        self.txt_password.setBaseSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet("padding-left: 4px;")
        self.txt_password.setText("")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.horizontalLayout_2.addWidget(self.txt_password)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(110, 343, 364, 33))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_forgot = QtWidgets.QLabel(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.lbl_forgot.sizePolicy().hasHeightForWidth())
        self.lbl_forgot.setSizePolicy(sizePolicy)
        self.lbl_forgot.setMinimumSize(QtCore.QSize(187, 31))
        self.lbl_forgot.setMaximumSize(QtCore.QSize(187, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_forgot.setFont(font)
        self.lbl_forgot.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_forgot.setObjectName("lbl_forgot")
        self.horizontalLayout_3.addWidget(self.lbl_forgot)
        self.btn_forgot = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_forgot.sizePolicy().hasHeightForWidth())
        self.btn_forgot.setSizePolicy(sizePolicy)
        self.btn_forgot.setMinimumSize(QtCore.QSize(169, 31))
        self.btn_forgot.setMaximumSize(QtCore.QSize(169, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.btn_forgot.setFont(font)
        self.btn_forgot.setObjectName("btn_forgot")
        self.horizontalLayout_3.addWidget(self.btn_forgot)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_username, self.txt_password)
        MainWindow.setTabOrder(self.txt_password, self.btn_login)
        MainWindow.setTabOrder(self.btn_login, self.btn_forgot)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIDS Login"))
        self.aids_logo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">AIDS</span></p></body></html>"))
        self.app_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">Air-based Inspection Deployment System</span></p></body></html>"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.lbl_response.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.txt_username.setPlaceholderText(_translate("MainWindow", "User ID"))
        self.txt_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lbl_forgot.setText(_translate("MainWindow", "Forgot Password?"))
        self.btn_forgot.setText(_translate("MainWindow", "Reset Password"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())