# core functionality of PearLogger
import copy
import re
import time, datetime
from PearLogger_DataManager import DataManager
from PearLogger_Utils import Constants, inBetween, getCurrentTime

MONTH = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December')
WEEKDAY = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

studentTableOrder = list()  # list of Profiles, parallel with studentTable boxes order
mentorTableOrder = list()  # list of Profiles, parallel with mentorTable boxes order

class Core(object):

    dm = DataManager()

    # initializes data manager object
    def initialize_DataManager(self):
        self.dm.initialize()

    # this must be done after app object created in ui
    def initialize_IDBoxes(self):
        for ID, profile in self.dm.peopleDict.items():
            profile.construct_pixmap()

    # initializes previous logins
    def initialize_previous_logins(self):
        for ID in self.dm.loggedIn.keys():
            self.add_box(self.dm.peopleDict[ID])

    # logs person in or out
    def log(self, ID, logTime=True):
        # make sure ID exists in system
        if ID in self.dm.peopleDict.keys():
            # get current time
            currentTime = getCurrentTime()
            print(currentTime)

            # get profile
            profile = self.dm.peopleDict[ID]

            # get configs
            enable_time_limit_config = self.dm.config['Enable_Time_Limit'] is '1'
            enable_time_window_config = self.dm.config['Enable_Time_Window'] is '1'
            time_limit_minimum_config = float(self.dm.config['Minimum_Hours'])
            time_limit_maximum_config = float(self.dm.config['Maximum_Hours'])
            open_delimited = re.split(':', self.dm.config['Window_Open'])
            close_delimited = re.split(':', self.dm.config['Window_Close'])
            time_window_open_seconds_config = int(open_delimited[0]) * 3600 + int(open_delimited[1]) * 60
            time_window_close_seconds_config = int(close_delimited[0]) * 3600 + int(close_delimited[1]) * 60

            # choose whether to login or logout
            if ID in self.dm.loggedIn.keys():
                # logout
                print("Logging out " + ID)

                current_session_logged_time = currentTime - self.dm.loggedIn[ID]

                # apply config settings
                # calculate logout time relative to start time
                logout_time_relative = currentTime % (24 * 3600)
                if enable_time_window_config and not inBetween(
                        logout_time_relative, time_window_open_seconds_config, time_window_close_seconds_config):

                    # limit logout time
                    print("Limiting log time (window)")
                    if logout_time_relative > time_window_close_seconds_config:
                        # same day
                        limited_logout_time = currentTime - (logout_time_relative - time_window_close_seconds_config)
                    else:
                        # new day
                        limited_logout_time = currentTime - (
                                (24 * 3600) - (time_window_close_seconds_config - logout_time_relative))

                    print(str(currentTime-limited_logout_time))

                if enable_time_limit_config:
                    if current_session_logged_time > time_limit_maximum_config:
                        # logged in too long, only log max time
                        print("Limiting log time (limit, long)")
                        current_session_logged_time = time_limit_maximum_config
                    elif current_session_logged_time < time_limit_minimum_config:
                        # not logged in long enough, don't record time
                        print("Blocking log time (limit, short)")
                        logTime = False

                if logTime:
                    # Record logged hours

                    # create ID entry for logging times if it doesn't exist yet
                    if ID not in self.dm.loggedTime.keys():
                        self.dm.loggedTime[ID] = 0
                    # add dt to logged
                    self.dm.loggedTime[ID] += current_session_logged_time

                    # add time to log
                    self.dm.appendLog(ID, self.dm.loggedIn[ID], currentTime)

                # remove ID from loggedIn dictionary
                self.dm.loggedIn.pop(ID, None)

                # update loggedIn file
                self.dm.rewriteLoggedIn()

                # remove ID box from GUI Table
                self.remove_box(profile)

                # update leaderboard
                self.updateLeaderboard()
            else:
                # login
                print("Logging in " + ID)

                # check if too early to sign in
                login_time_relative = currentTime % (24 * 3600)
                if not inBetween(
                        login_time_relative, time_window_open_seconds_config, time_window_close_seconds_config):
                    print("Blocking login (window, too early)")
                    self.showErrorMessage("Error: Login time too early! Change config or sync sys time.")
                    return False

                # add current time to loggedIn dictionary
                self.dm.loggedIn[ID] = currentTime

                # update loggedIn file
                self.dm.rewriteLoggedIn()

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
            row = int((len(studentTableOrder) - 1) / Constants.STUDENT_TABLE_COLUMNS)
            column = int((len(studentTableOrder) - 1) % Constants.STUDENT_TABLE_COLUMNS)
        else:
            mentorTableOrder.append(profile)
            # choose what coordinates to put picture in
            row = int((len(mentorTableOrder) - 1) / Constants.MENTOR_TABLE_COLUMNS)
            column = int((len(mentorTableOrder) - 1) % Constants.MENTOR_TABLE_COLUMNS)

        # add rows if needed
        if row >= (backEnd.student_table_rows if profile.isStudent else backEnd.mentor_table_rows):
            print(str(row) + " " + str(backEnd.mentor_table_rows))
            backEnd.add_row_student() if profile.isStudent else backEnd.add_row_mentor()
        backEnd.setIDBox(profile.create_groupBox(), profile.isStudent, row, column)

    # logs out person, but does not log hours
    def clearHours(self, ID):
        # make sure person is still signed in
        if ID in self.dm.loggedIn.keys():
            # log person out, but pass in boolean to NOT log hours
            self.log(ID, False)

    # clear hours for all logged in people
    def clearAll(self):
        # get copy of dictionary so keys() dont change
        dict_copy = copy.deepcopy(self.dm.loggedIn)
        for ID in dict_copy.keys():
            self.clearHours(ID)

    # signs out all logged in peopl
    def signoutAll(self):
        # get copy of dictionary so keys() dont change
        dict_copy = copy.deepcopy(self.dm.loggedIn)
        for ID in dict_copy.keys():
            self.log(ID)

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

        # remove unnecessary lines
        if column is 0 and row >= (Constants.STUDENT_TABLE_ROWS if profile.isStudent else Constants.MENTOR_TABLE_ROWS):
            backEnd.remove_row_student() if profile.isStudent else backEnd.remove_row_mentor()

        # update list to match
        studentTableOrder.remove(profile) if profile.isStudent else mentorTableOrder.remove(profile)

    def updateLeaderboard(self):
        from PearLogger_UI import backEnd

        # sorts times in reverse order, gives a list of tuples ([0]=ID, [1]=time)
        sortedTimes = sorted(self.dm.loggedTime.items(), key=lambda kv: kv[1], reverse=True)

        # keep track of ranks
        rank = 1

        # need max time to determine bar sizes
        top_time = 0

        # get leaderboard filter configuration
        # add leaderboard visiblitiy config entry if it doesn't exist
        if 'Leaderboard_Visible_Categories' not in self.dm.config.keys():
            self.dm.config['Leaderboard_Visible_Categories'] = '1,2,3,11,12,13,21,22'

        # get list config of visible boxes
        visible_categories = re.split(',', self.dm.config['Leaderboard_Visible_Categories'])

        # clear leaderboard
        backEnd.clearLeaderboard()

        for tup in sortedTimes:
            # only take top 10
            if rank > 10:
                break

            # log file error check: nonexistent ID
            if tup[0] not in self.dm.peopleDict:
                print("ERROR: Non Existent ID in Log (" + tup[0] + ")")
                continue

            # get profile with ID
            profile = self.dm.peopleDict[tup[0]]

            # check for filter
            if str(profile.category) not in visible_categories:
                continue

            # calculate hours
            hours = tup[1]/3600

            # set max time if top rank
            if rank is 1:
                top_time = hours

            # send values to leaderboard backend
            backEnd.setLeaderboard(rank, profile.name, hours, top_time)

            # increase rank by 1 for next loop
            rank += 1

    def add_person(self, name, category, picture_path, graduation_year, initialized_main_backEnd):
        # send to data manager
        self.dm.addPerson(name, category, picture_path, graduation_year, initialized_main_backEnd)

    def check_bad_time_change(self):
        # check for bad time change
        if self.dm.latest_known_time > time.time():
            from PearLogger_UI import backEnd
            message = "Current time (" + str(int(time.time())) + \
                      ") is earlier than latest time (" + str(self.dm.latest_known_time) + ")!"
            print(message)
            backEnd.showError_popup("Time Change Error", message)

    def showErrorMessage(self, message):
        from PearLogger_UI import showErrorMessage_caller
        showErrorMessage_caller(message)

