import sys, os, cv2, datetime
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, 
                             QLabel, QVBoxLayout)
sys.path.append('..')
from Gui.Pilot.PastOperations import PastOperations
from ConnectToDB import connectToDB

class pilotOperationClass(QtWidgets.QMainWindow, PastOperations.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.btn_logout.clicked.connect(self.logout)
        self.btn_back.clicked.connect(self.back)

        self.pilot = self.parent.currentUser[0]
        self.initializeData()

    def logout(self):
        self.parent.logout()
        self.close()
    
    def back(self):
        self.close()
        self.parent.show()

    def initializeData(self):
        con = connectToDB()
        cur = con.cursor()

        print("adasdasdasdaddaaaaaaa")
        print(str(self.pilot[0]))
        cur.execute('SELECT ops_id FROM user_operations WHERE user_id = %s', (str(self.pilot[0]),))
        result = cur.fetchall()
        print(result)
        opsID = str(result[0][0])

        cur.execute('SELECT ops_id, date_of_ops, ops_location FROM operations WHERE ops_id = %s', (opsID,))
        result = cur.fetchall()

        self.getData(result)

    def getData(self,result):
        self.table_pilotOps.setRowCount(len(result))
        print(result)
        row = 0
        # buttonDict = {}
        for i in result:
            if (i[0] <= 9 and i[0] > 0):
                self.table_pilotOps.setItem(row,0, QtWidgets.QTableWidgetItem('OP-00' + str(i[0])))
            elif (i[0] > 9):
                self.table_pilotOps.setItem(row,0, QtWidgets.QTableWidgetItem('OP-0' + str(i[0])))
            else:
                self.table_pilotOps.setItem(row,0, QtWidgets.QTableWidgetItem('OP-' + str(i[0])))

            # self.table_pilotOps.setItem(row,1, QtWidgets.QTableWidgetItem(i[2].strftime("%d %b %Y")))
            self.table_pilotOps.setItem(row,1, QtWidgets.QTableWidgetItem("0000-00-00"))
            self.table_pilotOps.setItem(row,2, QtWidgets.QTableWidgetItem(i[2]))

            layout_view = QtWidgets.QHBoxLayout()
            self.btn_view = QtWidgets.QPushButton()
            self.btn_view.clicked.connect(self.view)
            self.btn_view.setFixedHeight(34)
            self.btn_view.setFixedWidth(170)
            self.btn_view.setIcon(QtGui.QIcon("../Gui/Resources/file_view.png"))
            self.btn_view.setIconSize(QtCore.QSize(22, 22))
            font = QtGui.QFont()
            font.setFamily("Helvetica")
            font.setPointSize(11)
            font.setKerning(True)
            self.btn_view.setFont(font)
            self.btn_view.setStyleSheet("QPushButton {\n"
                    "    background-color: #1E88E5;\n"
                    "    color: rgb(255, 255, 255);\n"
                    "border: 1.2px solid #1976D2;\n"
                    "outline: none;}\n"
                    "\n"
                    "QPushButton:hover{\n"
                    "    background-color: #1976D2;\n"
                    "outline: none;\n"
                    "border: none;\n"
                    "}\n"
                    "\n"
                    "QPushButton:pressed{\n"
                    "    background-color: #1565C0;\n"
                    "outline: none;\n"
                    "border: none;\n"
                    "}\n"
                    "\n"
                    "\n"
                    "")
            self.btn_view.setCursor(QtCore.Qt.PointingHandCursor)
            layout_view.addWidget(self.btn_view, 10)

            layout = QtWidgets.QHBoxLayout()
            cellWidget = QtWidgets.QWidget()
            cellWidget.setLayout(layout)

            cellWidget_View = QtWidgets.QWidget()
            cellWidget_View.setLayout(layout_view)

            # buttons placement
            self.table_pilotOps.setCellWidget(row, 3, self.btn_view)

            row += 1

    def view(self):
        print("asdasdasdasdasd")