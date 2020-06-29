import sys, datetime
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.Homepage import HomepageAlt
from Gui.Administrator.ViewPilot import ViewPilotAlt
from AddPilot import addClass
from ViewPilot import viewClass
from Audit import auditClass
from DeletePilot import deleteClass, deleteSuccessClass, deleteErrorClass
from ConnectToDB import connectToDB
from Operations import operationClass

class adminhomepageClass(QtWidgets.QMainWindow, HomepageAlt.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.btn_add.clicked.connect(self.add)
        self.btn_operations.clicked.connect(self.operations)
        self.btn_search.clicked.connect(self.search)
        self.btn_logout.clicked.connect(self.logout)
        self.btn_audit.clicked.connect(self.openAudit)
        self.btn_deleteall.clicked.connect(self.multipleDelete)

        self.initializeData()

        self.strRow = ''

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.search()

    def openAudit(self):
        self.audit = auditClass(parent=self)
        self.audit.show()
        self.hide()

    def add(self):
        print('adddddd')
        self.addPilot = addClass(parent=self)
        self.addPilot.show()
        self.close()

    def operations(self):
        print('operations')
        self.operations = operationClass(parent=self)
        self.operations.show()
        self.close()

    def search(self):
        print('search')
        toSearch = self.searchbar.text()

        conn = connectToDB()
        cur = conn.cursor()

        if (toSearch != "" or toSearch.startswith('OP-')):
            if (toSearch.startswith('OP-') or toSearch.startswith('op-')):
                toSearch = toSearch[3:]
            cur.execute('SELECT user_id,last_name,first_name from users WHERE '
            '(user_id = "%s" OR last_name = "%s" OR first_name = "%s") AND isActive = "1"' % (toSearch,toSearch,toSearch))
            result = cur.fetchall()
            self.getData(result)
        else:
            self.initializeData()
    
    def logout(self):
        self.close()
        self.parent.showself()

    def showself(self):
        self.initializeData()
        self.show()
    
    def deletes(self):
        button = self.sender()
        self.rows = self.table_pilots.indexAt(button.pos()).row()

        print("Call delete class")
        self.deleteData = deleteClass(parent=self)
        self.deleteData.show()
    
    def softDelete(self, row):
        print("Soft Delete:I was called")
        print(str(row))
        # tempID = self.table_pilots.item(row,1).text()[3:]
        print(int(self.table_pilots.item(row,1).text()[3:]))
        self.pilotID = int(self.table_pilots.item(row,1).text()[3:])
        # self.pilotID = int(tempID)

        lastName = self.table_pilots.item(row,2).text()
        firstName = self.table_pilots.item(row,3).text()

        try:
            conn = connectToDB()
            cur = conn.cursor()

            print(str(self.pilotID) + " " + firstName + " " + lastName)
            cur.execute('UPDATE users SET isActive = 0 WHERE first_name = "%s" AND last_name = "%s" AND user_id = "%s"' % (firstName, lastName, self.pilotID))
            conn.commit()

            self.deleteSuccess = deleteSuccessClass(parent=self)
            self.deleteSuccess.show()
            self.deleteSuccess.activateWindow()
        except Exception as e:
            self.deleteError = deleteErrorClass(parent=self)
            self.deleteError.show()
            self.deleteError.activateWindow()
            print(e)

        self.audits("Admin deleted pilot " + firstName + " " + lastName)
        self.initializeData()
    
    def multipleSelect(self):
        print('change state')
        button = self.sender()
        self.multipleRows = self.table_pilots.indexAt(button.pos()).row()
        self.strRow += str(self.multipleRows)
        self.tupleRow = tuple(self.strRow)
        print(self.tupleRow)

    def multipleDelete(self, rows):
        print("I'm supposed to do something")
        
        i=0
        strToDelete = ''
        while(i<=self.table_pilots.rowCount()):
            count = self.tupleRow.count(str(i))
            print(count)
            if (count%2 != 0):
                strToDelete += str(i)
            i+=1
        tupleToDelete = tuple(strToDelete)
        print(tupleToDelete)

        if "0" in tupleToDelete:
            for i in tupleToDelete:
                iToInt = int(i)
                if(iToInt > 0):
                    iToInt -=1
                print(iToInt)
                self.softDelete(iToInt)
        else:
            counter = 0
            for i in tupleToDelete:
                iToInt = int(i)
                if(counter > 0):
                    iToInt -= 1
                print(counter)
                counter+=1
                self.softDelete(iToInt)

    def view(self):
        print('view')
        button = self.sender()
        row = self.table_pilots.indexAt(button.pos()).row()
        print(row)
        self.viewForm = viewClass(parent=self)
        self.viewForm.show()
        self.hide()
    
    def getInfo(self):
        button = self.sender()
        row = self.table_pilots.indexAt(button.pos()).row()
        print("this is teh row")
        print(row)

        lastName = self.table_pilots.item(row,2).text()
        firstName = self.table_pilots.item(row,3).text()  

        conn = connectToDB()
        cur = conn.cursor()      

        cur.execute('SELECT * FROM users WHERE first_name = "%s" AND last_name = "%s"' % (firstName,lastName))
        result = cur.fetchall()

        # print(result)

        infoTuple = ((),)
        for i in result:
            infoTuple = i
        
        return (infoTuple)

    def initializeData(self):
        con = connectToDB()
        cur = con.cursor()

        cur.execute('SELECT user_id,last_name,first_name from users WHERE isActive = 1 AND user_type = 1')
        result = cur.fetchall()

        self.getData(result)

    def getData(self,result):
        self.table_pilots.setRowCount(len(result))
        # print(result)
        row = 0
        for i in result:

            # delete multiple
            layout_delete = QtWidgets.QHBoxLayout()
            self.cb_delete = QtWidgets.QCheckBox()
            self.cb_delete.stateChanged.connect(self.multipleSelect)
            self.cb_delete.setCheckState(QtCore.Qt.Unchecked)
            layout_delete.addWidget(self.cb_delete, 10)
            layout_delete.setAlignment(QtCore.Qt.AlignCenter)
            layout_delete.setContentsMargins(18, 0, 0, 0)

            # self.cellWidget = QtWidgets.QWidget()
            # self.cellWidget.setLayout(layout_delete)

            self.table_pilots.setCellWidget(row,0,self.cb_delete)
            if (i[0] <= 9 and i[0] > 0):
                self.table_pilots.setItem(row,1, QtWidgets.QTableWidgetItem('OP-00' + str(i[0])))
            elif (i[0] > 9):
                self.table_pilots.setItem(row,1, QtWidgets.QTableWidgetItem('OP-0' + str(i[0])))
            else:
                self.table_pilots.setItem(row,1, QtWidgets.QTableWidgetItem('OP-' + str(i[0])))
            self.table_pilots.setItem(row,2, QtWidgets.QTableWidgetItem(i[1]))
            self.table_pilots.setItem(row,3, QtWidgets.QTableWidgetItem(i[2]))

            #create buttons inside table cell
            layout = QtWidgets.QHBoxLayout()
            self.btn_view = QtWidgets.QPushButton()
            self.btn_view.clicked.connect(self.view)
            self.btn_delete = QtWidgets.QPushButton()
            self.btn_delete.clicked.connect(self.deletes)
            self.btn_view.setFixedHeight(34)
            self.btn_delete.setFixedHeight(34)
            self.btn_delete.setIcon(QtGui.QIcon("../Gui/Resources/trash_delete_2.png"))
            self.btn_delete.setIconSize(QtCore.QSize(22,22))
            self.btn_view.setIcon(QtGui.QIcon("../Gui/Resources/file_view.png"))
            self.btn_view.setIconSize(QtCore.QSize(22,22))
            font = QtGui.QFont()
            font.setFamily("Helvetica")
            font.setPointSize(11)
            self.btn_view.setFont(font)
            self.btn_delete.setFont(font)
            self.btn_delete.setStyleSheet("QPushButton {\n"
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
    "}\n"
    "\n"
    "\n"
    "")
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
            self.btn_delete.setCursor(QtCore.Qt.PointingHandCursor)
            layout.addStretch()
            layout.addWidget(self.btn_view,20)
            layout.addWidget(self.btn_delete,20)

            #button placement
            self.table_pilots.setCellWidget(row,4,self.btn_view)
            self.table_pilots.setCellWidget(row,5,self.btn_delete)
            self.table_pilots.horizontalHeader().setStyleSheet( "QHeaderView::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid #D8D8D8;"
                "border-bottom: 1px solid #D8D8D8;"
                "background-color:white;"
                "padding:4px;"
            "}"
            "QTableCornerButton::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid #D8D8D8;"
                "border-bottom: 1px solid #D8D8D8;"
                "background-color:white;"
            "}" );

            row += 1
            # vars().update(buttonDict)

    def audits(self, message):
        conn = connectToDB()
        cur = conn.cursor()

        cur.execute("SELECT user_id FROM users WHERE user_type = 0")
        result = cur.fetchall()

        uid = result[0][0]
        currentTime = datetime.datetime.now()

        query = "INSERT INTO audit(user_id, time, actions_made) VALUES (%s, %s, %s)"
        values = (str(uid), currentTime, str(message))

        cur.execute(query,values)
        conn.commit()