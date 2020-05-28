import sys, datetime, re
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.UpdatePilot import UpdatePilotAlt
from Functionality.UpdatePopUps import updateSuccessClass,updateErrorClass,cancelUpdateClass,confirmPopupClass
from Functionality.Test import testClass
from ConnectToDB import connectToDB
from PyQt5.QtWidgets import QFileDialog

class updateClass(QtWidgets.QMainWindow, UpdatePilotAlt.Ui_MainWindow):
    def __init__(self,result,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        
        self.btn_cancel.clicked.connect(self.cancelUpdate)
        self.btn_save.clicked.connect(self.update)
        self.btn_profImg.clicked.connect(self.openFileNameDialog)

        self.txt_fname.editingFinished.connect(self.checkfname)
        self.txt_lname.editingFinished.connect(self.checklname)

        self.txt_address.editingFinished.connect(self.checkAddress)
        self.txt_city.editingFinished.connect(self.checkCity)
        self.txt_province.editingFinished.connect(self.checkProvince)
        self.txt_zip.editingFinished.connect(self.checkZip)

        self.txt_email.editingFinished.connect(self.checkEmail)
        self.txt_mobile.editingFinished.connect(self.checkMobile)
        self.txt_emContact.editingFinished.connect(self.checkEmContact)
        self.txt_emNumber.editingFinished.connect(self.checkEmNumber)

        self.txt_certificate.editingFinished.connect(self.checkCertificate)
        self.txt_operator.editingFinished.connect(self.checkOperator)

        self.cmb_day.currentTextChanged.connect(self.checkContent)
        self.cmb_month.currentTextChanged.connect(self.checkContent)
        self.cmb_year.currentTextChanged.connect(self.checkContent)

        self.cmb_issue_day.currentTextChanged.connect(self.checkContent)
        self.cmb_issue_month.currentTextChanged.connect(self.checkContent)
        self.cmb_issue_year.currentTextChanged.connect(self.checkContent)

        self.cmb_expiry_day.currentTextChanged.connect(self.checkContent)
        self.cmb_expiry_month.currentTextChanged.connect(self.checkContent)
        self.cmb_expiry_year.currentTextChanged.connect(self.checkContent)

        self.txt_address.setMaxLength(255)
        self.txt_zip.setMaxLength(4)
        self.txt_mobile.setMaxLength(11)
        self.txt_emNumber.setMaxLength(11)

        onlyInt = QtGui.QIntValidator()
        self.txt_mobile.setValidator(onlyInt)
        self.txt_emNumber.setValidator(onlyInt)

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

        year=2016
        self.cmb_year.addItem('')
        self.cmb_issue_year.addItem('')
        self.cmb_expiry_year.addItem('')
        while year < 2024:
            self.cmb_issue_year.addItem(str(year))
            self.cmb_expiry_year.addItem(str(year))
            year += 1
        
        birthYear=1970
        while birthYear < 2021:
            self.cmb_year.addItem(str(birthYear))
            birthYear += 1

        self.uid = result[0]
        self.aid = addressTuple[0][0]

        print('UPDATE PART')
        # print(result)
        print(addressTuple)

        for i in addressTuple:
            address = i
        
        self.lbl_profilePic.setStyleSheet("border-image:url(fileName);")
        image_data = result[2]

        image = QtGui.QImage.fromData(image_data)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.lbl_profilePic.setPixmap(pixmap)

        self.txt_fname.setText(result[4])
        self.txt_lname.setText(result[3])

        if (int(result[14]) == 0):
            self.rbtn_female.toggle()
        else:
            self.rbtn_male.toggle()
        self.cmb_month.setCurrentIndex(self.cmb_month.findText(result[15].strftime("%B"),
                                        QtCore.Qt.MatchFixedString))
        self.cmb_day.setCurrentIndex(self.cmb_day.findText(result[15].strftime("%d"),
                                        QtCore.Qt.MatchExactly))
        self.cmb_year.setCurrentIndex(self.cmb_year.findText(result[15].strftime("%Y"),
                                        QtCore.Qt.MatchFixedString))
        self.txt_address.setText(address[1])
        self.txt_city.setText(address[2])
        self.txt_province.setText(address[3])
        self.txt_zip.setText(address[4])

        self.txt_email.setText(str(result[16]))
        self.txt_mobile.setText(str(result[17]))
        self.txt_emContact.setText(str(result[11]))
        self.txt_emNumber.setText(str(result[12]))

        self.txt_certificate.setText(str(result[10]))
        self.txt_operator.setText(str(result[13]))
        self.cmb_issue_month.setCurrentIndex(self.cmb_issue_month.findText(result[8].strftime("%B"),
                                            QtCore.Qt.MatchFixedString))
        self.cmb_issue_day.setCurrentIndex(self.cmb_issue_day.findText(result[8].strftime('%d'),
                                            QtCore.Qt.MatchFixedString))
        self.cmb_issue_year.setCurrentIndex(self.cmb_issue_year.findText(result[8].strftime("%Y"),
                                            QtCore.Qt.MatchFixedString))
        self.cmb_expiry_month.setCurrentIndex(self.cmb_expiry_month.findText(result[9].strftime("%B"),
                                            QtCore.Qt.MatchFixedString))
        self.cmb_expiry_day.setCurrentIndex(self.cmb_expiry_day.findText(result[9].strftime('%d'),
                                            QtCore.Qt.MatchFixedString))
        self.cmb_expiry_year.setCurrentIndex(self.cmb_expiry_year.findText(result[9].strftime("%Y"),
                                            QtCore.Qt.MatchFixedString))
        
        print(result[9].strftime('%d'))
    
    def update(self):
        self.disableAll()

        self.updateClass = confirmPopupClass(parent=self)
        self.updateClass.show()
    
    def returnToView(self):
        self.close()
        self.parent.show()

    def saveUpdate(self):
        try:
            self.updateData()

            self.updateSuccess = updateSuccessClass(parent=self)
            self.updateSuccess.show()
        except Exception as e:
            print(e)
            self.updateError = updateErrorClass(parent=self)
            self.updateError.show()

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

        conn = connectToDB()
        cur = conn.cursor()

        cur.execute('UPDATE address SET permanent_address = "%s", city = "%s", province = "%s", zipcode="%s"'
        ' WHERE address_id = "%s"' % (address, city, province, zipCode, self.aid))

        cur.execute('UPDATE users SET last_name="%s", first_name="%s", license_date="%s", '
        'license_expiry="%s", certif_no="%s", emergency_contact="%s", emergency_number="%s", '
        'operator="%s", gender="%s", date_of_birth="%s", email="%s", phone_number="%s" WHERE '
        'user_id = "%s"' % (lname, fname, issueDate, expiry, certNo, emContact, emNumber, 
        operator,gender, birthday, email, mobile, self.uid))
        
        conn.commit()
        self.audit("Admin updated pilot " + fname + " " + lname + "'s information.")

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Change Image", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.lbl_profilePic.setStyleSheet("border-image:url(fileName);")
            image = QtGui.QPixmap(fileName)
            self.lbl_profilePic.setPixmap(image)
    
    def disableAll(self):
        self.txt_fname.setReadOnly(True)
        self.txt_lname.setReadOnly(True)

        self.txt_address.setReadOnly(True)
        self.txt_city.setReadOnly(True)
        self.txt_province.setReadOnly(True)
        self.txt_zip.setReadOnly(True)

        self.txt_email.setReadOnly(True)
        self.txt_mobile.setReadOnly(True)
        self.txt_emContact.setReadOnly(True)
        self.txt_emNumber.setReadOnly(True)

        self.txt_certificate.setReadOnly(True)
        self.txt_operator.setReadOnly(True)

        self.cmb_day.setEnabled(False)
        self.cmb_month.setEnabled(False)
        self.cmb_year.setEnabled(False)

        self.cmb_expiry_day.setEnabled(False)
        self.cmb_expiry_month.setEnabled(False)
        self.cmb_expiry_year.setEnabled(False)

        self.cmb_issue_day.setEnabled(False)
        self.cmb_issue_month.setEnabled(False)
        self.cmb_issue_year.setEnabled(False)

        self.btn_profImg.setEnabled(False)
        self.btn_save.setEnabled(False)
        self.btn_cancel.setEnabled(False)
    
    def enableAll(self):
        self.txt_fname.setReadOnly(False)
        self.txt_lname.setReadOnly(False)

        self.txt_address.setReadOnly(False)
        self.txt_city.setReadOnly(False)
        self.txt_province.setReadOnly(False)
        self.txt_zip.setReadOnly(False)

        self.txt_email.setReadOnly(False)
        self.txt_mobile.setReadOnly(False)
        self.txt_emContact.setReadOnly(False)
        self.txt_emNumber.setReadOnly(False)

        self.txt_certificate.setReadOnly(False)
        self.txt_operator.setReadOnly(False)

        self.cmb_day.setEnabled(True)
        self.cmb_month.setEnabled(True)
        self.cmb_year.setEnabled(True)

        self.cmb_expiry_day.setEnabled(True)
        self.cmb_expiry_month.setEnabled(True)
        self.cmb_expiry_year.setEnabled(True)

        self.cmb_issue_day.setEnabled(True)
        self.cmb_issue_month.setEnabled(True)
        self.cmb_issue_year.setEnabled(True)

        self.btn_profImg.setEnabled(True)
        self.btn_save.setEnabled(True)
        self.btn_cancel.setEnabled(True)

    def cancelUpdate(self):
        self.disableAll()

        self.cancelUpdate = cancelUpdateClass(parent=self)
        self.cancelUpdate.show()

        # self.testclass = testClass(parent=self)
        # self.testclass.show()
    
    def audit(self, message):
        conn = connectToDB()
        cur = conn.cursor()

        cur.execute("SELECT user_id FROM users WHERE user_type = 0")
        result = cur.fetchall()

        uid = result[0][0]
        currentTime = datetime.datetime.now()

        query = "INSERT INTO audit(user_id, time, actions_made) VALUES (%s, %s, %s)"
        values = (str(uid), currentTime, str(message))

        cur.execute(query,values)
        conn.commit()

    def checkfname(self):
        if (self.txt_fname.text() == ''):
            self.txt_fname.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
        else:
            self.txt_fname.setStyleSheet("padding-left: 4px;")
        
        self.checkContent()

    def checklname(self):
        if (self.txt_lname.text() == ''):
            self.txt_lname.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
        else:
            self.txt_lname.setStyleSheet("padding-left: 4px;")
        
        self.checkContent()
    
    def checkAddress(self):
        if (self.txt_address.text() == '' ):
            self.txt_address.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
        else:
            self.txt_address.setStyleSheet("padding-left: 4px;")
        
        self.checkContent()

    def checkCity(self):
        if (self.txt_city.text() == ''):
            self.txt_city.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
        else:
            self.txt_city.setStyleSheet("padding-left: 4px;")

        self.checkContent()

    def checkProvince(self):
        if (self.txt_province.text() == ''):
            self.txt_province.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
        else:
            self.txt_province.setStyleSheet("padding-left: 4px;")
        
        self.checkContent()

    def checkZip(self):
        if (self.txt_zip.text() == ''):
           self.txt_zip.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
        else:
            self.txt_zip.setStyleSheet("padding-left: 4px;")
        
        self.checkContent()
    
    def checkEmail(self):
        font = QtGui.QFont()
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        font.setPointSize(10)
        font.setFamily("Helvetica")

        if(re.search(regex, self.txt_email.text())):  
            self.txt_email.setFont(font)
            self.txt_email.setStyleSheet("padding-left: 4px;")
            print("Valid Email")
            self.btn_save.setEnabled(True)        
        else:  
            print("Invalid Email")
            self.txt_email.setFont(font)
            self.txt_email.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px;}")
            self.btn_save.setEnabled(False)

        if (self.txt_email.text() == ''):
            self.txt_email.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px;}")
        else:
            self.txt_email.setStyleSheet("padding-left: 4px;")
        
        self.checkContent()

    def checkMobile(self):
        if (self.txt_mobile.text() == ''):
            self.txt_mobile.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
        else:
            self.txt_mobile.setStyleSheet("padding-left: 4px;")

        self.checkContent()

    def checkEmContact(self):
        if (self.txt_emContact.text() == ''):
            self.txt_emContact.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
        else:
            self.txt_emContact.setStyleSheet("padding-left: 4px;")
        
        self.checkContent()

    def checkEmNumber(self):
        if (self.txt_emNumber.text() == ''):
            self.txt_emNumber.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
        else:
            self.txt_emNumber.setStyleSheet("padding-left: 4px;")

            self.checkContent()
    
    def checkCertificate(self):
        if (self.txt_certificate.text() == ''):
            self.txt_certificate.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
        else:
            self.txt_certificate.setStyleSheet("padding-left: 4px;")
        
        self.checkContent()

    def checkOperator(self):
        if (self.txt_operator.text() == ''): 
            self.txt_operator.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px}")
        else:
            self.txt_operator.setStyleSheet("padding-left: 4px;")

            self.checkContent()
    
    def checkContent(self):
        if (self.txt_fname.text() == '' or self.txt_lname.text() == ''
        or self.txt_address.text() == '' or self.txt_city.text() == '' 
        or self.txt_province.text() == '' or self.txt_zip.text() == '' 
        or self.txt_email.text() == '' or self.txt_mobile.text() == '' 
        or self.txt_emContact.text() == '' or self.txt_emNumber.text() == ''
        or self.txt_certificate.text() == '' or self.txt_operator.text() == ''
        or self.cmb_day.currentText() == '' or self.cmb_month.currentText() == ''
        or self.cmb_year.currentText() == '' or self.cmb_issue_day.currentText() == ''
        or self.cmb_issue_month.currentText() == '' or self.cmb_issue_year.currentText() == ''
        or self.cmb_expiry_day.currentText() == '' or self.cmb_expiry_month.currentText() == ''
        or self.cmb_expiry_year.currentText() == '' or not(self.rbtn_male.isChecked() or self.rbtn_female.isChecked())):
            self.btn_save.setEnabled(False)
        else:
            self.btn_save.setEnabled(True)