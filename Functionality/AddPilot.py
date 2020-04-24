import sys, datetime, smtplib, ssl, re
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.AddPilot import addpilotAlt
from Gui.Administrator.AddPilot import UnsavedChangesAlert
import MySQLdb as mdb
from Encryption import AESCipher
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QFileDialog

class addClass(QtWidgets.QMainWindow, addpilotAlt.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        # self.btn_save.setEnabled(False)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_save.clicked.connect(self.savePilot)
        self.btn_profImg.clicked.connect(self.openFileNameDialog)

        self.txt_zip.setMaxLength(4)
        self.txt_address.setMaxLength(255)

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

        year=1970
        self.cmb_year.addItem('')
        self.cmb_issue_year.addItem('')
        self.cmb_expiry_year.addItem('')
        while year < 2021:
            self.cmb_year.addItem(str(year))
            self.cmb_issue_year.addItem(str(year))
            self.cmb_expiry_year.addItem(str(year))
            year += 1

        imageLoc = "../Gui/Resources/profile_placeholder.jpg"
        image = QtGui.QPixmap(imageLoc)
        self.lbl_profilePic.setPixmap(image)

        # self.txt_mobile.setValidator(QIntValidator())
        # self.txt_emNumber.setValidator(QIntValidator())
        self.txt_email.editingFinished.connect(self.checkEmail)

        imageLoc = "../Gui/Resources/profile_placeholder.png"
        image = QtGui.QPixmap(imageLoc)
        self.lbl_profilePic.setPixmap(image)

        self.dbimage = self.convertToBinaryData(imageLoc)
    
    def cancel(self):
        self.addPopup = addPopupClass(parent=self)
        self.addPopup.exec_()

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

        conn = self.connectToDB()
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
        self.audit("Admin added pilot " + fname + " " + lname)

    def sendEmail(self):
        port = 465
        mypass = (AESCipher('my password').decrypt('30hLaA3Uc12BkhQC2i4ZLjrlxqHAGkeJkedXOB2QdIU=')).decode()
        context = ssl.create_default_context()
        Recipient = self.txt_email.text()

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
                server.login('loztestcode@gmail.com', mypass)

                msg = MIMEMultipart('alternative')
                msg['Subject'] = 'Test Message'
                msg['To'] = self.txt_email.text()
                message = """
Username: %s
Password: %s
                """ % (self.username, self.password)
                msg.attach(MIMEText(message))

                server.sendmail('loztestcode.gmail.com', Recipient, msg.as_string())
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
            self.btn_save.setEnabled(True)        
        else:  
            print("Invalid Email")
            self.txt_email.setFont(font)
            self.txt_email.setStyleSheet("QLineEdit {\nborder: 1.2px solid red; padding-left: 4px;}")
            self.btn_save.setEnabled(False)
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
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
        self.close()
        self.parent.returnToHome()