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

        i=0
        while i < 31:
            self.cmb_day.addItem(str(i+1))
            i+=1
        

        monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December']

        self.cmb_month.addItems(monthList)
    
    def returnToHome(self):
        self.close()
        self.parent.showself()
    
    def savePilot(self):
        fname = self.txt_fname.text()
        lname = self.txt_lname.text()

        if (self.rbtn_female.isChecked()):
            gender = 'F'
        elif (self.rbtn_male.isChecked()):
            gender = 'M'

        month = self.cmb_month.text()
        day = self.cmb_day.text()
        year = self.cmb_year.text()

        address = self.txt_address.text()

        print('Saved')
        print(fname + " " + lname)
        print(gender)
        print(month + " " + day + ", " + year)
        self.returnToHome()