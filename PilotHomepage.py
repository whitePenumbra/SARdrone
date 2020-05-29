from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebChannel
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl, QTimer
from PyQt5  import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow

import human_counter
from vis_helper import vis_util

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.webchannel = QtWebChannel.QWebChannel(self)

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
        self.btn_profile.setGeometry(QtCore.QRect(30, 22, 160, 31))
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
        self.btn_pastOps.setGeometry(QtCore.QRect(210, 22, 160, 31))
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
        self.droneMap = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.droneMap.setGeometry(QtCore.QRect(30, 410, 401, 301))
        self.droneMap.setObjectName("droneMap")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(450, 460, 162, 181))
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
        self.btn_endOps = QtWidgets.QPushButton(self.layoutWidget1)
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(619, 410, 421, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.coordinates = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.coordinates.setObjectName("coordinates")
        self.horizontalLayout.addWidget(self.coordinates)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout.addWidget(self.textBrowser_2)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget_2.setGeometry(QtCore.QRect(180, 80, 651, 331))
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.drone_stream = QtWidgets.QLabel(self.horizontalWidget_2)
        self.drone_stream.setText("")
        self.drone_stream.setObjectName("drone_stream")
        self.horizontalLayout_2.addWidget(self.drone_stream)
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

from PyQt5.QtWebEngineWidgets import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.droneMap.load(QUrl.fromLocalFile(r"\pointer.html"))
        self.droneMap.page().setWebChannel(self.webchannel)
        self.webchannel.registerObject('MyChannel', self)

    @QtCore.pyqtSlot(str)
    def addWaypoint(self, coords):
        self.coordinates.append(coords)
        print(coords)

    def GetTimer(self):
        self.timer=QTimer(QMainWindow)
        self.timer.setInterval(0.05)
        # noinspection PyTypeChecker
        self.timer.timeout.connect(self.getNextFrame())
        self.timer.start()

    def getNextFrame(self):
        cvImg = vis_util.next_proc_frame('')

        height, width, channel = cvImg.shape
        bytesPerLine = 3 * width
        qImg = QImage(cvImg.data, width, height, bytesPerLine, QImage.Format_RGB888)

        self.drone_stream.setPixmap(qImg)



#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    w = MainWindow()
#    w.show()
#    sys.exit(app.exec_())