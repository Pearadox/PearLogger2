# core functionality of PearLogger

import time, datetime
from PearLogger_DataManager import DataManager
from PearLogger_Utils import Profile
from PyQt5 import QtWidgets

MONTH = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December')
WEEKDAY = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

dm = DataManager()

studentTableOrder = list()  # list of Profiles, parallel with studentTable boxes order
mentorTableOrder = list()  # list of Profiles, parallel with mentorTable boxes order

class Core(object):

    def initialize_DataManager(self):
        dm.initialize()

    # this must be done after app object created in ui
    def initialize_IDBoxes(self):
        for ID, profile in dm.peopleDict.items():
            profile.construct_picture_label()
            profile.construct_groupBox()

    # logs person in or out
    def log(self, ID):
        from PearLogger_UI import backEnd

        if ID in dm.peopleDict.keys():
            # get current epoch time
            currentTime = int(time.time())

            # choose whether to login or logout
            if ID in dm.loggedIn.keys():
                # logout
                print("Logging out " + ID)

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

                # remove ID box from GUI Table


            else:
                # login
                print("Logging in " + ID)

                # add current time to loggedIn dictionary
                dm.loggedIn[ID] = currentTime

                # update loggedIn file
                dm.rewriteLoggedIn()

                # add ID box to GUI Table

                # check if student to see which table to put ID box in
                isStudent = dm.peopleDict[ID].category == Profile.CATEGORY_STUDENT
                backEnd.createIDBox(dm.peopleDict[ID].groupBox, isStudent, 0, 0)

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

