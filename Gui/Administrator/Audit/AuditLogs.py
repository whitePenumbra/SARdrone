# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AuditLogs.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

# center table text
class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 739)
        MainWindow.setMinimumSize(QtCore.QSize(1071, 739))
        MainWindow.setMaximumSize(QtCore.QSize(1071, 739))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(680, 10, 361, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_user = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setKerning(True)
        self.lbl_user.setFont(font)
        self.lbl_user.setText("")
        self.lbl_user.setScaledContents(False)
        self.lbl_user.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_user.setObjectName("lbl_user")
        self.horizontalLayout.addWidget(self.lbl_user)
        self.btn_logout = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_logout.setMinimumSize(QtCore.QSize(121, 31))
        self.btn_logout.setMaximumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        font.setKerning(True)
        self.btn_logout.setFont(font)
        self.btn_logout.setStyleSheet("QPushButton {\n"
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
        self.btn_logout.setObjectName("btn_logout")
        self.horizontalLayout.addWidget(self.btn_logout)
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(920, 90, 121, 31))
        self.btn_search.setMinimumSize(QtCore.QSize(121, 31))
        self.btn_search.setMaximumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        font.setKerning(True)
        self.btn_search.setFont(font)
        self.btn_search.setIcon(QtGui.QIcon("../../Resources/search_white.png"))
        self.btn_search.setIconSize(QtCore.QSize(22,22))
        self.btn_search.setStyleSheet("QPushButton {\n"
                "color: rgb(255, 255, 255);\n"
                " background-color: #26A69A;\n"
                "border: 1.2px solid #009688;\n"
                "outline: none;}\n"
                "\n"
                "QPushButton:hover{\n"
                "background-color: #009688;\n"
                "outline: none;\n"
                "border: none;\n"
                "}\n"
                "\n"
                "QPushButton:pressed{\n"
                "background-color: #00897B;\n"
                "outline: none;\n"
                "border: none;\n"
                "}\n"
                "\n"
                "\n"
                "")
        self.btn_search.setObjectName("btn_search")
        self.searchbar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchbar.setGeometry(QtCore.QRect(700, 90, 201, 31))
        self.searchbar.setMinimumSize(QtCore.QSize(201, 31))
        self.searchbar.setMaximumSize(QtCore.QSize(201, 31))
        self.searchbar.setStyleSheet("padding-left: 4px;")
        self.searchbar.setText("")
        self.searchbar.setObjectName("searchbar")
        self.lbl_audit = QtWidgets.QLabel(self.centralwidget)
        self.lbl_audit.setGeometry(QtCore.QRect(30, 50, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(29)
        font.setKerning(True)
        self.lbl_audit.setFont(font)
        self.lbl_audit.setObjectName("lbl_audit")
        self.table_audit = QtWidgets.QTableWidget(self.centralwidget)
        self.table_audit.setGeometry(QtCore.QRect(30, 130, 1011, 551))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.table_audit.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_audit.sizePolicy().hasHeightForWidth())
        self.table_audit.setSizePolicy(sizePolicy)
        self.table_audit.setAutoFillBackground(False)
        self.table_audit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_audit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_audit.setObjectName("table_audit")
        self.table_audit.setColumnCount(3)
        self.table_audit.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setKerning(True)
        font.setBold(True)
        item.setFont(font)
        self.table_audit.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setKerning(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(203, 203, 203))
        self.table_audit.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setKerning(True)
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(203, 203, 203))
        self.table_audit.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setKerning(True)
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(203, 203, 203))
        self.table_audit.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setKerning(True)
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(203, 203, 203))
        self.table_audit.horizontalHeader().setVisible(True)
        self.table_audit.horizontalHeader().setCascadingSectionResizes(False)
        self.table_audit.horizontalHeader().setHighlightSections(True)
        self.table_audit.horizontalHeader().setSortIndicatorShown(True)
        self.table_audit.horizontalHeader().setStretchLastSection(True)
        self.table_audit.verticalHeader().setVisible(False)
        self.table_audit.verticalHeader().setSortIndicatorShown(False)
        self.table_audit.verticalHeader().setStretchLastSection(False)
        self.table_audit.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.table_audit.setColumnWidth(0, 150)
        self.table_audit.setColumnWidth(1, 250)
        self.table_audit.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.table_audit.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.table_audit.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        # add bottom border for horizontal header
        self.table_audit.horizontalHeader().setStyleSheet("QHeaderView::section{"
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
                "}");
        # remove select trigger
        self.table_audit.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.table_audit.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # center column text
        delegate = AlignDelegate(self.table_audit)
        self.table_audit.setItemDelegate(delegate)
        # remove dotted border
        self.table_audit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(920, 690, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setKerning(True)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("QPushButton {\n"
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
        self.btn_back.setObjectName("btn_back")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIDS – Audit Logs [Administrator]"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.lbl_audit.setText(_translate("MainWindow", "Audit Logs"))
        self.table_audit.setSortingEnabled(True)
        item = self.table_audit.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User ID"))
        item = self.table_audit.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "System  Access"))
        item = self.table_audit.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Actions Made"))
        self.btn_back.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
