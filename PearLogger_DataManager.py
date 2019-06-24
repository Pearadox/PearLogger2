# files and data structures are accessed here by the core
import time
from pathlib import Path
import re

from PearLogger_Utils import Profile, LogEntry, Constants


class DataManager(object):
    peopleDict = dict()  # k: ID number  v: profile object
    log = list()  # list of logEntry objects
    loggedTime = dict()  # k: ID number  v: total logged time (seconds)
    loggedIn = dict()  # k: ID number  v: login time (epoch)
    config = dict()  # k: config name  v: config entry

    newIDs = list()  # list of newly added IDs, prevents ID reuse

    latest_known_time = 0

    def initialize(self):
        self.readPeople()
        self.readLog()
        self.readLoggedIn()
        self.readConfig()

    def readPeople(self):
        # open file
        people_file = Path("data/people.pear")

        # create file if it doesn't exist
        if not people_file.exists():
            #  create new people file
            file = open("data/people.pear", 'w')

            #  write in example data
            file.write("0;example name;example_picture.jpg;0")
            file.close()

        # process people into dictionary
        with open("data/people.pear") as inf:
            # keep track of current line for error message
            lineCount = 0
            for line in inf:
                lineCount += 1

                # parse through data in each line
                try:
                    raw = str.strip(line)
                    delimited = re.split(';', raw)
                    ID = str.strip(delimited[0])
                    name = str.strip(delimited[1])
                    picture_path = Path("data/profilepics/" + str.strip(delimited[2]))
                    category = int(str.strip(delimited[3]))

                    # make sure picture works or is not empty. otherwise use default
                    if (len(str(picture_path)) is len('data\profilepics')) or (not picture_path.exists()):
                        picture_path = Path('data/profilepics/default.jpg')

                    # check if number already exists in dictionary
                    if ID in self.peopleDict.keys():
                        # ID already exists, skip line
                        print(
                            "ERROR: Duplicate IDs in people file (#" + ID + ") (data/people.pear, line " + str(
                                lineCount) + ")")
                        continue

                    # record the data
                    self.peopleDict[ID] = Profile(ID, name, str(picture_path), category)

                    # add loggedTime entry
                    self.loggedTime[ID] = 0
                except Exception as e:
                    print(e)
                    print("ERROR: Parsing error in people file (data/people.pear, line " + str(lineCount) + ")")
        print("Loaded data/people.pear")

    def appendDirectory(self, ID, name, picture_path, category):
        with open("data/people.pear", "a") as peopleFile:
            peopleFile.write(ID + ";" + name + ";" + picture_path + ";" + str(category) + "\n")
            peopleFile.close()

        print("Appended data/people.pear")

    def addPerson(self, name, category, picture_path, initialized_main_backEnd):
        try:
            # find an ID, loop from id start to id end of category
            new_ID = int()
            for new_ID in range(Profile.CATEGORY__ID_START_DICTIONARY[category],
                                Profile.CATEGORY__ID_START_DICTIONARY[category]
                                + Profile.CATEGORY__ID_RANGE_DICTIONARY[category]):
                # make sure ID is unused
                if (str(new_ID) not in self.peopleDict.keys()) and (new_ID not in self.newIDs):
                    # add to list since new IDs aren't added to the directory dictionary
                    self.newIDs.append(new_ID)
                    break

            print("Adding " + name + " (" + str(new_ID) + ") to people file")

            # add to directory file
            self.appendDirectory(str(new_ID), name, picture_path, category)

            #
            initialized_main_backEnd.showInfo_popup(
                "Profile Created", (name + " (ID #" + str(new_ID) + ") has been added to the directory.\n\n "
                                                                    "Please restart PearLogger to use new profiles."))
        except Exception as e:
            print(e)

    # reads in log file
    def readLog(self):
        # open file
        log_file = Path("data/log.pear")

        # create file if it doesn't exist
        if not log_file.exists():
            #  create new people file
            file = open("data/log.pear", 'w')
            file.close()

        # process logs
        with open("data/log.pear") as inf:
            # keep track of current line for error message
            lineCount = 0
            for line in inf:
                lineCount += 1

                # parse through data in each line
                try:
                    raw = str.strip(line)
                    delimited = re.split(';', raw)
                    ID = str.strip(delimited[0])
                    login_time = int(str.strip(delimited[1]))
                    logout_time = int(str.strip(delimited[2]))

                    self.latest_known_time = max(logout_time, self.latest_known_time)

                    # record the data
                    self.log.append(LogEntry(ID, login_time, logout_time))

                    # calculate and add logged hours to logged dictionary
                    # create ID entry if it doesn't exist yet
                    if ID not in self.loggedTime.keys():
                        self.loggedTime[ID] = 0

                    # add dt to logged
                    self.loggedTime[ID] += logout_time - login_time

                except:
                    print("ERROR: Parsing error in log file (data/log.pear, line " + str(lineCount) + ")")
        print("Loaded data/log.pear")

    # add log entry to end of log file
    def appendLog(self, ID, login_time, logout_time):
        with open("data/log.pear", "a") as logFile:
            logFile.write(ID + ";" + str(login_time) + ";" + str(logout_time) + "\n")
            logFile.close()

        print("Appended data/log.pear")

    # read currently logged in file
    def readLoggedIn(self):
        # open file
        loggedIn_file = Path("data/loggedIn.pear")

        # create file if it doesn't exist
        if not loggedIn_file.exists():
            #  create new people file
            file = open("data/loggedIn.pear", 'w')
            file.close()

        # process logs
        with open("data/loggedIn.pear") as inf:
            # keep track of current line for error message
            lineCount = 0
            for line in inf:
                lineCount += 1

                # parse through data in each line
                try:
                    raw = str.strip(line)
                    delimited = re.split(';', raw)
                    ID = str.strip(delimited[0])
                    login_time = int(str.strip(delimited[1]))

                    self.latest_known_time = max(login_time, self.latest_known_time)

                    # check for login duplicates
                    if ID in self.loggedIn.keys():
                        # ID already exists, skip line
                        print(
                            "ERROR: Duplicate IDs in loggedIn file (#" + ID + ") (data/loggedIn.pear, line " + str(
                                lineCount) + ")")
                        continue

                    # record the data
                    self.loggedIn[ID] = login_time
                except:
                    print("ERROR: Parsing error in loggedIn file (data/loggedIn.pear, line " + str(lineCount) + ")")
        print("Loaded data/loggedIn.pear")

    # updates logged in file
    def rewriteLoggedIn(self):
        # open file
        loggedIn_file = open("data/loggedIn.pear", 'w')
        for ID, login_time in self.loggedIn.items():
            loggedIn_file.write(ID + ";" + str(login_time) + "\n")
        print("Rewrote data/loggedIn.pear")

    def readConfig(self):
        # open file
        config_file = Path("data/config.pear")

        # create file if it doesn't exist
        if not config_file.exists():
            #  create new people file
            file = open("data/config.pear", 'w')

            #  write in default data
            file.write("Shortest_Time_Allowed=00:00:00\n" +
                        "Longest_Time_Allowed=12:00:00\n" +
                        "Earliest_Time_Allowed=08:00:00\n" +
                        "Latest_Time_Allowed=00:00:00\n" +
                        "Enable_Time_Limit=0\n" +
                        "Enable_Time_Window=0\n" +
                        "Leaderboard_Visible_Categories=0,1,2,3,4,5,6,7")
            file.close()

        # process people into dictionary
        with open("data/config.pear") as inf:
            # keep track of current line for error message
            lineCount = 0
            for line in inf:
                lineCount += 1
                try:
                    # parse through data in each line
                    raw = str.strip(line)
                    delimited = re.split('=', raw)
                    config_key = str.strip(delimited[0])
                    config_value = str.strip(delimited[1])

                    # record the config
                    self.config[config_key] = config_value
                except Exception as e:
                    print(e)
                    print("ERROR: Parsing error in config file (data/config.pear, line " + str(lineCount) + ")")
        print("Loaded data/config.pear")

    # updates config file
    def rewriteConfig(self):
        # open file
        config_file = open("data/config.pear", 'w')
        for config_key, config_value in self.config.items():
            config_file.write(str(config_key) + "=" + str(config_value) + "\n")
        print("Rewrote data/config.pear")
