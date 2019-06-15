# core functionality of PearLogger

import time, datetime
from PearLogger_DataManager import DataManager
from PyQt5 import QtWidgets

MONTH = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December')
WEEKDAY = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

dm = DataManager()

class Core(object):

    def initialize(self):
        picture_label = QtWidgets.QLabel()
        dm.initialize()

    def log(self, ID):
        if ID in dm.peopleDict.keys():
            # get current epoch time
            currentTime = int(time.time())

            # choose whether to login or logout
            if ID in dm.loggedIn.keys():
                # logout
                # add time to log
                dm.appendLog(ID, dm.loggedIn[ID], currentTime)

                # calculate and record logged hours
                # create ID entry if it doesn't exist yet
                if ID not in dm.logged.keys():
                    dm.logged[ID] = 0
                # add dt to logged
                dm.logged[ID] += currentTime - dm.loggedIn[ID]

                # remove ID from loggedIn dictionary
                dm.loggedIn.pop(ID, None)

                # update loggedIn file
                dm.rewriteLoggedIn()

                pass
            else:
                # login
                # add current time to loggedIn dictionary
                dm.loggedIn[ID] = currentTime

                # update loggedIn file
                dm.rewriteLoggedIn()

                from PearLogger_UI import backEnd
                backEnd.createIDBox(dm.peopleDict[ID].groupBox, True, 0, 0)

            # successful
            return True
        else:
            # ID does not exist
            self.showErrorMessage("Error: ID does not exist")
            # unsuccessful
            return False

    def showErrorMessage(self, message):
        from PearLogger_UI import showErrorMessage_Caller
        showErrorMessage_Caller(message)

