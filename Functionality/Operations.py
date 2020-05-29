import sys, datetime, smtplib, ssl, re
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from ConnectToDB import connectToDB
from Gui.Administrator.OperationRecords import OperationRecordsAlt
from ViewOperation import viewOperationClass

class operationClass(QtWidgets.QMainWindow, OperationRecordsAlt.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.initializeData()

    def search(self):
        print('search')
        toSearch = self.searchbar.text()

        conn = connectToDB()
        cur = conn.cursor()

        if (toSearch != "" or toSearch.startswith('OP-')):
            if (toSearch.startswith('OP-') or toSearch.startswith('op-')):
                toSearch = toSearch[3:]
            cur.execute('SELECT user_id,last_name,first_name from users WHERE '
            'user_id = "%s" OR last_name = "%s" OR first_name = "%s"' % (toSearch,toSearch,toSearch))
            result = cur.fetchall()
            self.getData(result)
        else:
            self.initializeData()
    
    def cancel(self):
        self.parent.showself()
        self.close()

    def logout(self):
        self.close()
        self.parent.showself()

    def initializeData(self):
        con = connectToDB()
        cur = con.cursor()

        cur.execute('SELECT ops_id, ops_location, time_start FROM operations')
        result = cur.fetchall()

        # print(result)

        self.getData(result)
    
    def getData(self,result):
        self.table_records.setRowCount(len(result))
        # print(result)
        row = 0
        # buttonDict = {}
        for i in result:
            if (i[0] <= 9 and i[0] > 0):
                self.table_records.setItem(row,0, QtWidgets.QTableWidgetItem('OP-00' + str(i[0])))
            elif (i[0] > 9):
                self.table_records.setItem(row,0, QtWidgets.QTableWidgetItem('OP-0' + str(i[0])))
            else:
                self.table_records.setItem(row,0, QtWidgets.QTableWidgetItem('OP-' + str(i[0])))
            self.table_records.setItem(row,1, QtWidgets.QTableWidgetItem(i[2].strftime("%d %b %Y")))
            self.table_records.setItem(row,2, QtWidgets.QTableWidgetItem(i[1]))

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

            # download button
            layout = QtWidgets.QHBoxLayout()
            self.btn_download = QtWidgets.QPushButton()
            self.btn_download.clicked.connect(self.download)
            self.btn_download.setFixedHeight(34)
            self.btn_download.setFixedWidth(170)
            self.btn_download.setIcon(QtGui.QIcon("../Gui/Resources/download.png"))
            self.btn_download.setIconSize(QtCore.QSize(22, 22))
            self.btn_download.setFont(font)
            self.btn_download.setStyleSheet("QPushButton {\n"
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
            self.btn_download.setCursor(QtCore.Qt.PointingHandCursor)
            """layout.addStretch()"""
            layout.addWidget(self.btn_download, 10)

            cellWidget = QtWidgets.QWidget()
            cellWidget.setLayout(layout)

            cellWidget_View = QtWidgets.QWidget()
            cellWidget_View.setLayout(layout_view)

            # buttons placement
            self.table_records.setCellWidget(row, 3, self.btn_view)
            self.table_records.setCellWidget(row, 4, self.btn_download)

            row += 1
        
    def view(self):
        print("VIEW")
        button = self.sender()
        row = self.table_records.indexAt(button.pos()).row()
        print(row)
        self.viewForm = viewOperationClass(parent=self)
        self.viewForm.show()
        self.hide()

    def download(self):
        print("Download")

    def getInfo(self):
        button = self.sender()
        row = self.table_records.indexAt(button.pos()).row()

        opsID = self.table_records.item(row,0).text()[3:]
        location = self.table_records.item(row,2).text()
        dateData = self.table_records.item(row,1).text()
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
