import sys, os, cv2, datetime
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from ConnectToDB import connectToDB
from Gui.Administrator.PilotOperationsHistory import PilotOpsAlt
from ViewOperation import viewOperationClass

class adminViewHistory(QtWidgets.QMainWindow, PilotOpsAlt.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.pilot = self.parent.result

        self.initializeData()

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

            self.table_pilotOps.setItem(row,1, QtWidgets.QTableWidgetItem(i[1].strftime("%d %B %Y")))
            # self.table_pilotOps.setItem(row,1, QtWidgets.QTableWidgetItem("0000-00-00"))
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
        self.viewing = viewOperationClass(parent=self)
        self.viewing.show()
        self.close()

    def getInfo(self):
        button = self.sender()
        row = self.table_pilotOps.indexAt(button.pos()).row()

        opsID = self.table_pilotOps.item(row,0).text()[3:]
        location = self.table_pilotOps.item(row,2).text()
        dateData = self.table_pilotOps.item(row,1).text()
        date = datetime.datetime.strptime(dateData,"%d %B %Y") 

        conn = connectToDB()
        cur = conn.cursor()      

        cur.execute('SELECT * FROM operations WHERE ops_location = "%s" AND ops_id = "%s"' % (location,int(opsID)))
        result = cur.fetchall()
        # print(result)

        infoTuple = ((),)
        for i in result:
            infoTuple = i
        
        return (infoTuple)