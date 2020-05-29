import sys, datetime, smtplib, ssl, re
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from ConnectToDB import connectToDB
from Gui.Pilot.ViewProfile import ViewProfile

class pilotViewClass(QtWidgets.QMainWindow, ViewProfile.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.btn_cancel.clicked.connect(self.goBack)

        self.pilot = self.parent.currentUser[0]
        self.getData()
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

    def getAddress(self,result):
        conn = connectToDB()
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

    def getData(self):
        conn = connectToDB()
        cur = conn.cursor()

        cur.execute('SELECT * FROM users WHERE user_id = %s', (str(self.pilot[0]),))
        result1 = cur.fetchall()

        self.result = result1[0]

    def goBack(self):
        self.close()
        self.parent.show()
