import sys, datetime
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

        self.result = self.getData()
        addressTuple = self.getAddress(self.result)
        self.getImage()

        for i in addressTuple:
            address = i
        
        # print(address)
        # print(self.result)

        monthList = {
            '' : '00',
            'January': '01',
            'February': '02',
            'March': '03',
            'April': '04',
            'May': '05',
            'June': '06',
            'July': '07',
            'August': '08',
            'September': '09',
            'October': '10',
            'November': '11',
            'December': '12'
        }
        # yy/mm/dd str(self.result[14])

        self.lbl_addPilot.setText(str(self.result[4]) + " " + str(self.result[3]))
        self.lbl_id.setText("OP-00" + str(self.result[0]))
        if (self.result[14] == 1):
            self.lbl_gender.setText('Male')
        else:
            self.lbl_gender.setText('Female')
        self.lbl_dob.setText(self.result[15].strftime('%B %d, %Y'))
        address1 = address[1][0:50]
        address2 = address[1][50:]
        self.lbl_address.setText(address1)
        self.lbl_addressExt.setText(address2)
        self.lbl_city.setText(address[2])
        self.lbl_province.setText(address[3])
        self.lbl_zip.setText(address[4])

        self.lbl_email.setText(str(self.result[16]))
        self.lbl_mobile.setText(str(self.result[17]))
        self.lbl_emContact.setText(str(self.result[11]))
        self.lbl_emNumber.setText(str(self.result[12]))

        self.lbl_certification.setText(str(self.result[10]))
        self.lbl_operator.setText(str(self.result[13]))
        self.lbl_issuedate.setText(self.result[8].strftime('%B %d, %Y'))
        self.lbl_expirydate.setText(self.result[9].strftime('%B %d, %Y'))

        self.audit("Admin viewed " + str(self.result[4]) + " " + str(self.result[3]) + "'s profile")

    def cancel(self):
        self.parent.showself()
        self.close()

    def updateInfo(self):
        self.updateForm = updateClass(self.result, parent=self)
        self.updateForm.show()
        self.hide()

    def pastOps(self):
        print('past')
    
    def getData(self):
        userTuple = self.parent.getInfo()

        return userTuple
    
    def getAddress(self,result):
        conn = self.connectToDB()
        cur = conn.cursor() 

        cur.execute('SELECT * FROM address WHERE address_id = %s', (result[1],))
        addressTuple = cur.fetchall()

        return addressTuple

    def getImage(self):
        image_data = self.result[2]
        if (self.result[2] == ''):
            imageLoc = "../Gui/Resources/profile_placeholder.png"
            image = QtGui.QPixmap(imageLoc)
            self.lbl_profilePic.setPixmap(image)
        else:
            image = QtGui.QImage.fromData(image_data)
            pixmap = QtGui.QPixmap.fromImage(image)

            self.lbl_profilePic.setPixmap(pixmap)

    def connectToDB(self):
        try:
            db = mdb.connect('localhost', 'root', '', 'aids')
            return (db)

        except mdb.Error as e:
            print('Connection failed!')
            sys.exit(1)
    
    def audit(self, message):
        conn = self.connectToDB()
        cur = conn.cursor()

        cur.execute("SELECT user_id FROM users WHERE user_type = 0")
        result = cur.fetchall()

        uid = result[0][0]
        currentTime = datetime.datetime.now()

        query = "INSERT INTO audit(user_id, time, actions_made) VALUES (%s, %s, %s)"
        values = (str(uid), currentTime, str(message))

        cur.execute(query,values)
        conn.commit()