import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administator.Homepage import HomepageAlt

class homepageClass(QtWidgets.QMainWindow, HomepageAlt.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)