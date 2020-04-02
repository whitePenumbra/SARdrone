import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.AddPilot import addpilotAlt
from Gui.Administrator.AddPilot import UnsavedChangesAlert
import MySQLdb as mdb
from Encryption import AESCipher

class addClass(QtWidgets.QMainWindow, addpilotAlt.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_save.clicked.connect(self.savePilot)

        day=0
        while day < 31:
            self.cmb_day.addItem(str(day + 1))
            day += 1

        monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December']
        self.cmb_month.addItems(monthList)

        year=1970
        while year < 2021:
            self.cmb_year.addItem(str(year))
            year += 1
    
    def cancel(self):
        self.addPopup = addPopupClass(parent=self)
        self.addPopup.exec_()

    def returnToHome(self):
        self.close()
        self.parent.showself()
        self.parent.initializeData()
    
    def savePilot(self):  
        self.insertToDB()

        print('Saved')
        # print(fname + " " + lname + "\n")
        # print(gender + "\n")
        # print(month + " " + day + ", " + year + "\n")
        # print(address + " " + city + " " + province + " " + zipCode + "\n")
        # print(email + " " + mobile+ " " + emContact + " " + emNumber + "\n")
        # print(certNo + " " + operator + " " + issueDate + " " + expire)
        self.returnToHome()

    def connectToDB(self):
        try:
            db = mdb.connect('localhost', 'root', '', 'aids')
            print('Connected successfully!')

        except mdb.Error as e:
            print('Connection failed!')
            sys.exit(1)
    
    def insertToDB(self):
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

        con = mdb.connect('localhost', 'root', '', 'aids')
        cur = con.cursor()

        cur.execute('INSERT INTO address(permanent_address, city, province, zipcode) VALUES'
        '("%s","%s","%s",%s)' % (address, city, province, zipCode))
        con.commit()

        cur.execute('SELECT address_id FROM address WHERE permanent_address = "%s" AND zipcode = %s' % (address,zipCode))
        result = cur.fetchall()

        address_id = 0
        for row in result:
            for i in row:
                address_id = i

        username = fname[0:1] + lname[0:]
        password = lname[0:1] + fname[0:]
        # password = lname

        encpass = AESCipher('aids').encrypt(password)

        cur.execute('INSERT INTO users(address_id, last_name, first_name, username, password, user_type, '
        'license_date, license_expiry, certif_no, emergency_contact, emergency_number, operator, gender, '
        'date_of_birth, email, phone_number) VALUES'
        '("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' 
        % (address_id, lname, fname, username, encpass, 1, 0000-00-00, 0000-00-00, certNo, emContact, emNumber, operator,
        gender, (year + '-' + month + '-' + day), email, mobile))
        con.commit()

class addPopupClass(QtWidgets.QDialog, UnsavedChangesAlert.Ui_Dialog):
    def __init__(self,parent):
        super(QtWidgets.QDialog,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_delete.clicked.connect(self.delete)

    def cancel(self):
        self.close()
    
    def delete(self):
        self.parent.txt_fname.clear()
        self.parent.txt_lname.clear()

        self.parent.txt_address.clear()
        self.parent.txt_province.clear()
        self.parent.txt_city.clear()
        self.parent.txt_zip.clear()

        self.parent.txt_mobile.clear()
        self.parent.txt_emContact.clear()
        self.parent.txt_emNumber.clear()
        self.parent.txt_email.clear()

        self.parent.txt_operator.clear()
        self.parent.txt_certificate.clear()
        self.parent.txt_issueDate.clear()
        self.parent.txt_licenseEx.clear()

        self.close()
        self.parent.returnToHome()