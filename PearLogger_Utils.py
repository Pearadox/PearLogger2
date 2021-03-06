# Objects to hold data
import datetime

from PyQt5 import QtWidgets, QtGui, QtCore


class Constants(object):

    STUDENT_TABLE_ROWS = 4
    STUDENT_TABLE_COLUMNS = 9

    MENTOR_TABLE_ROWS = 2
    MENTOR_TABLE_COLUMNS = 9

    ID_START_ALUMNI = 500
    ID_RANGE_ALUMNI = 500
    ID_START_MENTOR = 100
    ID_RANGE_MENTOR = 100
    ID_START_TEACHER = 200
    ID_RANGE_TEACHER = 100
    ID_START_TEAM = 300
    ID_RANGE_TEAM = 100
    ID_START_OTHER = 4000
    ID_RANGE_OTHER = 1000


class Profile(object):

    # constants for people categories
    CATEGORY_STUDENT_DAWSON = 1
    CATEGORY_STUDENT_PEARLAND = 2
    CATEGORY_STUDENT_TURNER = 3
    CATEGORY_ALUMNI = 11
    CATEGORY_MENTOR = 12
    CATEGORY_TEACHER = 13
    CATEGORY_TEAM = 21
    CATEGORY_OTHER = 22

    NUM_CATEGORIES = 8

    CATEGORY__DICTIONARY = {
        1: "Student (Dawson)",
        2: "Student (Pearland)",
        3: "Student (Turner)",
        11: "Alumni",
        12: "Mentor",
        13: "Teacher",
        21: "Team",
        22: "Other"
    }

    CATEGORY__ID_START_DICTIONARY = {
        11: Constants.ID_START_ALUMNI,
        12: Constants.ID_START_MENTOR,
        13: Constants.ID_START_TEACHER,
        21: Constants.ID_START_TEAM,
        22: Constants.ID_START_OTHER
    }

    CATEGORY__ID_RANGE_DICTIONARY = {
        11: Constants.ID_RANGE_ALUMNI,
        12: Constants.ID_RANGE_MENTOR,
        13: Constants.ID_RANGE_TEACHER,
        21: Constants.ID_RANGE_TEAM,
        22: Constants.ID_RANGE_OTHER
    }

    CATEGORY__SCHOOL_DICTIONARY = {
        1: '0',
        2: '2',
        3: '1'
    }

    ID = ""
    name = ""
    picture_path = ""
    pixmap_scaled = None
    category = -1
    isStudent = bool()

    pixmap_width = 120
    pixmap_height = 120

    def __init__(self, ID, name, picture_path, category):
        self.ID = ID
        self.name = name
        self.picture_path = picture_path
        self.category = category
        self.isStudent = category == self.CATEGORY_STUDENT_DAWSON \
                         or category == self.CATEGORY_STUDENT_PEARLAND \
                         or category == self.CATEGORY_STUDENT_TURNER

    def create_groupBox(self):
        try:
            picture_label = QtWidgets.QLabel()

            # configure picture label
            picture_label.setMaximumSize(self.pixmap_width, self.pixmap_height)

            # associate label with picture
            picture_label.setPixmap(self.pixmap_scaled)

            # set label alignment to center
            picture_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

            # create label for name and ID
            personLabel = QtWidgets.QLabel(self.name + " (" + self.ID + ")")
            personLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
            personLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            personLabel.setWordWrap(True)
            font = QtGui.QFont()
            font.setFamily("OpenSymbol")
            font.setPointSize(10)

            personLabel.setFont(font)

            # add colors to text (student=(121, 86, 10), mentor=(10,129,10)
            if self.isStudent:
                personLabel.setStyleSheet("QLabel { color: rgb(121, 86, 10)}")
            else:
                personLabel.setStyleSheet("QLabel { color: rgb(10, 129, 10)}")

            # put name/ID label and picture label together in one vertical box container
            vbox = QtWidgets.QVBoxLayout()
            vbox.addWidget(picture_label, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
            vbox.addWidget(personLabel, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
            vbox.addStretch(1)

            # groupBox will hold the widgets together
            self.groupBox = QtWidgets.QGroupBox()

            # add vbox to groupBox
            self.groupBox.setLayout(vbox)

            return self.groupBox
        except Exception as e:
            print(e)

    # constructs a pixmap for picture label
    def construct_pixmap(self):

        # picture_label = QtWidgets.QLabel()
        #
        # # set maximum size of picture label for reference
        # picture_label.setFixedSize(self.pixmap_width, self.pixmap_height)

        # create pixmap
        pixmap_raw = QtGui.QPixmap(self.picture_path)

        # scale pixmap with constant aspect ratio to match picture label
        self.pixmap_scaled = pixmap_raw.scaled(self.pixmap_width, self.pixmap_height, QtCore.Qt.KeepAspectRatio)


class LogEntry(object):
    ID = ""
    login_time = -1
    logout_time = -1

    length = logout_time - login_time

    def __init__(self, ID, login_time, logout_time):
        self.ID = ID
        self.login_time = login_time
        self.logout_time = logout_time


# gives current epoch time but in this time zone based on system time
def getCurrentTime():
    currentTime = int((datetime.datetime.now() - datetime.datetime(1970, 1, 1)).total_seconds())
    return currentTime


# determines if a time is in between a start and end point
def inBetween(now, start, end):
    if start <= end:
        return start <= now < end
    else:  # over midnight
        return start <= now or now < end
