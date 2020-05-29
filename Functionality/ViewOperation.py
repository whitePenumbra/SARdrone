import sys, datetime, smtplib, ssl, re
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('..')
from ConnectToDB import connectToDB
from Gui.Administrator.OperationDetails import OperationDetails

class viewOperationClass(QtWidgets.QMainWindow, OperationDetails.Ui_MainWindow):
    def __init__(self,parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.info = self.getData()
        self.compData = self.compareData()
        self.mainPilotInfo = self.getMainPilot()
        self.coPilotInfo = self.getCoPilot()

        self.lbl_opsid.setText(str(self.info[0]))
        self.lbl_location.setText(str(self.info[1]))

        self.lbl_timeStart.setText(self.info[2].strftime("%H:%M:%S"))
        self.lbl_timeEnd_2.setText(self.info[3].strftime("%H:%M:%S"))

        self.lbl_flightduration.setText(str(self.info[4]))
        self.lbl_totalObjFound.setText(str(self.info[5]))
        self.lbl_battery.setText(str(self.info[6]))
        # self.lbl_date.setText(self.info[7].strftime("%B%d%Y"))

        self.lbl_missedobj.setText(str(self.compData[2]))
        self.lbl_totalObjCount.setText(str(self.compData[3]))

        self.lbl_pilotid.setText(str(self.mainPilotInfo[0]))
        self.lbl_pilotname.setText(str(self.mainPilotInfo[1]) + " " + str(self.mainPilotInfo[2]))

        self.lbl_droneid.setText(self.droneID)

        self.lbl_coID.setText(str(self.coPilotInfo[0]))
        self.lbl_coPilotName.setText(str(self.coPilotInfo[1]) + " " + str(self.coPilotInfo[2]))


    def getData(self):
        userTuple = self.parent.getInfo()

        return userTuple

    def compareData(self):
        conn = connectToDB()
        cur = conn.cursor()

        cur.execute('SELECT * FROM operations_compare_form WHERE ops_id = %s', (self.info[0],))
        result = cur.fetchall()

        return(result[0])
    
    def getMainPilot(self):
        conn = connectToDB()
        cur = conn.cursor()

        cur.execute('SELECT * FROM user_operations WHERE ops_id = %s AND pilot_role = 0', (self.info[0],))
        result = cur.fetchall()

        self.droneID = result[0][3]

        pilot = self.getPilotInfo(result[0][0])

        return(pilot)

    def getCoPilot(self):
        conn = connectToDB()
        cur = conn.cursor()

        cur.execute('SELECT * FROM user_operations WHERE ops_id = %s AND pilot_role = 1', (self.info[0],))
        result = cur.fetchall()

        pilot = self.getPilotInfo(result[0][0])

        return(pilot)
    
    def getPilotInfo(self,pilotID):
        conn = connectToDB()
        cur = conn.cursor()

        cur.execute('SELECT user_id, first_name, last_name FROM users WHERE user_id = %s', (pilotID,))
        result = cur.fetchall()
        print(result[0])

        return (result[0])
