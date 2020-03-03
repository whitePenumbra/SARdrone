import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.ViewPilot import ViewPilotAlt
import MySQLdb as mdb
from UpdatePilot import updateClass

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
        print(result)

        self.lbl_addPilot.setText(str(result[3]) + " " + str(result[2]))
        self.lbl_id.setText("OP-00" + str(result[0]))
        if (result[13] == 1):
            self.lbl_gender.setText('Male')
        else:
            self.lbl_gender.setText('Female')
        self.lbl_dob.setText(str(result[14]))
        self.lbl_address.setText(address[1])
        self.lbl_city.setText(address[2])
        self.lbl_province.setText(address[3])
        self.lbl_zip.setText(address[4])

        self.lbl_email.setText(str(result[15]))
        self.lbl_mobile.setText(str(result[16]))
        self.lbl_emContact.setText(str(result[10]))
        self.lbl_emNumber.setText(str(result[11]))

        self.lbl_certification.setText(str(result[9]))
        self.lbl_operator.setText(str(result[12]))
        self.lbl_issuedate.setText(str(result[7]))
        self.lbl_expirydate.setText(str(result[8]))

        # print(result)

    def cancel(self):
        self.parent.showself()
        self.close()

    def updateInfo(self):
        self.updateForm = updateClass(parent=self)
        self.updateForm.show()
        self.hide()

    def pastOps(self):
        print('past')