# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPilotAlt.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 739)
        MainWindow.setMinimumSize(QtCore.QSize(1071, 739))
        MainWindow.setMaximumSize(QtCore.QSize(1071, 739))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setKerning(True)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Gui/Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_addPilot = QtWidgets.QLabel(self.centralwidget)
        self.lbl_addPilot.setGeometry(QtCore.QRect(20, 24, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(29)
        font.setKerning(True)
        self.lbl_addPilot.setFont(font)
        self.lbl_addPilot.setStyleSheet("padding-bottom: 4px;\n"
                "padding-right:4px;\n"
                "")
        self.lbl_addPilot.setObjectName("lbl_addPilot")
        self.lbl_caap = QtWidgets.QLabel(self.centralwidget)
        self.lbl_caap.setGeometry(QtCore.QRect(20, 530, 381, 35))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(19)
        font.setKerning(True)
        self.lbl_caap.setFont(font)
        self.lbl_caap.setStyleSheet("padding-left:3px;")
        self.lbl_caap.setObjectName("lbl_caap")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 230, 761, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 510, 771, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(30, 370, 761, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lbl_profilePic = QtWidgets.QLabel(self.centralwidget)
        self.lbl_profilePic.setGeometry(QtCore.QRect(830, 30, 191, 181))
        self.lbl_profilePic.setMinimumSize(QtCore.QSize(191, 181))
        self.lbl_profilePic.setMaximumSize(QtCore.QSize(191, 181))
        self.lbl_profilePic.setText("")
        self.lbl_profilePic.setPixmap(QtGui.QPixmap("../Gui/Resources/profile_placeholder.png"))
        self.lbl_profilePic.setScaledContents(True)
        self.lbl_profilePic.setObjectName("lbl_profilePic")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(730, 682, 331, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_cancel.setMinimumSize(QtCore.QSize(131, 31))
        self.btn_cancel.setMaximumSize(QtCore.QSize(131, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("QPushButton {\n"
                "color: rgb(0, 0, 0);\n"
                "    background-color: rgb(202, 202, 202);\n"
                "border: 1.2px solid #ABABAB;\n"
                "outline: none;}\n"
                "\n"
                "QPushButton:hover{\n"
                "color: rgb(255, 255, 255);\n"
                "background-color: rgb(171, 171, 171);\n"
                "outline: none;\n"
                "border: none;\n"
                "}\n"
                "\n"
                "QPushButton:pressed{\n"
                "color: rgb(255, 255, 255);\n"
                "background-color: rgb(129, 129, 129);\n"
                "outline: none;\n"
                "border: none;\n"
                "}\n"
                "\n"
                "\n"
                "")
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.btn_save = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_save.setMinimumSize(QtCore.QSize(131, 31))
        self.btn_save.setMaximumSize(QtCore.QSize(131, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("QPushButton {\n"
                "background-color: rgb(255, 176, 6);\n"
                "border: 1.2px solid #ff9d07;\n"
                "outline: none;}\n"
                "\n"
                "QPushButton:hover{\n"
                "background-color: rgb(255, 157, 7);\n"
                "outline: none;\n"
                "border: none;\n"
                "}\n"
                "\n"
                "QPushButton:pressed{\n"
                "background-color: rgb(254, 140, 8);\n"
                "outline: none;\n"
                "border: none;\n"
                "}\n"
                "\n"
                "\n"
                "")
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(370, 140, 311, 33))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.lname_layout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.lname_layout.setContentsMargins(0, 0, 0, 0)
        self.lname_layout.setObjectName("lname_layout")
        self.lbl_Lname = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_Lname.setFont(font)
        self.lbl_Lname.setStyleSheet("")
        self.lbl_Lname.setObjectName("lbl_Lname")
        self.lname_layout.addWidget(self.lbl_Lname)
        self.txt_lname = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_lname.setMinimumSize(QtCore.QSize(211, 31))
        self.txt_lname.setMaximumSize(QtCore.QSize(211, 31))
        font.setKerning(True)
        self.txt_lname.setFont(font)
        self.txt_lname.setStyleSheet("padding-left:4px;")
        self.txt_lname.setObjectName("txt_lname")
        self.lname_layout.addWidget(self.txt_lname)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 140, 311, 33))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.fname_layout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.fname_layout.setContentsMargins(0, 0, 0, 0)
        self.fname_layout.setObjectName("fname_layout")
        self.lbl_fName = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lbl_fName.setFont(font)
        self.lbl_fName.setStyleSheet("padding-left: 1px;\n"
                "")
        self.lbl_fName.setObjectName("lbl_fName")
        self.fname_layout.addWidget(self.lbl_fName)
        self.txt_fname = QtWidgets.QLineEdit(self.layoutWidget2)
        self.txt_fname.setMinimumSize(QtCore.QSize(211, 31))
        self.txt_fname.setMaximumSize(QtCore.QSize(211, 31))
        font.setKerning(True)
        self.txt_fname.setFont(font)
        self.txt_fname.setStyleSheet("padding-left:4px;")
        self.txt_fname.setObjectName("txt_fname")
        self.fname_layout.addWidget(self.txt_fname)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 190, 311, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gender_layout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.gender_layout.setContentsMargins(0, 0, 0, 0)
        self.gender_layout.setObjectName("gender_layout")
        self.lbl_gender = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_gender.setFont(font)
        self.lbl_gender.setStyleSheet("padding-left:1px;")
        self.lbl_gender.setObjectName("lbl_gender")
        self.gender_layout.addWidget(self.lbl_gender)
        self.rbtn_male = QtWidgets.QRadioButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.rbtn_male.setFont(font)
        self.rbtn_male.setStyleSheet("")
        self.rbtn_male.setObjectName("rbtn_male")
        self.gender_layout.addWidget(self.rbtn_male)
        self.rbtn_female = QtWidgets.QRadioButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.rbtn_female.setFont(font)
        self.rbtn_female.setObjectName("rbtn_female")
        self.gender_layout.addWidget(self.rbtn_female)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(370, 190, 311, 41))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.dob_layout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.dob_layout.setContentsMargins(0, 0, 0, 0)
        self.dob_layout.setObjectName("dob_layout")
        self.lbl_dob = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_dob.setFont(font)
        self.lbl_dob.setStyleSheet("")
        self.lbl_dob.setObjectName("lbl_dob")
        self.dob_layout.addWidget(self.lbl_dob)
        self.cmb_month = QtWidgets.QComboBox(self.layoutWidget4)
        self.cmb_month.setObjectName("cmb_month")
        self.dob_layout.addWidget(self.cmb_month)
        self.cmb_day = QtWidgets.QComboBox(self.layoutWidget4)
        self.cmb_day.setObjectName("cmb_day")
        self.dob_layout.addWidget(self.cmb_day)
        self.cmb_year = QtWidgets.QComboBox(self.layoutWidget4)
        self.cmb_year.setObjectName("cmb_year")
        self.dob_layout.addWidget(self.cmb_year)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(30, 260, 651, 33))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.address_layout = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.address_layout.setContentsMargins(0, 0, 0, 0)
        self.address_layout.setObjectName("address_layout")
        self.lbl_address = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_address.setFont(font)
        self.lbl_address.setStyleSheet("")
        self.lbl_address.setObjectName("lbl_address")
        self.address_layout.addWidget(self.lbl_address)
        self.txt_address = QtWidgets.QLineEdit(self.layoutWidget5)
        self.txt_address.setMinimumSize(QtCore.QSize(491, 31))
        self.txt_address.setMaximumSize(QtCore.QSize(491, 31))
        font.setKerning(True)
        self.txt_address.setFont(font)
        self.txt_address.setStyleSheet("padding-left:4px;")
        self.txt_address.setObjectName("txt_address")
        self.address_layout.addWidget(self.txt_address)
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(30, 320, 201, 33))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.city_layout = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.city_layout.setContentsMargins(0, 0, 0, 0)
        self.city_layout.setObjectName("city_layout")
        self.lbl_city = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_city.setFont(font)
        self.lbl_city.setStyleSheet("")
        self.lbl_city.setObjectName("lbl_city")
        self.city_layout.addWidget(self.lbl_city)
        self.txt_city = QtWidgets.QLineEdit(self.layoutWidget6)
        self.txt_city.setMinimumSize(QtCore.QSize(141, 31))
        self.txt_city.setMaximumSize(QtCore.QSize(141, 31))
        font.setKerning(True)
        self.txt_city.setFont(font)
        self.txt_city.setStyleSheet("padding-left:4px;")
        self.txt_city.setObjectName("txt_city")
        self.city_layout.addWidget(self.txt_city)
        self.layoutWidget7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(260, 320, 241, 33))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.province_layout = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.province_layout.setContentsMargins(0, 0, 0, 0)
        self.province_layout.setObjectName("province_layout")
        self.lbl_province = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_province.setFont(font)
        self.lbl_province.setStyleSheet("")
        self.lbl_province.setObjectName("lbl_province")
        self.province_layout.addWidget(self.lbl_province)
        self.txt_province = QtWidgets.QLineEdit(self.layoutWidget7)
        self.txt_province.setMinimumSize(QtCore.QSize(171, 31))
        self.txt_province.setMaximumSize(QtCore.QSize(171, 31))
        font.setKerning(True)
        self.txt_province.setFont(font)
        self.txt_province.setStyleSheet("padding-left:4px;")
        self.txt_province.setObjectName("txt_province")
        self.province_layout.addWidget(self.txt_province)
        self.layoutWidget8 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget8.setGeometry(QtCore.QRect(530, 320, 151, 33))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.zip_layout = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.zip_layout.setContentsMargins(0, 0, 0, 0)
        self.zip_layout.setObjectName("zip_layout")
        self.lbl_zip = QtWidgets.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_zip.setFont(font)
        self.lbl_zip.setStyleSheet("")
        self.lbl_zip.setObjectName("lbl_zip")
        self.zip_layout.addWidget(self.lbl_zip)
        self.txt_zip = QtWidgets.QLineEdit(self.layoutWidget8)
        self.txt_zip.setMinimumSize(QtCore.QSize(71, 31))
        self.txt_zip.setMaximumSize(QtCore.QSize(71, 31))
        font.setKerning(True)
        self.txt_zip.setFont(font)
        self.txt_zip.setStyleSheet("padding-left:4px;")
        self.txt_zip.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txt_zip.setText("")
        #set max length and accept only integers
        self.txt_zip.setMaxLength(4)
        onlyInt = QtGui.QIntValidator()
        self.txt_zip.setValidator(onlyInt)
        self.txt_zip.setObjectName("txt_zip")
        self.zip_layout.addWidget(self.txt_zip)
        self.layoutWidget9 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget9.setGeometry(QtCore.QRect(31, 401, 361, 33))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.email_layout = QtWidgets.QHBoxLayout(self.layoutWidget9)
        self.email_layout.setContentsMargins(0, 0, 0, 0)
        self.email_layout.setObjectName("email_layout")
        self.lbl_email = QtWidgets.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_email.setFont(font)
        self.lbl_email.setStyleSheet("")
        self.lbl_email.setObjectName("lbl_email")
        self.email_layout.addWidget(self.lbl_email)
        self.txt_email = QtWidgets.QLineEdit(self.layoutWidget9)
        self.txt_email.setMinimumSize(QtCore.QSize(251, 31))
        self.txt_email.setMaximumSize(QtCore.QSize(251, 31))
        font.setKerning(True)
        self.txt_email.setFont(font)
        self.txt_email.setStyleSheet("padding-left:4px;\n"
                "margin-left:6px;")
        self.txt_email.setObjectName("txt_email")
        self.email_layout.addWidget(self.txt_email)
        self.layoutWidget10 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget10.setGeometry(QtCore.QRect(420, 400, 341, 33))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.mobile_layout = QtWidgets.QHBoxLayout(self.layoutWidget10)
        self.mobile_layout.setContentsMargins(0, 0, 0, 0)
        self.mobile_layout.setObjectName("mobile_layout")
        self.lbl_mobile = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_mobile.setFont(font)
        self.lbl_mobile.setStyleSheet("")
        self.lbl_mobile.setObjectName("lbl_mobile")
        self.mobile_layout.addWidget(self.lbl_mobile)
        self.txt_mobile = QtWidgets.QLineEdit(self.layoutWidget10)
        self.txt_mobile.setMinimumSize(QtCore.QSize(191, 31))
        self.txt_mobile.setMaximumSize(QtCore.QSize(191, 31))
        font.setKerning(True)
        self.txt_mobile.setFont(font)
        self.txt_mobile.setStyleSheet("padding-left:4px;\n"
                "margin-left:1px;")
        self.txt_zip.setMaxLength(11)
        self.txt_mobile.setObjectName("txt_mobile")
        self.mobile_layout.addWidget(self.txt_mobile)
        self.layoutWidget11 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget11.setGeometry(QtCore.QRect(30, 470, 361, 33))
        self.layoutWidget11.setObjectName("layoutWidget11")
        self.emcontact_layout = QtWidgets.QHBoxLayout(self.layoutWidget11)
        self.emcontact_layout.setContentsMargins(0, 0, 0, 0)
        self.emcontact_layout.setObjectName("emcontact_layout")
        self.lbl_emContact = QtWidgets.QLabel(self.layoutWidget11)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_emContact.setFont(font)
        self.lbl_emContact.setStyleSheet("")
        self.lbl_emContact.setObjectName("lbl_emContact")
        self.emcontact_layout.addWidget(self.lbl_emContact)
        self.txt_emContact = QtWidgets.QLineEdit(self.layoutWidget11)
        self.txt_emContact.setMinimumSize(QtCore.QSize(231, 31))
        self.txt_emContact.setMaximumSize(QtCore.QSize(231, 31))
        font.setKerning(True)
        self.txt_emContact.setFont(font)
        self.txt_emContact.setStyleSheet("padding-left:4px;")
        self.txt_emContact.setObjectName("txt_emContact")
        self.emcontact_layout.addWidget(self.txt_emContact)
        self.layoutWidget12 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget12.setGeometry(QtCore.QRect(420, 470, 343, 33))
        self.layoutWidget12.setObjectName("layoutWidget12")
        self.emmobile_layout = QtWidgets.QHBoxLayout(self.layoutWidget12)
        self.emmobile_layout.setContentsMargins(0, 0, 0, 0)
        self.emmobile_layout.setObjectName("emmobile_layout")
        self.lbl_emNumber = QtWidgets.QLabel(self.layoutWidget12)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_emNumber.setFont(font)
        self.lbl_emNumber.setObjectName("lbl_emNumber")
        self.emmobile_layout.addWidget(self.lbl_emNumber)
        self.txt_emNumber = QtWidgets.QLineEdit(self.layoutWidget12)
        self.txt_emNumber.setMinimumSize(QtCore.QSize(191, 31))
        self.txt_emNumber.setMaximumSize(QtCore.QSize(191, 31))
        font.setKerning(True)
        self.txt_emNumber.setFont(font)
        self.txt_emNumber.setStyleSheet("padding-left:4px;")
        self.txt_emNumber.setMaxLength(11)
        self.txt_emNumber.setObjectName("txt_emNumber")
        self.emmobile_layout.addWidget(self.txt_emNumber)
        self.layoutWidget13 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget13.setGeometry(QtCore.QRect(30, 580, 361, 33))
        self.layoutWidget13.setObjectName("layoutWidget13")
        self.certno_layout = QtWidgets.QHBoxLayout(self.layoutWidget13)
        self.certno_layout.setContentsMargins(0, 0, 0, 0)
        self.certno_layout.setObjectName("certno_layout")
        self.lbl_certificate = QtWidgets.QLabel(self.layoutWidget13)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_certificate.setFont(font)
        self.lbl_certificate.setStyleSheet("")
        self.lbl_certificate.setObjectName("lbl_certificate")
        self.certno_layout.addWidget(self.lbl_certificate)
        self.txt_certificate = QtWidgets.QLineEdit(self.layoutWidget13)
        self.txt_certificate.setMinimumSize(QtCore.QSize(241, 31))
        self.txt_certificate.setMaximumSize(QtCore.QSize(241, 31))
        font.setKerning(True)
        self.txt_certificate.setFont(font)
        self.txt_certificate.setStyleSheet("padding-left:4px;")
        self.txt_certificate.setObjectName("txt_certificate")
        self.certno_layout.addWidget(self.txt_certificate)
        self.layoutWidget14 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget14.setGeometry(QtCore.QRect(420, 580, 341, 33))
        self.layoutWidget14.setObjectName("layoutWidget14")
        self.operator_layout = QtWidgets.QHBoxLayout(self.layoutWidget14)
        self.operator_layout.setContentsMargins(0, 0, 0, 0)
        self.operator_layout.setObjectName("operator_layout")
        self.lbl_operator = QtWidgets.QLabel(self.layoutWidget14)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_operator.setFont(font)
        self.lbl_operator.setStyleSheet("")
        self.lbl_operator.setObjectName("lbl_operator")
        self.operator_layout.addWidget(self.lbl_operator)
        self.txt_operator = QtWidgets.QLineEdit(self.layoutWidget14)
        self.txt_operator.setMinimumSize(QtCore.QSize(241, 31))
        self.txt_operator.setMaximumSize(QtCore.QSize(241, 31))
        font.setKerning(True)
        self.txt_operator.setFont(font)
        self.txt_operator.setStyleSheet("padding-left:4px;")
        self.txt_operator.setObjectName("txt_operator")
        self.operator_layout.addWidget(self.txt_operator)
        self.layoutWidget15 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget15.setGeometry(QtCore.QRect(30, 630, 340, 33))
        self.layoutWidget15.setObjectName("layoutWidget15")
        self.issuedate_layout = QtWidgets.QHBoxLayout(self.layoutWidget15)
        self.issuedate_layout.setContentsMargins(0, 0, 0, 0)
        self.issuedate_layout.setObjectName("issuedate_layout")
        self.lbl_licenseIssue = QtWidgets.QLabel(self.layoutWidget15)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_licenseIssue.setFont(font)
        self.lbl_licenseIssue.setStyleSheet("")
        self.lbl_licenseIssue.setObjectName("lbl_licenseIssue")
        self.issuedate_layout.addWidget(self.lbl_licenseIssue)
        self.cmb_issue_month = QtWidgets.QComboBox(self.layoutWidget15)
        self.cmb_issue_month.setObjectName("cmb_issue_month")
        self.issuedate_layout.addWidget(self.cmb_issue_month)
        self.cmb_issue_day = QtWidgets.QComboBox(self.layoutWidget15)
        self.cmb_issue_day.setObjectName("cmb_issue_day")
        self.issuedate_layout.addWidget(self.cmb_issue_day)
        self.cmb_issue_year = QtWidgets.QComboBox(self.layoutWidget15)
        self.cmb_issue_year.setObjectName("cmb_issue_year")
        self.issuedate_layout.addWidget(self.cmb_issue_year)
        self.layoutWidget16 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget16.setGeometry(QtCore.QRect(420, 630, 346, 33))
        self.layoutWidget16.setObjectName("layoutWidget16")
        self.expirydate_layout = QtWidgets.QHBoxLayout(self.layoutWidget16)
        self.expirydate_layout.setContentsMargins(0, 0, 0, 0)
        self.expirydate_layout.setObjectName("expirydate_layout")
        self.lbl_licenseEx = QtWidgets.QLabel(self.layoutWidget16)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setKerning(True)
        self.lbl_licenseEx.setFont(font)
        self.lbl_licenseEx.setStyleSheet("")
        self.lbl_licenseEx.setObjectName("lbl_licenseEx")
        self.expirydate_layout.addWidget(self.lbl_licenseEx)
        self.cmb_expiry_month = QtWidgets.QComboBox(self.layoutWidget16)
        self.cmb_expiry_month.setObjectName("cmb_expiry_month")
        self.expirydate_layout.addWidget(self.cmb_expiry_month)
        self.cmb_expiry_day = QtWidgets.QComboBox(self.layoutWidget16)
        self.cmb_expiry_day.setObjectName("cmb_expiry_day")
        self.expirydate_layout.addWidget(self.cmb_expiry_day)
        self.cmb_expiry_year = QtWidgets.QComboBox(self.layoutWidget16)
        self.cmb_expiry_year.setObjectName("cmb_expiry_year")
        self.expirydate_layout.addWidget(self.cmb_expiry_year)
        self.layoutWidget17 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget17.setGeometry(QtCore.QRect(31, 84, 221, 33))
        self.layoutWidget17.setObjectName("layoutWidget17")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget17)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_profile = QtWidgets.QLabel(self.layoutWidget17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_profile.sizePolicy().hasHeightForWidth())
        self.lbl_profile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lbl_profile.setFont(font)
        self.lbl_profile.setStyleSheet("padding-right:2px;")
        self.lbl_profile.setObjectName("lbl_profile")
        self.horizontalLayout_2.addWidget(self.lbl_profile)
        self.btn_profImg = QtWidgets.QPushButton(self.layoutWidget17)
        self.btn_profImg.setMinimumSize(QtCore.QSize(121, 31))
        self.btn_profImg.setMaximumSize(QtCore.QSize(121, 31))
        self.btn_profImg.setStyleSheet("")
        self.btn_profImg.setObjectName("btn_profImg")
        self.horizontalLayout_2.addWidget(self.btn_profImg)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_profImg, self.txt_fname)
        MainWindow.setTabOrder(self.txt_fname, self.txt_lname)
        MainWindow.setTabOrder(self.txt_lname, self.rbtn_male)
        MainWindow.setTabOrder(self.rbtn_male, self.rbtn_female)
        MainWindow.setTabOrder(self.rbtn_female, self.cmb_month)
        MainWindow.setTabOrder(self.cmb_month, self.cmb_day)
        MainWindow.setTabOrder(self.cmb_day, self.cmb_year)
        MainWindow.setTabOrder(self.cmb_year, self.txt_address)
        MainWindow.setTabOrder(self.txt_address, self.txt_city)
        MainWindow.setTabOrder(self.txt_city, self.txt_province)
        MainWindow.setTabOrder(self.txt_province, self.txt_zip)
        MainWindow.setTabOrder(self.txt_zip, self.txt_email)
        MainWindow.setTabOrder(self.txt_email, self.txt_mobile)
        MainWindow.setTabOrder(self.txt_mobile, self.txt_emContact)
        MainWindow.setTabOrder(self.txt_emContact, self.txt_emNumber)
        MainWindow.setTabOrder(self.txt_emNumber, self.txt_certificate)
        MainWindow.setTabOrder(self.txt_certificate, self.txt_operator)
        MainWindow.setTabOrder(self.txt_operator, self.btn_cancel)
        MainWindow.setTabOrder(self.btn_cancel, self.btn_save)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIDS – Pilot Registration [Administrator] "))
        self.lbl_addPilot.setText(_translate("MainWindow", "Add Pilot"))
        self.lbl_caap.setText(_translate("MainWindow", "CAAP RPAS Certification Details"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.lbl_Lname.setText(_translate("MainWindow", "Last Name :"))
        self.lbl_fName.setText(_translate("MainWindow", "First Name :"))
        self.lbl_gender.setText(_translate("MainWindow", "Gender :"))
        self.rbtn_male.setText(_translate("MainWindow", "Male"))
        self.rbtn_female.setText(_translate("MainWindow", "Female"))
        self.lbl_dob.setText(_translate("MainWindow", "Date of Birth :"))
        self.lbl_address.setText(_translate("MainWindow", "Permanent Address :"))
        self.lbl_city.setText(_translate("MainWindow", "City  :"))
        self.lbl_province.setText(_translate("MainWindow", "Province :"))
        self.lbl_zip.setText(_translate("MainWindow", "Zip Code :"))
        self.lbl_email.setText(_translate("MainWindow", "Email Address :"))
        self.lbl_mobile.setText(_translate("MainWindow", "Phone Number :"))
        self.lbl_emContact.setText(_translate("MainWindow", "Emergency Contact :"))
        self.lbl_emNumber.setText(_translate("MainWindow", "Emergency Contact No. :"))
        self.lbl_certificate.setText(_translate("MainWindow", "Certificate No. :"))
        self.lbl_operator.setText(_translate("MainWindow", "Operator :"))
        self.lbl_licenseIssue.setText(_translate("MainWindow", "License Issue Date :"))
        self.lbl_licenseEx.setText(_translate("MainWindow", "License Expiry Date :"))
        self.lbl_profile.setText(_translate("MainWindow", "Profile Image :"))
        self.btn_profImg.setText(_translate("MainWindow", "Choose File..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
