# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeletePilotSuccess.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 191)
        MainWindow.setMinimumSize(QtCore.QSize(531, 191))
        MainWindow.setMaximumSize(QtCore.QSize(531, 191))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Gui/Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_OK = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OK.setGeometry(QtCore.QRect(200, 146, 131, 31))
        self.btn_OK.setMinimumSize(QtCore.QSize(131, 31))
        self.btn_OK.setMaximumSize(QtCore.QSize(131, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_OK.setFont(font)
        self.btn_OK.setStyleSheet("QPushButton {\n"
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
        self.btn_OK.setObjectName("btn_OK")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 481, 123))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Gui/Resources/success.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_success = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_success.setMinimumSize(QtCore.QSize(350, 49))
        self.lbl_success.setMaximumSize(QtCore.QSize(350, 49))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(19)
        self.lbl_success.setFont(font)
        self.lbl_success.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_success.setObjectName("lbl_success")
        self.horizontalLayout_2.addWidget(self.lbl_success)
        self.lbl_ID = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_ID.setMinimumSize(QtCore.QSize(121, 49))
        self.lbl_ID.setMaximumSize(QtCore.QSize(121, 49))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(19)
        self.lbl_ID.setFont(font)
        self.lbl_ID.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ID.setObjectName("lbl_ID")
        self.horizontalLayout_2.addWidget(self.lbl_ID)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Delete Pilot Success"))
        self.btn_OK.setText(_translate("MainWindow", "OK"))
        self.lbl_success.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#2c365d;\">Successfully removed Pilot ID:</span></p></body></html>"))
        self.lbl_ID.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\"><br/></span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
