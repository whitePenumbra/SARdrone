import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.Homepage import HomepageAlt
from AddPilot import addClass


class homepageClass(QtWidgets.QMainWindow, HomepageAlt.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_add.clicked.connect(self.add)
        self.btn_operations.clicked.connect(self.operations)
        self.btn_search.clicked.connect(self.search)
        self.btn_logout.clicked.connect(self.logout)

    def add(self):
        print('adddddd')
        self.addPilot = addClass(parent=self)
        self.addPilot.show()
        self.hide()

    def operations(self):
        print('operations')

    def search(self):
        print('search')
        # searchbar.text
    
    def logout(self):
        self.close()
        self.parent.showself()

    def showself(self):
        self.show()