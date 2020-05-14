# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeletePilotError.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 191)
        Dialog.setMinimumSize(QtCore.QSize(531, 191))
        Dialog.setMaximumSize(QtCore.QSize(531, 191))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        # removes ? from title bar
        Dialog.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.btn_OK = QtWidgets.QPushButton(Dialog)
        self.btn_OK.setGeometry(QtCore.QRect(200, 140, 131, 31))
        self.btn_OK.setMinimumSize(QtCore.QSize(131, 31))
        self.btn_OK.setMaximumSize(QtCore.QSize(131, 31))
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
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 0, 451, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.img_success = QtWidgets.QLabel(self.layoutWidget)
        self.img_success.setText("")
        self.img_success.setPixmap(QtGui.QPixmap("../../Resources/error.png"))
        self.img_success.setAlignment(QtCore.Qt.AlignCenter)
        self.img_success.setObjectName("img_success")
        self.verticalLayout.addWidget(self.img_success)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_success = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_success.setMinimumSize(QtCore.QSize(342, 31))
        self.lbl_success.setMaximumSize(QtCore.QSize(342, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(19)
        self.lbl_success.setFont(font)
        self.lbl_success.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_success.setObjectName("lbl_success")
        self.horizontalLayout.addWidget(self.lbl_success)
        self.lbl_success_2 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_success_2.setMinimumSize(QtCore.QSize(81, 31))
        self.lbl_success_2.setMaximumSize(QtCore.QSize(81, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(19)
        self.lbl_success_2.setFont(font)
        self.lbl_success_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_success_2.setObjectName("lbl_success_2")
        self.horizontalLayout.addWidget(self.lbl_success_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Delete Pilot Error"))
        self.btn_OK.setText(_translate("Dialog", "Dismiss"))
        self.lbl_success.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#2c365d;\">Failed to delete Pilot ID:</span></p></body></html>"))
        self.lbl_success_2.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())