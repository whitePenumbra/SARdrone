import sys, datetime
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.DeletePilot import DeletePilot, DeletePilotError, DeletePilotMultiple, DeletePilotMultipleSuccess, DeletePilotSuccess
from Gui.Administrator.Homepage import SelectMultipleDeleteAlert
from ConnectToDB import connectToDB

class deleteClass(QtWidgets.QMainWindow, DeletePilot.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        print("Delete Class: I was called")
        self.btn_delete.clicked.connect(self.goToDelete)
        self.btn_cancel.clicked.connect(self.cancel)

    def goToDelete(self):
        print("Call Soft Delete")
        self.parent.softDelete(self.parent.rows)
        self.close()
    
    def cancel(self):
        self.close()

class deleteSuccessClass(QtWidgets.QMainWindow, DeletePilotSuccess.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.btn_OK.clicked.connect(self.goBack)
        self.lbl_success_2.setText(str(self.parent.pilotID))

    def goBack(self):
        self.close()

class deleteErrorClass(QtWidgets.QMainWindow, DeletePilotError.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.btn_OK.clicked.connect(self.goBack)

    def goBack(self):
        self.close()

class multipleDeleteClass(QtWidgets.QMainWindow, DeletePilotMultiple.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.btn_cancel.clicked.connect(self.goBack)
        self.btn_delete.clicked.connect(self.goDelete)

    def goBack(self):
        self.close()

    def goDelete(self):
        self.parent.confirmMultiple()
        self.close()
    
class multipleSuccessClass(QtWidgets.QMainWindow, DeletePilotMultipleSuccess.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
    
        self.btn_OK.clicked.connect(self.goBack)
    
    def goBack(self):
        self.close()

class SelectMultipleDeleteAlertClass(QtWidgets.QMainWindow, SelectMultipleDeleteAlert.Ui_MainWindow):
    def __init__(self,parent):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.btn_OK.clicked.connect(self.goBack)

    def goBack(self):
        self.close()