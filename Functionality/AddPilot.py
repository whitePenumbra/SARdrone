import sys, datetime, smtplib, ssl, re
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.AddPilot import addpilotAlt, AddPilotSuccess, AddPilotError, UnsavedChangesAlert
from ConnectToDB import connectToDB
from Encryption import AESCipher
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QFileDialog

class addClass(QtWidgets.QMainWindow, addpilotAlt.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.btn_save.setEnabled(False)

        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_save.clicked.connect(self.savePilot)
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

        self.rbtn_female.clicked.connect(self.checkContent)
        self.rbtn_male.clicked.connect(self.checkContent)

        self.txt_zip.setMaxLength(4)
        self.txt_mobile.setMaxLength(11)
        self.txt_emNumber.setMaxLength(11)
        self.txt_address.setMaxLength(255)

        onlyInt = QtGui.QIntValidator()
        self.txt_mobile.setValidator(onlyInt)
        self.txt_emNumber.setValidator(onlyInt)

        rx = QtCore.QRegExp("^[a-zA-Z ]+$")
        letterOnly = QtGui.QRegExpValidator(rx)
        self.txt_fname.setValidator(letterOnly)
        self.txt_lname.setValidator(letterOnly)
        self.txt_emContact.setValidator(letterOnly)
        self.txt_operator.setValidator(letterOnly)

        day=0
        self.cmb_day.addItem('')
        self.cmb_issue_day.addItem('')
        self.cmb_expiry_day.addItem('')
        while day < 31:
            self.cmb_day.addItem(str(day + 1))
            self.cmb_issue_day.addItem(str(day + 1))
            self.cmb_expiry_day.addItem(str(day + 1))
            day += 1

        # self.monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
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

        imageLoc = "../Gui/Resources/profile_placeholder.jpg"
        image = QtGui.QPixmap(imageLoc)
        self.lbl_profilePic.setPixmap(image)

        imageLoc = "../Gui/Resources/profile_placeholder.png"
        image = QtGui.QPixmap(imageLoc)
        self.lbl_profilePic.setPixmap(image)

        self.dbimage = self.convertToBinaryData(imageLoc)
    
    def cancel(self):
        self.btn_cancel.setEnabled(False)
        self.btn_save.setEnabled(False)
        self.disableAll()

        self.addPopup = addPopupClass(parent=self)
        self.addPopup.show()

    def returnToHome(self):
        self.close()
        self.parent.showself()
        self.parent.initializeData()
    
    def savePilot(self):
        self.insertToDB()
        self.sendEmail()

        print('Saved')
        self.returnToHome()

    def connectToDB(self):
        try:
            db = mdb.connect('localhost', 'root', '', 'aids')
            return (db)

        except mdb.Error as e:
            print('Connection failed!')
            sys.exit(1)
    
    def insertToDB(self):
        try:
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
            expire = datetime.datetime.strptime(monthList[self.cmb_expiry_month.currentText()] + self.cmb_expiry_day.currentText() +
                        self.cmb_expiry_year.currentText(), '%m%d%Y').date()

            conn = connectToDB()
            cur = conn.cursor()

            cur.execute('INSERT INTO address(permanent_address, city, province, zipcode) VALUES'
            '("%s","%s","%s",%s)' % (address, city, province, zipCode))
            conn.commit()

            cur.execute('SELECT address_id FROM address WHERE permanent_address = "%s" AND zipcode = %s' % (address,zipCode))
            result = cur.fetchall()

            address_id = 0
            for row in result:
                for i in row:
                    address_id = i

            self.username = fname[0:1] + lname[0:]
            self.password = lname[0:1] + fname[0:]
            # password = lname

            encpass = AESCipher('aids').encrypt(self.password)

            query = """INSERT INTO users(address_id, user_img, last_name, first_name, username, password, user_type, license_date,
            license_expiry, certif_no, emergency_contact, emergency_number, operator, gender, date_of_birth, email, phone_number) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            # values = (address_id, lname, fname, self.username, encpass, 1, issueDate, expire, certNo, emContact, emNumber,
            # operator, gender, birthday, email, mobile)
            values = (str(address_id), self.dbimage, str(lname), str(fname), str(self.username), encpass, 1, issueDate, expire,
            str(certNo), str(emContact), str(emNumber), str(operator), gender, birthday, str(email), str(mobile))

            cur.execute(query, values)
            conn.commit()

            self.addSuccess = addSuccessClass(parent=self)
            self.addSuccess.show()            
        except Exception as e:
            self.addError = addErrorClass(parent=self)
            self.addError.show()

        self.audit("Admin added pilot " + fname + " " + lname)

    def sendEmail(self):
        port = 465
        mypass = (AESCipher('my password').decrypt('oNp8RcyRuLep8XYQ1JOJl57azvNzmeIrQ9pEKp0cIHs=')).decode()
        context = ssl.create_default_context()
        Recipient = self.txt_email.text()

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
                server.login('airbaseddeploymentsystem@gmail.com', mypass)

                msg = MIMEMultipart('alternative')
                msg['Subject'] = 'Test Message'
                msg['To'] = self.txt_email.text()
                message = """
Username: %s
Password: %s
                """ % (self.username, self.password)
                msg.attach(MIMEText(message))

                server.sendmail('airbaseddeploymentsystem@gmail.com', Recipient, msg.as_string())
                server.quit()
                print('Email Sent!')
        except Exception as e:
            print(e)

    def checkEmail(self):
        font = QtGui.QFont()
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        font.setPointSize(10)
        font.setFamily("Helvetica")

        if(re.search(regex, self.txt_email.text())):  
            self.txt_email.setFont(font)
            self.txt_email.setStyleSheet("padding-left: 4px;")
            print("Valid Email")
            return (True)    
        else:  
            print("Invalid Email")
            self.txt_email.setFont(font)
            self.txt_email.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px;}")
            return (False)
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Add Image", "","All Files (*);;Python Files (*.py)", options=options)
        if (fileName):
            print(fileName)
            self.lbl_profilePic.setStyleSheet("border-image:url(fileName);")
            image = QtGui.QPixmap(fileName)
            self.lbl_profilePic.setPixmap(image)

            self.dbimage = self.convertToBinaryData(fileName)
            # print(sys.getsizeof(self.dbimage))

    
    def convertToBinaryData(self, fileName):
        with open(fileName, 'rb') as file:
            binaryData = file.read()
        return(binaryData)
    
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

class addPopupClass(QtWidgets.QMainWindow, UnsavedChangesAlert.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_delete.clicked.connect(self.delete)

    def closeEvent(self, event):
        self.cancel()

    def cancel(self):
        self.parent.btn_save.setEnabled(True)
        self.parent.btn_cancel.setEnabled(True)
        self.parent.enableAll()

        self.close()
    
    def delete(self):
        self.close()
        self.parent.returnToHome()

class addSuccessClass(QtWidgets.QMainWindow, AddPilotSuccess.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.btn_OK.clicked.connect(self.goBack)

    def goBack(self):
        self.close()

class addErrorClass(QtWidgets.QMainWindow, AddPilotError.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.btn_OK.clicked.connect(self.goBack)

    def goBack(self):
        self.close()