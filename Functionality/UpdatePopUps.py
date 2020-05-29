import sys, datetime
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.UpdatePilot import UpdatePilotConfirm,UpdatePilotError,UpdatePilotSuccess,UnsavedChangesAlert
import MySQLdb as mdb
import datetime

class cancelUpdateClass(QtWidgets.QMainWindow, UnsavedChangesAlert.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.btn_delete.clicked.connect(self.exit)
        self.btn_cancel.clicked.connect(self.goBack)

    def closeEvent(self, event):
        self.goBack()

    def exit(self):
        self.close()
        self.parent.returnToView()
    
    def goBack(self):
        self.parent.btn_save.setEnabled(True)
        self.parent.btn_cancel.setEnabled(True)
        self.parent.enableAll()

        self.close()

class confirmPopupClass(QtWidgets.QMainWindow, UpdatePilotConfirm.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.pushButton_2.clicked.connect(self.save)
        self.pushButton.clicked.connect(self.cancel)
        self.pushButton_3.clicked.connect(self.delete)

    def closeEvent(self, event):
        self.cancel()

    def cancel(self):
        self.parent.enableAll()

        self.close()
    
    def delete(self):
        self.close()
        self.parent.returnToView()
    
    def save(self):
        if (self.parent.txt_fname.text() == '' or self.parent.txt_lname.text() == '' or 
        self.parent.txt_address.text() == '' or self.parent.txt_city.text() == '' or self.parent.txt_province.text() == '' or
        self.parent.txt_zip.text() == '' or self.parent.txt_email.text() == '' or self.parent.txt_mobile.text() == ''
        or self.parent.txt_emContact.text() == '' or self.parent.txt_emNumber.text() == '' or self.parent.txt_certificate.text() == ''
        or self.parent.txt_operator.text() == ''):
            self.close()
            self.parent.btn_save.setEnabled(False)
        else:
            self.close()
            self.parent.saveUpdate()

class updateSuccessClass(QtWidgets.QMainWindow, UpdatePilotSuccess.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.btn_OK.clicked.connect(self.goBack)

    def goBack(self):
        self.close()

class updateErrorClass(QtWidgets.QMainWindow, UpdatePilotError.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.btn_OK.clicked.connect(self.goBack)

    def goBack(self):
        self.close()