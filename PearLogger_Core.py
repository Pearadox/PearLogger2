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

    # initializes data manager object
    def initialize_DataManager(self):
        dm.initialize()

    # this must be done after app object created in ui
    def initialize_IDBoxes(self):
        for ID, profile in dm.peopleDict.items():
            profile.construct_pixmap()

    # initializes previous logins
    def initialize_previous_logins(self):
        for ID in dm.loggedIn.keys():
            self.add_box(dm.peopleDict[ID])

    # logs person in or out
    def log(self, ID):
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

                # calculate and record logged hours
                # create ID entry for logging times if it doesn't exist yet
                if ID not in dm.loggedTime.keys():
                    dm.loggedTime[ID] = 0
                # add dt to logged
                dm.loggedTime[ID] += currentTime - dm.loggedIn[ID]

                # add time to log
                dm.appendLog(ID, dm.loggedIn[ID], currentTime)

                # remove ID from loggedIn dictionary
                dm.loggedIn.pop(ID, None)

                # update loggedIn file
                dm.rewriteLoggedIn()

                # remove ID box from GUI Table
                self.remove_box(profile)

                # update leaderboard
                self.updateLeaderboard()
            else:
                # login
                print("Logging in " + ID)

                # add current time to loggedIn dictionary
                dm.loggedIn[ID] = currentTime

                # update loggedIn file
                dm.rewriteLoggedIn()

                # add ID box to GUI Table
                self.add_box(profile)

            # successful
            return True
        else:
            # ID does not exist
            self.showErrorMessage("Error: ID does not exist")
            # unsuccessful
            return False

    # add ID box to GUI Table
    def add_box(self, profile):
        from PearLogger_UI import backEnd

        # choose which table to add picture to
        if profile.isStudent:
            studentTableOrder.append(profile)
            # choose what coordinates to put picture in
            row = (len(studentTableOrder) - 1) / Constants.STUDENT_TABLE_COLUMNS
            column = (len(studentTableOrder) - 1) % Constants.STUDENT_TABLE_COLUMNS
        else:
            mentorTableOrder.append(profile)
            # choose what coordinates to put picture in
            row = (len(mentorTableOrder) - 1) / Constants.MENTOR_TABLE_COLUMNS
            column = (len(mentorTableOrder) - 1) % Constants.MENTOR_TABLE_COLUMNS

        backEnd.setIDBox(profile.create_groupBox(), profile.isStudent, row, column)

    # remove ID box from GUI Table
    def remove_box(self, profile):
        from PearLogger_UI import backEnd

        # find coordinates to remove picture from
        index = studentTableOrder.index(profile) if profile.isStudent else mentorTableOrder.index(profile)

        # remove picture and shift other pictures down
        while index < len(studentTableOrder if profile.isStudent else mentorTableOrder) - 1:
            # get profile of next person to shift down
            newProfile = studentTableOrder[index + 1] if profile.isStudent else mentorTableOrder[index + 1]

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


    def updateLeaderboard(self):
        # sorts times in reverse order, gives a list of tuples ([0]=ID, [1]=time)
        sortedTimes = sorted(dm.loggedTime.items(), key=lambda kv: kv[1], reverse=True)

        # keep track of ranks
        rank = 1
        for tup in sortedTimes:
            # get profile with ID
            profile = dm.peopleDict[tup[0]]

            # calculate hours
            hours = tup[1]/3600



            rank += 1

    def showErrorMessage(self, message):
        from PearLogger_UI import showErrorMessage_Caller
        showErrorMessage_Caller(message)

