# core functionality of PearLogger
import copy
import time, datetime
from PearLogger_DataManager import DataManager
from PearLogger_Utils import Profile, Constants
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
            profile.construct_pixmap()

    # logs person in or out
    def log(self, ID):
        from PearLogger_UI import backEnd

        # make sure ID exists in system
        if ID in dm.peopleDict.keys():
            # get current epoch time
            currentTime = int(time.time())

            # get profile
            profile = dm.peopleDict[ID]

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

                # find coordinates to remove picture from
                index = studentTableOrder.index(profile) if profile.isStudent else mentorTableOrder.index(profile)

                # remove picture and shift other pictures down
                while index < len(studentTableOrder if profile.isStudent else mentorTableOrder)-1:
                    # get profile of next person to shift down
                    newProfile = studentTableOrder[index+1] if profile.isStudent else mentorTableOrder[index+1]

                    # calculate row and column of current box
                    row = int(index / Constants.STUDENT_TABLE_COLUMNS)
                    column = int(index % Constants.STUDENT_TABLE_COLUMNS)

                    # shift next person down to current box
                    backEnd.setIDBox(newProfile.create_groupBox(), profile.isStudent, row, column)
                    index += 1

                # delete last box
                row = int(index / Constants.STUDENT_TABLE_COLUMNS)
                column = int(index % Constants.STUDENT_TABLE_COLUMNS)
                backEnd.removeIDBox(profile.isStudent, row, column)

                # update list to match
                studentTableOrder.remove(profile) if profile.isStudent else mentorTableOrder.remove(profile)
            else:
                # login
                print("Logging in " + ID)

                # add current time to loggedIn dictionary
                dm.loggedIn[ID] = currentTime

                # update loggedIn file
                dm.rewriteLoggedIn()

                # add ID box to GUI Table

                # choose which table to add picture to
                if profile.isStudent:
                    studentTableOrder.append(profile)
                    # choose what coordinates to put picture in
                    row = (len(studentTableOrder)-1) / Constants.STUDENT_TABLE_COLUMNS
                    column = (len(studentTableOrder)-1) % Constants.STUDENT_TABLE_COLUMNS
                else:
                    mentorTableOrder.append(profile)
                    # choose what coordinates to put picture in
                    row = (len(mentorTableOrder)-1) / Constants.MENTOR_TABLE_COLUMNS
                    column = (len(mentorTableOrder)-1) % Constants.MENTOR_TABLE_COLUMNS

                backEnd.setIDBox(profile.create_groupBox(), profile.isStudent, row, column)

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

