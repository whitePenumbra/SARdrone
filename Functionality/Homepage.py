import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from Gui.Administrator.Homepage import HomepageAlt
from AddPilot import addClass
import MySQLdb as mdb


class homepageClass(QtWidgets.QMainWindow, HomepageAlt.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_add.clicked.connect(self.add)
        self.btn_operations.clicked.connect(self.operations)
        self.btn_search.clicked.connect(self.search)
        self.btn_logout.clicked.connect(self.logout)

        con = mdb.connect('localhost', 'root', '', 'aids')
        cur = con.cursor()

        cur.execute('SELECT user_id,last_name,first_name from users WHERE isActive = 1 AND user_type = 1')
        result = cur.fetchall()
        self.table_pilots.setRowCount(len(result))
        print(result)
        row = 0
        for i in result:
            self.table_pilots.setItem(row,0, QtWidgets.QTableWidgetItem('OP-00' + str(i[0])))
            self.table_pilots.setItem(row,1, QtWidgets.QTableWidgetItem(i[1]))
            self.table_pilots.setItem(row,2, QtWidgets.QTableWidgetItem(i[2]))

            #create buttons inside table cell
            layout = QtWidgets.QHBoxLayout()
            self.btn_view = QtWidgets.QPushButton()
            self.btn_view.clicked.connect(self.view)
            self.btn_delete = QtWidgets.QPushButton()
            self.btn_delete.clicked.connect(self.softDelete)
            #btn_view.setText('View')
            self.btn_view.setFixedHeight(34)
            self.btn_delete.setFixedHeight(34)
            self.btn_delete.setIcon(QtGui.QIcon("../Gui/Resources/trash_delete_2.png"))
            self.btn_delete.setIconSize(QtCore.QSize(22,22))
            self.btn_view.setIcon(QtGui.QIcon("../Gui/Resources/file_view.png"))
            self.btn_view.setIconSize(QtCore.QSize(22,22))
            #btn_delete.setText('Delete')
            font = QtGui.QFont()
            font.setFamily("Helvetica")
            font.setPointSize(11)
            self.btn_view.setFont(font)
            self.btn_delete.setFont(font)
            self.btn_delete.setStyleSheet("QPushButton {\n"
    "color: rgb(255, 255, 255);\n"
    "background-color: #E53935;\n"
    "border: 1.2px solid #D32F2F;\n"
    "outline: none;}\n"
    "\n"
    "QPushButton:hover{\n"
    "background-color: #D32F2F;\n"
    "outline: none;\n"
    "border: none;\n"
    "}\n"
    "\n"
    "QPushButton:pressed{\n"
    "    background-color: #C62828;\n"
    "outline: none;\n"
    "border: none;\n"
    "}\n"
    "\n"
    "\n"
    "")
            self.btn_view.setStyleSheet("QPushButton {\n"
    "    background-color: #1E88E5;\n"
    "    color: rgb(255, 255, 255);\n"
    "border: 1.2px solid #1976D2;\n"
    "outline: none;}\n"
    "\n"
    "QPushButton:hover{\n"
    "    background-color: #1976D2;\n"
    "outline: none;\n"
    "border: none;\n"
    "}\n"
    "\n"
    "QPushButton:pressed{\n"
    "    background-color: #1565C0;\n"
    "outline: none;\n"
    "border: none;\n"
    "}\n"
    "\n"
    "\n"
    "")
            self.btn_view.setCursor(QtCore.Qt.PointingHandCursor)
            self.btn_delete.setCursor(QtCore.Qt.PointingHandCursor)
            layout.addStretch()
            layout.addWidget(self.btn_view,20)
            layout.addWidget(self.btn_delete,20)

            self.cellWidget = QtWidgets.QWidget()
            self.cellWidget.setLayout(layout)

            self.table_pilots.setCellWidget(row,3,self.cellWidget) #buttons placement
            # self.table_pilots.setCellWidget(row,4,self.btn_delete)
            self.table_pilots.horizontalHeader().setStyleSheet( "QHeaderView::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid #D8D8D8;"
                "border-bottom: 1px solid #D8D8D8;"
                "background-color:white;"
                "padding:4px;"
            "}"
            "QTableCornerButton::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid #D8D8D8;"
                "border-bottom: 1px solid #D8D8D8;"
                "background-color:white;"
            "}" );

            row += 1

    def add(self):
        print('adddddd')
        self.addPilot = addClass(parent=self)
        self.addPilot.show()
        self.close()

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
    
    def softDelete(self):
        print('del')
        button = self.sender()
        row = self.table_pilots.indexAt(button.pos()).row()
        
        lastName = self.table_pilots.item(row,1).text()
        firstName = self.table_pilots.item(row,2).text()

        conn = mdb.connect('localhost', 'root', '', 'aids')
        cur = conn.cursor()

        print(firstName + " " + lastName)
        cur.execute('UPDATE users SET isActive = 0 WHERE first_name = "%s" AND last_name = "%s"' % (firstName, lastName))
        conn.commit()



    def view(self):
        print('view')
        button = self.sender()
        row = self.table_pilots.indexAt(button.pos()).row()
        print(row)