import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.UpdatePilot import UpdatePilotAlt
from Gui.Administrator.UpdatePilot import UpdatePilotConfirm
import MySQLdb as mdb
import datetime

class updateClass(QtWidgets.QMainWindow, UpdatePilotAlt.Ui_MainWindow):
    def __init__(self,result,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_cancel.clicked.connect(self.returnToView)
        self.btn_save.clicked.connect(self.update)

        self.txt_address.setMaxLength(255)
        self.txt_zip.setMaxLength(4)

        addressTuple = self.parent.getAddress(result)

        dayList = [
            '01',
            '02',
            '03',
            '04',
            '05',
            '06',
            '07',
            '08',
            '09'
        ]
        self.cmb_day.addItems(dayList)
        self.cmb_issue_day.addItems(dayList)
        self.cmb_expiry_day.addItems(dayList)

        day=10
        while day <= 31:
            self.cmb_day.addItem(str(day))
            self.cmb_issue_day.addItem(str(day))
            self.cmb_expiry_day.addItem(str(day))
            day += 1

        # monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
        # 'August', 'September', 'October', 'November', 'December']
        monthList = [
            '',
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
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
        self.cmb_month.setCurrentIndex(self.cmb_month.findText(result[14].strftime("%B"),
                                        QtCore.Qt.MatchFixedString))
        self.cmb_day.setCurrentIndex(self.cmb_day.findText(result[14].strftime("%d"),
                                        QtCore.Qt.MatchExactly))
        self.cmb_year.setCurrentIndex(self.cmb_year.findText(result[14].strftime("%Y"),
                                        QtCore.Qt.MatchFixedString))
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
        self.cmb_issue_month.setCurrentIndex(self.cmb_issue_month.findText(result[7].strftime("%B"),
                                            QtCore.Qt.MatchFixedString))
        self.cmb_issue_day.setCurrentIndex(self.cmb_issue_day.findText(result[7].strftime('%d'),
                                            QtCore.Qt.MatchFixedString))
        self.cmb_issue_year.setCurrentIndex(self.cmb_issue_year.findText(result[7].strftime("%Y"),
                                            QtCore.Qt.MatchFixedString))
        self.cmb_expiry_month.setCurrentIndex(self.cmb_expiry_month.findText(result[8].strftime("%B"),
                                            QtCore.Qt.MatchFixedString))
        self.cmb_expiry_day.setCurrentIndex(self.cmb_expiry_day.findText(result[8].strftime('%d'),
                                            QtCore.Qt.MatchFixedString))
        self.cmb_expiry_year.setCurrentIndex(self.cmb_expiry_year.findText(result[8].strftime("%Y"),
                                            QtCore.Qt.MatchFixedString))
        
        print(result[8].strftime('%d'))
    
    def update(self):
        self.updateClass = confirmPopupClass(parent=self)
        self.updateClass.exec_()
    
    def returnToView(self):
        self.close()
        self.parent.show()

    def saveUpdate(self):
        self.updateData()
        self.parent.cancel()
        self.close()
    
    def updateData(self):
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

        fname = self.txt_fname.text()
        lname = self.txt_lname.text()

        if (self.rbtn_female.isChecked()):
            gender = 0
        elif (self.rbtn_male.isChecked()):
            gender = 1
        else:
            gender = ''

        month = self.cmb_month.currentText()
        day = self.cmb_day.currentText()
        year = self.cmb_year.currentText()
        birthday = datetime.datetime.strptime(monthList[month] + day + year, '%m%d%Y').date()

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
        issueDate = datetime.datetime.strptime(monthList[self.cmb_issue_month.currentText()] + self.cmb_issue_day.currentText() +
                    self.cmb_issue_year.currentText(), '%m%d%Y').date()
        expiry = datetime.datetime.strptime(monthList[self.cmb_expiry_month.currentText()] + self.cmb_expiry_day.currentText() +
                    self.cmb_expiry_year.currentText(), '%m%d%Y').date()

        conn = mdb.connect('localhost', 'root', '', 'aids')
        cur = conn.cursor()

        cur.execute('UPDATE address SET permanent_address = "%s", city = "%s", province = "%s", zipcode="%s"'
        ' WHERE address_id = "%s"' % (address, city, province, zipCode, self.aid))

        cur.execute('UPDATE users SET last_name="%s", first_name="%s", license_date="%s", '
        'license_expiry="%s", certif_no="%s", emergency_contact="%s", emergency_number="%s", '
        'operator="%s", gender="%s", date_of_birth="%s", email="%s", phone_number="%s" WHERE '
        'user_id = "%s"' % (lname, fname, issueDate, expiry, certNo, emContact, emNumber, 
        operator,gender, birthday, email, mobile, self.uid))
        
        conn.commit()
    
class confirmPopupClass(QtWidgets.QDialog, UpdatePilotConfirm.Ui_Dialog):
    def __init__(self,parent):
        super(QtWidgets.QDialog,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.pushButton_2.clicked.connect(self.save)
        self.pushButton.clicked.connect(self.cancel)
        self.pushButton_3.clicked.connect(self.delete)

    def cancel(self):
        self.close()
    
    def delete(self):
        self.close()
        self.parent.returnToView()
    
    def save(self):
        self.close()
        self.parent.saveUpdate()