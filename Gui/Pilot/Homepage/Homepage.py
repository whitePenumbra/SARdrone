# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1257, 914)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(870, 20, 361, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.logout_layout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.logout_layout.setContentsMargins(0, 0, 0, 0)
        self.logout_layout.setObjectName("logout_layout")
        self.lbl_user = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl_user.setFont(font)
        self.lbl_user.setText("")
        self.lbl_user.setScaledContents(False)
        self.lbl_user.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_user.setObjectName("lbl_user")
        self.logout_layout.addWidget(self.lbl_user)
        self.btn_logout = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_logout.setMinimumSize(QtCore.QSize(121, 31))
        self.btn_logout.setMaximumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_logout.setFont(font)
        self.btn_logout.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color: #E53935;\n"
"border: 1.2px solid #D32F2F;\n"
"outline: none;}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #D32F2F;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #C62828;\n"
"outline: none;\n"
"border: none;\n"
"}")
        self.btn_logout.setObjectName("btn_logout")
        self.logout_layout.addWidget(self.btn_logout)
        self.btn_profile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_profile.setGeometry(QtCore.QRect(30, 22, 160, 31))
        self.btn_profile.setMinimumSize(QtCore.QSize(160, 31))
        self.btn_profile.setMaximumSize(QtCore.QSize(160, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_profile.setFont(font)
        self.btn_profile.setStyleSheet("QPushButton {\n"
"color: #009688;\n"
"background-color: rgb(240, 240, 240);\n"
"border: 2px solid #009688;\n"
"outline: none;}\n"
"                \n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#26A69A;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"                \n"
"QPushButton:pressed{\n"
"background-color: #00897B;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"                \n"
"                ")
        self.btn_profile.setObjectName("btn_profile")
        self.btn_pastOps = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pastOps.setGeometry(QtCore.QRect(210, 22, 160, 31))
        self.btn_pastOps.setMinimumSize(QtCore.QSize(160, 31))
        self.btn_pastOps.setMaximumSize(QtCore.QSize(160, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_pastOps.setFont(font)
        self.btn_pastOps.setStyleSheet("QPushButton {\n"
"color: #009688;\n"
"background-color: rgb(240, 240, 240);\n"
"border: 2px solid #009688;\n"
"outline: none;}\n"
"                \n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#26A69A;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"                \n"
"QPushButton:pressed{\n"
"background-color: #00897B;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"                \n"
"                ")
        self.btn_pastOps.setObjectName("btn_pastOps")
        self.droneStream = QtWidgets.QWidget(self.centralwidget)
        self.droneStream.setGeometry(QtCore.QRect(30, 80, 1201, 480))
        self.droneStream.setMinimumSize(QtCore.QSize(1201, 480))
        self.droneStream.setMaximumSize(QtCore.QSize(1201, 480))
        self.droneStream.setObjectName("droneStream")
        self.droneMap = QtWidgets.QWidget(self.centralwidget)
        self.droneMap.setGeometry(QtCore.QRect(30, 570, 481, 331))
        self.droneMap.setMinimumSize(QtCore.QSize(481, 331))
        self.droneMap.setMaximumSize(QtCore.QSize(481, 331))
        self.droneMap.setObjectName("droneMap")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(550, 630, 162, 184))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.operations_layout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.operations_layout.setContentsMargins(0, 0, 0, 0)
        self.operations_layout.setObjectName("operations_layout")
        self.btn_Launch = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_Launch.setMinimumSize(QtCore.QSize(160, 31))
        self.btn_Launch.setMaximumSize(QtCore.QSize(160, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_Launch.setFont(font)
        self.btn_Launch.setStyleSheet("QPushButton {\n"
"color: rgb(212, 128, 0);\n"
"background-color: rgb(240, 240, 240);\n"
"border: 2px solid #FF9D07;\n"
"outline: none;}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(255, 176, 6);\n"
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
        self.btn_Launch.setObjectName("btn_Launch")
        self.operations_layout.addWidget(self.btn_Launch)
        self.btn_endOps = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_endOps.setMinimumSize(QtCore.QSize(160, 31))
        self.btn_endOps.setMaximumSize(QtCore.QSize(160, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_endOps.setFont(font)
        self.btn_endOps.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 176, 6);\n"
"border: 1.2px solid #ff9d07;\n"
"outline: none;\n"
"}\n"
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
"}")
        self.btn_endOps.setObjectName("btn_endOps")
        self.operations_layout.addWidget(self.btn_endOps)
        self.btn_PDF = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_PDF.setMinimumSize(QtCore.QSize(160, 31))
        self.btn_PDF.setMaximumSize(QtCore.QSize(160, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_PDF.setFont(font)
        self.btn_PDF.setStyleSheet("QPushButton {\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(202, 202, 202);\n"
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
        self.btn_PDF.setObjectName("btn_PDF")
        self.operations_layout.addWidget(self.btn_PDF)
        self.droneConsole = QtWidgets.QTextBrowser(self.centralwidget)
        self.droneConsole.setGeometry(QtCore.QRect(750, 570, 231, 331))
        self.droneConsole.setMinimumSize(QtCore.QSize(231, 331))
        self.droneConsole.setMaximumSize(QtCore.QSize(231, 331))
        self.droneConsole.setObjectName("droneConsole")
        self.droneConsole_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.droneConsole_2.setGeometry(QtCore.QRect(1000, 570, 231, 331))
        self.droneConsole_2.setMinimumSize(QtCore.QSize(231, 331))
        self.droneConsole_2.setMaximumSize(QtCore.QSize(231, 331))
        self.droneConsole_2.setObjectName("droneConsole_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIDS – Home"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
        self.btn_profile.setText(_translate("MainWindow", "View Profile"))
        self.btn_pastOps.setText(_translate("MainWindow", "Past Operations"))
        self.btn_Launch.setText(_translate("MainWindow", "Launch Drone"))
        self.btn_endOps.setText(_translate("MainWindow", "End Operation"))
        self.btn_PDF.setText(_translate("MainWindow", "Download PDF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
