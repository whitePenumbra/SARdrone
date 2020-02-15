import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.AddPilot import addpilotAlt

class addClass(QtWidgets.QMainWindow, addpilotAlt.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_cancel.clicked.connect(self.returnToHome)
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
    
    def returnToHome(self):
        self.close()
        self.parent.showself()
    
    def savePilot(self):
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

        print('Saved')
        print(fname + " " + lname + "\n")
        print(gender + "\n")
        print(month + " " + day + ", " + year + "\n")
        print(address + " " + city + " " + province + " " + zipCode + "\n")
        print(email + " " + mobile+ " " + emContact + " " + emNumber + "\n")
        print(certNo + " " + operator + " " + issueDate + " " + expire)
        self.returnToHome()