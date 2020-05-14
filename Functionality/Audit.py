import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.Audit import AuditLogs
from ConnectToDB import connectToDB
from Encryption import AESCipher

class auditClass(QtWidgets.QMainWindow, AuditLogs.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_logout.clicked.connect(self.logout)
        self.btn_back.clicked.connect(self.goBack)
        self.btn_search.clicked.connect(self.search)

        self.initializeData()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.search()

    def logout(self):
        self.parent.logout()
        self.close()
    
    def goBack(self):
        self.hide()
        self.parent.showself()

    def search(self):
        print('search')
        toSearch = self.searchbar.text()

        con = mdb.connect('localhost', 'root', '', 'aids')
        cur = con.cursor()

        if (toSearch != ""):
            query = 'SELECT user_id, time, actions_made from audit WHERE user_id = %s OR time = %s  OR actions_made = %s'
            data = (toSearch, toSearch, toSearch)

            cur.execute(query, data)

            result = cur.fetchall()
            self.getData(result)
        else:
            self.initializeData()
    
    def initializeData(self):
        con = connectToDB()
        cur = con.cursor()

        cur.execute('SELECT user_id, time, actions_made from audit ORDER BY time DESC')
        result = cur.fetchall()

        self.getData(result)

    def getData(self,result):
        self.table_audit.setRowCount(len(result))
        # print(result)
        row = 0
        for i in result:
            if (i[0] <= 9 and i[0] > 0):
                self.table_audit.setItem(row,0, QtWidgets.QTableWidgetItem('OP-00' + str(i[0])))
            elif (i[0] > 9):
                self.table_audit.setItem(row,0, QtWidgets.QTableWidgetItem('OP-0' + str(i[0])))
            else:
                self.table_audit.setItem(row,0, QtWidgets.QTableWidgetItem('OP-' + str(i[0])))
            self.table_audit.setItem(row,1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.table_audit.setItem(row,2, QtWidgets.QTableWidgetItem(str(i[2])))

            row += 1