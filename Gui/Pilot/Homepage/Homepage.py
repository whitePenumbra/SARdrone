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
        MainWindow.resize(1071, 739)
        MainWindow.setMinimumSize(QtCore.QSize(1071, 739))
        MainWindow.setMaximumSize(QtCore.QSize(1071, 739))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(680, 20, 361, 33))
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
        self.btn_logout.setObjectName("btn_logout")
        self.logout_layout.addWidget(self.btn_logout)
        self.btn_profile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_profile.setGeometry(QtCore.QRect(30, 21, 160, 31))
        self.btn_profile.setMinimumSize(QtCore.QSize(160, 31))
        self.btn_profile.setMaximumSize(QtCore.QSize(160, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_profile.setFont(font)
        self.btn_profile.setStyleSheet("QPushButton {\n"
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
        self.btn_profile.setObjectName("btn_profile")
        self.btn_pastOps = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pastOps.setGeometry(QtCore.QRect(210, 21, 160, 31))
        self.btn_pastOps.setMinimumSize(QtCore.QSize(160, 31))
        self.btn_pastOps.setMaximumSize(QtCore.QSize(160, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_pastOps.setFont(font)
        self.btn_pastOps.setStyleSheet("QPushButton {\n"
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
        self.btn_pastOps.setObjectName("btn_pastOps")

        #System Errors
        #call when there are system errors

        """msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Warning")
        msgBox.setWindowIcon(icon)
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        font = QtGui.QFont()
        font.setPointSize(10)
        msgBox.setFont(font)
        msgBox.setText("Error: Internal Server Error ")
        #msgBox.setInformativeText("Internal Server Error")
        

        msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        ret = msgBox.exec_()"""

        #END DELETE PILOT


        self.droneStream = QtWidgets.QWidget(self.centralwidget)
        self.droneStream.setGeometry(QtCore.QRect(30, 80, 1011, 341))
        self.droneStream.setObjectName("droneStream")
        self.droneConsole = QtWidgets.QWidget(self.centralwidget)
        self.droneConsole.setGeometry(QtCore.QRect(640, 430, 401, 291))
        self.droneConsole.setObjectName("droneConsole")
        self.droneMap = QtWidgets.QWidget(self.centralwidget)
        self.droneMap.setGeometry(QtCore.QRect(30, 430, 401, 291))
        self.droneMap.setObjectName("droneMap")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(450, 480, 162, 181))
        self.widget.setObjectName("widget")
        self.operations_layout = QtWidgets.QVBoxLayout(self.widget)
        self.operations_layout.setContentsMargins(0, 0, 0, 0)
        self.operations_layout.setObjectName("operations_layout")
        self.btn_Launch = QtWidgets.QPushButton(self.widget)
        self.btn_Launch.setMinimumSize(QtCore.QSize(160, 31))
        self.btn_Launch.setMaximumSize(QtCore.QSize(160, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_Launch.setFont(font)
        self.btn_Launch.setStyleSheet("QPushButton {\n"
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
        self.btn_Launch.setObjectName("btn_Launch")
        self.operations_layout.addWidget(self.btn_Launch)
        self.btn_endOps = QtWidgets.QPushButton(self.widget)
        self.btn_endOps.setMinimumSize(QtCore.QSize(160, 31))
        self.btn_endOps.setMaximumSize(QtCore.QSize(160, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_endOps.setFont(font)
        self.btn_endOps.setStyleSheet("QPushButton {\n"
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
        self.btn_endOps.setObjectName("btn_endOps")
        self.operations_layout.addWidget(self.btn_endOps)
        self.btn_PDF = QtWidgets.QPushButton(self.widget)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.image_label = QtWidgets.QLabel(MainWindow)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        # self.verticalLayout.addWidget(self.image_label)

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
