# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage(1182x773).ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setMaximumSize(QtCore.QSize(871,0))
        MainWindow.setMinimumSize(QtCore.QSize(871, 760))
        MainWindow.setWindowTitle("AIDS – Operation ")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        layout.addWidget(self.scrollArea)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 830, 1530))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #header
        
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 641, 57))
        self.layoutWidget.setObjectName("layoutWidget")
        self.header_layout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setObjectName("header_layout")
        self.lbl_ops = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(31)
        self.lbl_ops.setFont(font)
        self.lbl_ops.setText("Operation Details")
        self.lbl_ops.setObjectName("lbl_ops")
        self.header_layout.addWidget(self.lbl_ops)
        self.lbl_opsNo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(31)
        self.lbl_opsNo.setFont(font)
        self.lbl_opsNo.setText("")
        self.lbl_opsNo.setObjectName("lbl_opsNo")
        self.header_layout.addWidget(self.lbl_opsNo)

        #operation details (left)

        self.layoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 100, 411, 431))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.opsdeets1_layout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.opsdeets1_layout.setContentsMargins(0, 0, 0, 0)
        self.opsdeets1_layout.setObjectName("opsdeets1_layout")
        self.opsid_layout = QtWidgets.QHBoxLayout()
        self.opsid_layout.setObjectName("opsid_layout")
        self.lbl_opsid_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_opsid_2.setFont(font)
        self.lbl_opsid_2.setText("Operation ID :")
        self.lbl_opsid_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_opsid_2.setObjectName("lbl_opsid_2")
        self.opsid_layout.addWidget(self.lbl_opsid_2)
        self.lbl_opsid = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_opsid.setMinimumSize(QtCore.QSize(281, 31))
        self.lbl_opsid.setMaximumSize(QtCore.QSize(281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_opsid.setFont(font)
        self.lbl_opsid.setStyleSheet("")
        self.lbl_opsid.setText("")
        self.lbl_opsid.setObjectName("lbl_opsid")
        self.opsid_layout.addWidget(self.lbl_opsid)
        self.opsdeets1_layout.addLayout(self.opsid_layout)
        self.droneid_layout = QtWidgets.QHBoxLayout()
        self.droneid_layout.setObjectName("droneid_layout")
        self.lbl_droneid_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_droneid_2.setFont(font)
        self.lbl_droneid_2.setText("Drone ID :")
        self.lbl_droneid_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_droneid_2.setObjectName("lbl_droneid_2")
        self.droneid_layout.addWidget(self.lbl_droneid_2)
        self.lbl_droneid = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_droneid.setMinimumSize(QtCore.QSize(281, 31))
        self.lbl_droneid.setMaximumSize(QtCore.QSize(281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_droneid.setFont(font)
        self.lbl_droneid.setText("")
        self.lbl_droneid.setObjectName("lbl_droneid")
        self.droneid_layout.addWidget(self.lbl_droneid)
        self.opsdeets1_layout.addLayout(self.droneid_layout)
        self.pilotid_layout = QtWidgets.QHBoxLayout()
        self.pilotid_layout.setObjectName("pilotid_layout")
        self.lbl_pilotid_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_pilotid_2.setFont(font)
        self.lbl_pilotid_2.setText("Pilot ID :")
        self.lbl_pilotid_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_pilotid_2.setObjectName("lbl_pilotid_2")
        self.pilotid_layout.addWidget(self.lbl_pilotid_2)
        self.lbl_pilotid = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_pilotid.setMinimumSize(QtCore.QSize(281, 31))
        self.lbl_pilotid.setMaximumSize(QtCore.QSize(281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_pilotid.setFont(font)
        self.lbl_pilotid.setText("")
        self.lbl_pilotid.setObjectName("lbl_pilotid")
        self.pilotid_layout.addWidget(self.lbl_pilotid)
        self.opsdeets1_layout.addLayout(self.pilotid_layout)
        self.piltoname_layout = QtWidgets.QHBoxLayout()
        self.piltoname_layout.setObjectName("piltoname_layout")
        self.lbl_pilotname_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_pilotname_2.setFont(font)
        self.lbl_pilotname_2.setText("Pilot Name :")
        self.lbl_pilotname_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_pilotname_2.setObjectName("lbl_pilotname_2")
        self.piltoname_layout.addWidget(self.lbl_pilotname_2)
        self.lbl_pilotname = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_pilotname.setMinimumSize(QtCore.QSize(281, 31))
        self.lbl_pilotname.setMaximumSize(QtCore.QSize(281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_pilotname.setFont(font)
        self.lbl_pilotname.setText("")
        self.lbl_pilotname.setObjectName("lbl_pilotname")
        self.piltoname_layout.addWidget(self.lbl_pilotname)
        self.opsdeets1_layout.addLayout(self.piltoname_layout)
        self.coPilotID_layout = QtWidgets.QHBoxLayout()
        self.coPilotID_layout.setObjectName("coPilotID_layout")
        self.lbl_coID_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_coID_2.setFont(font)
        self.lbl_coID_2.setText("Co-Pilot ID :")
        self.lbl_coID_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_coID_2.setObjectName("lbl_coID_2")
        self.coPilotID_layout.addWidget(self.lbl_coID_2)
        self.lbl_coID = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_coID.setMinimumSize(QtCore.QSize(281, 31))
        self.lbl_coID.setMaximumSize(QtCore.QSize(281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_coID.setFont(font)
        self.lbl_coID.setText("")
        self.lbl_coID.setObjectName("lbl_coID")
        self.coPilotID_layout.addWidget(self.lbl_coID)
        self.opsdeets1_layout.addLayout(self.coPilotID_layout)
        self.coPilotName_layout = QtWidgets.QHBoxLayout()
        self.coPilotName_layout.setObjectName("coPilotName_layout")
        self.lbl_coPilotName_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_coPilotName_2.setFont(font)
        self.lbl_coPilotName_2.setText("Co-Pilot Name :")
        self.lbl_coPilotName_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_coPilotName_2.setObjectName("lbl_coPilotName_2")
        self.coPilotName_layout.addWidget(self.lbl_coPilotName_2)
        self.lbl_coPilotName = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_coPilotName.setMinimumSize(QtCore.QSize(281, 31))
        self.lbl_coPilotName.setMaximumSize(QtCore.QSize(281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_coPilotName.setFont(font)
        self.lbl_coPilotName.setText("")
        self.lbl_coPilotName.setObjectName("lbl_coPilotName")
        self.coPilotName_layout.addWidget(self.lbl_coPilotName)
        self.opsdeets1_layout.addLayout(self.coPilotName_layout)
        
        
        #operation details (right)

        self.layoutWidget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_3.setGeometry(QtCore.QRect(480, 104, 351, 291))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.opsdeets2_layout = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.opsdeets2_layout.setContentsMargins(0, 0, 0, 0)
        self.opsdeets2_layout.setObjectName("opsdeets2_layout")
        self.location_layout = QtWidgets.QHBoxLayout()
        self.location_layout.setObjectName("location_layout")
        self.lbl_location_2 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_location_2.setFont(font)
        self.lbl_location_2.setText("Location :")
        self.lbl_location_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_location_2.setObjectName("lbl_location_2")
        self.location_layout.addWidget(self.lbl_location_2)
        self.lbl_location = QtWidgets.QLabel(self.layoutWidget_3)
        self.lbl_location.setMinimumSize(QtCore.QSize(231, 41))
        self.lbl_location.setMaximumSize(QtCore.QSize(231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_location.setFont(font)
        self.lbl_location.setText("")
        self.lbl_location.setObjectName("lbl_location")
        self.location_layout.addWidget(self.lbl_location)
        self.opsdeets2_layout.addLayout(self.location_layout)
        self.date_layout = QtWidgets.QHBoxLayout()
        self.date_layout.setObjectName("date_layout")
        self.lbl_date_2 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_date_2.setFont(font)
        self.lbl_date_2.setText("Date :")
        self.lbl_date_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_date_2.setObjectName("lbl_date_2")
        self.date_layout.addWidget(self.lbl_date_2)
        self.lbl_date = QtWidgets.QLabel(self.layoutWidget_3)
        self.lbl_date.setMinimumSize(QtCore.QSize(231, 41))
        self.lbl_date.setMaximumSize(QtCore.QSize(231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_date.setFont(font)
        self.lbl_date.setText("")
        self.lbl_date.setObjectName("lbl_date")
        self.date_layout.addWidget(self.lbl_date)
        self.opsdeets2_layout.addLayout(self.date_layout)
        self.timeStart_layout = QtWidgets.QHBoxLayout()
        self.timeStart_layout.setObjectName("timeStart_layout")
        self.lbl_timeStart_2 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_timeStart_2.setFont(font)
        self.lbl_timeStart_2.setText("Time Started :")
        self.lbl_timeStart_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_timeStart_2.setObjectName("lbl_timeStart_2")
        self.timeStart_layout.addWidget(self.lbl_timeStart_2)
        self.lbl_timeStart = QtWidgets.QLabel(self.layoutWidget_3)
        self.lbl_timeStart.setMinimumSize(QtCore.QSize(231, 41))
        self.lbl_timeStart.setMaximumSize(QtCore.QSize(231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_timeStart.setFont(font)
        self.lbl_timeStart.setText("")
        self.lbl_timeStart.setObjectName("lbl_timeStart")
        self.timeStart_layout.addWidget(self.lbl_timeStart)
        self.opsdeets2_layout.addLayout(self.timeStart_layout)
        self.timeEnd_layout = QtWidgets.QHBoxLayout()
        self.timeEnd_layout.setObjectName("timeEnd_layout")
        self.lbl_timeEnd = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_timeEnd.setFont(font)
        self.lbl_timeEnd.setText("Time Ended :")
        self.lbl_timeEnd.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_timeEnd.setObjectName("lbl_timeEnd")
        self.timeEnd_layout.addWidget(self.lbl_timeEnd)
        self.lbl_timeEnd_2 = QtWidgets.QLabel(self.layoutWidget_3)
        self.lbl_timeEnd_2.setMinimumSize(QtCore.QSize(231, 41))
        self.lbl_timeEnd_2.setMaximumSize(QtCore.QSize(231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_timeEnd_2.setFont(font)
        self.lbl_timeEnd_2.setText("")
        self.lbl_timeEnd_2.setObjectName("lbl_timeEnd_2")
        self.timeEnd_layout.addWidget(self.lbl_timeEnd_2)
        self.opsdeets2_layout.addLayout(self.timeEnd_layout)
        
        #horizontal line 1

        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(40, 550, 769, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        #drone report header
        self.lbl_droneReport = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_droneReport.setGeometry(QtCore.QRect(40, 580, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        self.lbl_droneReport.setFont(font)
        self.lbl_droneReport.setText("Drone Generated Report")
        self.lbl_droneReport.setObjectName("lbl_droneReport")

        #drone generated report
        
        self.layoutWidget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_4.setGeometry(QtCore.QRect(478, 710, 221, 23))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.totalObjFound_layout = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.totalObjFound_layout.setContentsMargins(0, 0, 0, 0)
        self.totalObjFound_layout.setObjectName("totalObjFound_layout")
        self.lbl_totalObjFound_2 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_totalObjFound_2.setFont(font)
        self.lbl_totalObjFound_2.setText("Total Objects Found :")
        self.lbl_totalObjFound_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_totalObjFound_2.setObjectName("lbl_totalObjFound_2")
        self.totalObjFound_layout.addWidget(self.lbl_totalObjFound_2)
        self.lbl_totalObjFound = QtWidgets.QLabel(self.layoutWidget_4)
        self.lbl_totalObjFound.setMinimumSize(QtCore.QSize(51, 21))
        self.lbl_totalObjFound.setMaximumSize(QtCore.QSize(51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_totalObjFound.setFont(font)
        self.lbl_totalObjFound.setText("")
        self.lbl_totalObjFound.setObjectName("lbl_totalObjFound")
        self.totalObjFound_layout.addWidget(self.lbl_totalObjFound)
        self.layoutWidget_9 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_9.setGeometry(QtCore.QRect(40, 710, 231, 23))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.totalWaypoint_layout = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.totalWaypoint_layout.setContentsMargins(0, 0, 0, 0)
        self.totalWaypoint_layout.setObjectName("totalWaypoint_layout")
        self.lbl_totalWaypoints = QtWidgets.QLabel(self.layoutWidget_9)
        self.lbl_totalWaypoints.setText("Number of Waypoints :")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_totalWaypoints.setFont(font)
        self.lbl_totalWaypoints.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_totalWaypoints.setObjectName("lbl_totalWaypoints")
        self.totalWaypoint_layout.addWidget(self.lbl_totalWaypoints)
        self.lbl_totalWaypoint_2 = QtWidgets.QLabel(self.layoutWidget_9)
        self.lbl_totalWaypoint_2.setMinimumSize(QtCore.QSize(51, 21))
        self.lbl_totalWaypoint_2.setMaximumSize(QtCore.QSize(51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_totalWaypoint_2.setFont(font)
        self.lbl_totalWaypoint_2.setText("")
        self.lbl_totalWaypoint_2.setObjectName("lbl_totalWaypoint_2")
        self.totalWaypoint_layout.addWidget(self.lbl_totalWaypoint_2)
        self.layoutWidget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_5.setGeometry(QtCore.QRect(40, 640, 341, 43))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.flightduration_layout = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.flightduration_layout.setContentsMargins(0, 0, 0, 0)
        self.flightduration_layout.setObjectName("flightduration_layout")
        self.lbl_flightduration_2 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_flightduration_2.setFont(font)
        self.lbl_flightduration_2.setText("Flight Duration :")
        self.lbl_flightduration_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_flightduration_2.setObjectName("lbl_flightduration_2")
        self.flightduration_layout.addWidget(self.lbl_flightduration_2)
        self.lbl_flightduration = QtWidgets.QLabel(self.layoutWidget_5)
        self.lbl_flightduration.setMinimumSize(QtCore.QSize(171, 41))
        self.lbl_flightduration.setMaximumSize(QtCore.QSize(171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_flightduration.setFont(font)
        self.lbl_flightduration.setText("")
        self.lbl_flightduration.setObjectName("lbl_flightduration")
        self.flightduration_layout.addWidget(self.lbl_flightduration)
        self.layoutWidget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_6.setGeometry(QtCore.QRect(479, 640, 341, 43))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.battery_layout = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.battery_layout.setContentsMargins(0, 0, 0, 0)
        self.battery_layout.setObjectName("battery_layout")
        self.lbl_battery_2 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_battery_2.setFont(font)
        self.lbl_battery_2.setText("Battery Capacity :")
        self.lbl_battery_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_battery_2.setObjectName("lbl_battery_2")
        self.battery_layout.addWidget(self.lbl_battery_2)
        self.lbl_battery = QtWidgets.QLabel(self.layoutWidget_6)
        self.lbl_battery.setMinimumSize(QtCore.QSize(191, 41))
        self.lbl_battery.setMaximumSize(QtCore.QSize(191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_battery.setFont(font)
        self.lbl_battery.setText("")
        self.lbl_battery.setObjectName("lbl_battery")
        self.battery_layout.addWidget(self.lbl_battery)

        #expedition logs

        self.table_exLog = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.table_exLog.setGeometry(QtCore.QRect(40, 1070, 760, 152))
        self.table_exLog.setRowCount(5)
        self.table_exLog.setColumnCount(2)
        self.table_exLog.setObjectName("table_exLog")
        self.table_exLog.horizontalHeader().setVisible(False)
        self.table_exLog.horizontalHeader().setStretchLastSection(True)
        self.table_exLog.verticalHeader().setVisible(False)
        self.table_exLog.verticalHeader().setStretchLastSection(False)
        self.table_exLog.setColumnWidth(0, 390)
        # remove select trigger
        self.table_exLog.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.table_exLog.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # remove dotted border
        self.table_exLog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.img_mapExp = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.img_mapExp.setGeometry(QtCore.QRect(40, 830, 770, 211))
        self.img_mapExp.setMinimumSize(QtCore.QSize(755, 211))
        self.img_mapExp.setMaximumSize(QtCore.QSize(755, 211))
        self.img_mapExp.setText("")
        self.img_mapExp.setPixmap(QtGui.QPixmap("../../Resources/map-placeholder.jpg"))
        self.img_mapExp.setScaledContents(False)
        self.img_mapExp.setObjectName("img_mapExp")
        self.lbl_expeditionLogs = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_expeditionLogs.setGeometry(QtCore.QRect(40, 770, 211, 28))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(19)
        self.lbl_expeditionLogs.setFont(font)
        self.lbl_expeditionLogs.setText("[ Expedition Logs ]")
        self.lbl_expeditionLogs.setObjectName("lbl_expeditionLogs")


        #comparison form
        self.lbl_missedCount = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_missedCount.setGeometry(QtCore.QRect(40, 1310, 251, 28))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(19)
        self.lbl_missedCount.setFont(font)
        self.lbl_missedCount.setText("[ Missed Count Logs ]")
        self.lbl_missedCount.setObjectName("lbl_missedCount")
        self.lbl_comparison = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_comparison.setGeometry(QtCore.QRect(40, 1250, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        self.lbl_comparison.setFont(font)
        self.lbl_comparison.setText("Pilot Comparison Form")
        self.lbl_comparison.setObjectName("lbl_comparison")
        self.layoutWidget_8 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_8.setGeometry(QtCore.QRect(40, 1370, 251, 23))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.missedobj_layout = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.missedobj_layout.setContentsMargins(0, 0, 0, 0)
        self.missedobj_layout.setObjectName("missedobj_layout")
        self.lbl_missedobj_2 = QtWidgets.QLabel(self.layoutWidget_8)
        self.lbl_missedobj_2.setText("Missed Object Count :")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_missedobj_2.setFont(font)
        self.lbl_missedobj_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_missedobj_2.setObjectName("lbl_missedobj_2")
        self.missedobj_layout.addWidget(self.lbl_missedobj_2)
        self.lbl_missedobj = QtWidgets.QLabel(self.layoutWidget_8)
        self.lbl_missedobj.setMinimumSize(QtCore.QSize(51, 21))
        self.lbl_missedobj.setMaximumSize(QtCore.QSize(51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_missedobj.setFont(font)
        self.lbl_missedobj.setText("")
        self.lbl_missedobj.setObjectName("lbl_missedobj")
        self.missedobj_layout.addWidget(self.lbl_missedobj)
        self.layoutWidget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_7.setGeometry(QtCore.QRect(480, 1370, 221, 23))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.totalObjCount = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.totalObjCount.setContentsMargins(0, 0, 0, 0)
        self.totalObjCount.setObjectName("totalObjCount")
        self.lbl_totalObjCount_2 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_totalObjCount_2.setFont(font)
        self.lbl_totalObjCount_2.setText("Updated Total Count :")
        self.lbl_totalObjCount_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.lbl_totalObjCount_2.setObjectName("lbl_totalObjCount_2")
        self.totalObjCount.addWidget(self.lbl_totalObjCount_2)
        self.lbl_totalObjCount = QtWidgets.QLabel(self.layoutWidget_7)
        self.lbl_totalObjCount.setMinimumSize(QtCore.QSize(51, 21))
        self.lbl_totalObjCount.setMaximumSize(QtCore.QSize(51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbl_totalObjCount.setFont(font)
        self.lbl_totalObjCount.setObjectName("lbl_totalObjCount")
        self.totalObjCount.addWidget(self.lbl_totalObjCount)
        self.table_comparison = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.table_comparison.setGeometry(QtCore.QRect(40, 1420, 760, 71))
        self.table_comparison.setRowCount(2)
        self.table_comparison.setColumnCount(2)
        self.table_comparison.setObjectName("table_comparison")
        self.table_comparison.horizontalHeader().setVisible(False)
        self.table_comparison.horizontalHeader().setStretchLastSection(True)
        self.table_comparison.verticalHeader().setVisible(False)
        self.table_comparison.verticalHeader().setStretchLastSection(True)
        self.table_comparison.setColumnWidth(0, 390)
        # remove select trigger
        self.table_comparison.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.table_comparison.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # remove dotted border
        self.table_comparison.setFocusPolicy(QtCore.Qt.NoFocus)


        
        layout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)        
        MainWindow.setCentralWidget(self.centralwidget)
        
        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "AIDS – Operations History [Administrator]"))
            self.lbl_ops.setText(_translate("MainWindow", "Operation Details"))
            self.lbl_opsid_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#434343;\">Operation ID : </span></p></body></html>"))
            self.lbl_droneid_2.setText(_translate("MainWindow", "Drone ID :"))
            self.lbl_pilotid_2.setText(_translate("MainWindow", "Pilot ID : "))
            self.lbl_pilotname_2.setText(_translate("MainWindow", "Pilot Name : "))
            self.lbl_coID_2.setText(_translate("MainWindow", "Co-Pilot ID :"))
            self.lbl_coPilotName_2.setText(_translate("MainWindow", "Co-Pilot Name : "))
            self.lbl_location_2.setText(_translate("MainWindow", "Location :"))
            self.lbl_date_2.setText(_translate("MainWindow", "Date :"))
            self.lbl_timeStart_2.setText(_translate("MainWindow", "Time Started :"))
            self.lbl_timeEnd.setText(_translate("MainWindow", "Time Ended :"))
            self.lbl_droneReport.setText(_translate("MainWindow", "Drone Generated Report"))
            self.lbl_totalObjFound_2.setText(_translate("MainWindow", "Total Objects Found :"))
            self.lbl_flightduration_2.setText(_translate("MainWindow", "Flight Duration :"))
            self.lbl_battery_2.setText(_translate("MainWindow", "Battery Capacity :"))
            self.lbl_expeditionLogs.setText(_translate("MainWindow", "[ Expedition Logs ]"))
            self.lbl_totalObjCount_2.setText(_translate("MainWindow", "Total Object Count :"))
            self.lbl_totalObjCount.setText(_translate("MainWindow", "8"))
            self.lbl_missedCount.setText(_translate("MainWindow", "[ Missed Count Logs ]"))
            self.lbl_comparison.setText(_translate("MainWindow", "Pilot Comparison Form"))
            self.lbl_missedobj_2.setText(_translate("MainWindow", "Missed Object Counts :"))
            self.lbl_missedobj.setText(_translate("MainWindow", "8"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
