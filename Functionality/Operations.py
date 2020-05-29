import sys, datetime, smtplib, ssl, re
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from ConnectToDB import connectToDB
from Gui.Administrator.OperationRecords import OperationRecordsAlt

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

        cur.execute('SELECT * FROM operations')
        result = cur.fetchall()

        self.getData(result)