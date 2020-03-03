import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.UpdatePilot import UpdatePilotAlt
import MySQLdb as mdb

class updateClass(QtWidgets.QMainWindow, UpdatePilotAlt.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_save.clicked.connect(self.update)
    
    def cancel(self):
        self.parent.cancel()
        self.close()
    
    def update(self):
        print('update')