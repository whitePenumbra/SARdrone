import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.ViewPilot import ViewPilotAlt
import MySQLdb as mdb

class viewClass(QtWidgets.QMainWindow, ViewPilotAlt.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_pastops.clicked.connect(self.pastOps)
        self.btn_update.clicked.connect(self.updateInfo)

        result = self.parent.getInfo()

        conn = mdb.connect('localhost', 'root', '', 'aids')
        cur = conn.cursor() 

        cur.execute('SELECT * FROM address WHERE address_id = %s', (result[1],))
        addressTuple = cur.fetchall()

        for i in addressTuple:
            address = i
        
        print(address)

        self.lbl_id.setText("OP-00" + str(result[0]))
        self.lbl_gender.setText('')
        self.lbl_dob.setText('')
        self.lbl_address.setText(address[1])
        self.lbl_city.setText(address[2])
        self.lbl_province.setText(address[3])
        self.lbl_zip.setText(address[4])

        self.lbl_email.setText('')
        self.lbl_mobile.setText('')
        self.lbl_emContact.setText('')
        self.lbl_emNumber.setText('')

        self.lbl_certification.setText('')
        self.lbl_operator.setText('')
        self.lbl_issuedate.setText('')
        self.lbl_expirydate.setText('')

        # print(result)

    def cancel(self):
        self.parent.showself()
        self.close()

    def updateInfo(self):
        print('update')

    def pastOps(self):
        print('past')