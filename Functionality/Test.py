import sys, datetime
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Test import SampleMainWindow,SampleQDialog
import MySQLdb as mdb
import datetime

# class testClass(QtWidgets.QMainWindow, SampleMainWindow.Ui_MainWindow):
#     def __init__(self,parent):
#         super(self.__class__, self).__init__()
#         self.setupUi(self)
#         self.parent = parent

class testClass(QtWidgets.QDialog, SampleQDialog.Ui_Dialog):
    def __init__(self,parent):
        super(QtWidgets.QDialog,self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.pushButton.clicked.connect(self.closeButton)

    def closeButton(self):
        self.parent.enableAll()
        self.close()