import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Pilot.Homepage import Homepage

class pilothomepageClass(QtWidgets.QMainWindow, Homepage.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        
        self.btn_profile.clicked.connect(self.view)
        self.btn_pastOps.clicked.connect(self.operations)
        self.btn_logout.clicked.connect(self.logout)
        self.btn_Launch.clicked.connect(self.launch)
        self.btn_endOps.clicked.connect(self.endOperation)
        self.btn_PDF.clicked.connect(self.printPDF)

    def view(self):
        print('Pilot View button')
    
    def operations(self):
        print('Pilot Operations button')
    
    def logout(self):
        self.close()
        self.parent.showself()
    
    def launch(self):
        print('Pilot Launch button')

    def endOperation(self):
        print('Pilot End Operations button')

    def printPDF(self):
        print('Pilot PDF button')