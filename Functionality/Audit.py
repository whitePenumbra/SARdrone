import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.Audit import AuditLogs
import MySQLdb as mdb
from Encryption import AESCipher

class auditClass(QtWidgets.QMainWindow, AuditLogs.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_logout.clicked.connect(self.logout)
        self.btn_back.clicked.connect(self.goBack)
        self.btn_search.clicked.connect(self.search)

    def logout(self):
        self.parent.logout()
    
    def goBack(self):
        self.hide()
        self.parent.showself()

        def search(self):
        print('search')
        toSearch = self.searchbar.text()

        con = mdb.connect('localhost', 'root', '', 'aids')
        cur = con.cursor()

        if (toSearch != ""):
            cur.execute('SELECT user_id,last_name,first_name from users WHERE '
            'user_id = "%s" OR last_name = "%s" OR first_name = "%s"' % (toSearch,toSearch,toSearch))
            result = cur.fetchall()
            self.getData(result)
        else:
            self.initializeData()