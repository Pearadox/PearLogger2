# files and data structures are accessed here by the core
import time
from pathlib import Path
import re

from PearLogger_Utils import Profile, LogEntry


class DataManager(object):

    peopleDict = dict()  # k: ID number  v: profile object
    log = list()  # list of logEntry objects
    loggedTime = dict()  # k: ID number  v: total logged time (seconds)
    loggedIn = dict()  # k: ID number  v: login time (epoch)

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
                    if (len(str(picture_path)) is 0) or (not picture_path.exists()):
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
                except:
                    print("ERROR: Parsing error in people file (data/people.pear, line " + str(lineCount) + ")")
        print("Loaded data/people.pear")

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
            logFile.write(ID + ";" + str(login_time) + ";" + str(logout_time)+"\n")
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
        pass