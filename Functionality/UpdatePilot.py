import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.UpdatePilot import UpdatePilotAlt
import MySQLdb as mdb

class updateClass(QtWidgets.QMainWindow, UpdatePilotAlt.Ui_MainWindow):
    def __init__(self,result,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_save.clicked.connect(self.saveUpdate)

        addressTuple = self.parent.getAddress(result)

        day=0
        while day < 31:
            self.cmb_day.addItem(str(day + 1))
            self.cmb_issue_day.addItem(str(day + 1))
            self.cmb_expiry_day.addItem(str(day + 1))
            day += 1

        # monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
        # 'August', 'September', 'October', 'November', 'December']
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
        self.cmb_month.addItems(monthList)
        self.cmb_issue_month.addItems(monthList)
        self.cmb_expiry_month.addItems(monthList)

        year=1970
        while year < 2021:
            self.cmb_year.addItem(str(year))
            self.cmb_issue_year.addItem(str(year))
            self.cmb_expiry_year.addItem(str(year))
            year += 1

        self.uid = result[0]
        self.aid = addressTuple[0][0]

        print('UPDATE PART')
        print(result)
        print(addressTuple)

        for i in addressTuple:
            address = i

        self.txt_fname.setText(result[3])
        self.txt_lname.setText(result[2])
        if (result[13] == 1):
            self.rbtn_male.toggle()
        else:
            self.rbtn_female.toggle()
        # self.lbl_dob.setText(str(result[14]))
        self.txt_address.setText(address[1])
        self.txt_city.setText(address[2])
        self.txt_province.setText(address[3])
        self.txt_zip.setText(address[4])

        self.txt_email.setText(str(result[15]))
        self.txt_mobile.setText(str(result[16]))
        self.txt_emContact.setText(str(result[10]))
        self.txt_emNumber.setText(str(result[11]))

        self.txt_certificate.setText(str(result[9]))
        self.txt_operator.setText(str(result[12]))
        self.txt_issueDate.setText(str(result[7]))
        self.txt_licenseEx.setText(str(result[8]))
    
    def cancel(self):
        self.parent.cancel()
        self.close()

    def saveUpdate(self):
        self.updateData()
        self.parent.cancel()
        self.close()
    
    def updateData(self):
        fname = self.txt_fname.text()
        lname = self.txt_lname.text()

        if (self.rbtn_female.isChecked()):
            gender = self.rbtn_female.text()
        elif (self.rbtn_male.isChecked()):
            gender = self.rbtn_male.text()
        else:
            gender = ''

        month = self.cmb_month.currentText()
        day = self.cmb_day.currentText()
        year = self.cmb_year.currentText()

        address = self.txt_address.text()
        city = self.txt_city.text()
        province = self.txt_province.text()
        zipCode = self.txt_zip.text()

        email = self.txt_email.text()
        mobile = self.txt_mobile.text()
        emContact = self.txt_emContact.text()
        emNumber = self.txt_emNumber.text()

        certNo = self.txt_certificate.text()
        operator = self.txt_operator.text()
        issueDate = self.txt_issueDate.text()
        expire = self.txt_licenseEx.text()

        conn = mdb.connect('localhost', 'root', '', 'aids')
        cur = conn.cursor()

        cur.execute('UPDATE address SET permanent_address = "%s", city = "%s", province = "%s", zipcode="%s"'
        ' WHERE address_id = "%s"' % (address, city, province, zipCode, self.aid))

        cur.execute('UPDATE users SET last_name="%s", first_name="%s", license_date="%s", '
        'license_expiry="%s", certif_no="%s", emergency_contact="%s", emergency_number="%s", '
        'operator="%s", gender="%s", date_of_birth="%s", email="%s", phone_number="%s" WHERE '
        'user_id = "%s"' % (lname, fname, 0000-00-00,0000-00-00, certNo, emContact, emNumber, 
        operator,gender, (year + '-' + month + '-' + day), email, mobile, self.uid))
        
        conn.commit()