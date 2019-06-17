# Objects to hold data

from PyQt5 import QtWidgets, QtGui, QtCore

class Profile(object):
    # constants for people categories
    CATEGORY_STUDENT = 0
    CATEGORY_ALUMNI = 1
    CATEGORY_MENTOR = 2
    CATEGORY_TEACHER = 3
    CATEGORY_TEAM = 4
    CATEGORY_OTHER = 5

    ID = ""
    name = ""
    picture_path = ""
    pixmap_scaled = None
    category = -1
    isStudent = bool()

    def __init__(self, ID, name, picture_path, category):
        self.ID = ID
        self.name = name
        self.picture_path = picture_path
        self.category = category
        self.isStudent = category == self.CATEGORY_STUDENT

    def create_groupBox(self):
        try:
            picture_label = QtWidgets.QLabel()

            # set maximum size of picture label
            picture_label.setMaximumSize(150, 150)

            # associate label with picture
            picture_label.setPixmap(self.pixmap_scaled)

            # set label alignment to center
            picture_label.setAlignment(QtCore.Qt.AlignHCenter)

            # create label for name and ID
            personLabel = QtWidgets.QLabel(self.name + " (" + self.ID + ")")
            personLabel.setAlignment(QtCore.Qt.AlignCenter)
            personLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
            vbox.addWidget(picture_label)
            vbox.addWidget(personLabel)
            vbox.addStretch(1)

            # groupBox will hold the widgets together
            self.groupBox = QtWidgets.QGroupBox()

            # add vbox to groupBox
            self.groupBox.setLayout(vbox)

            return self.groupBox
        except Exception as e:
            print(e)

    def construct_pixmap(self):

        picture_label = QtWidgets.QLabel()

        # set maximum size of picture label for reference
        picture_label.setMaximumSize(150, 150)

        # create pixmap
        pixmap_raw = QtGui.QPixmap(self.picture_path)

        # scale pixmap with constant aspect ratio to match picture label
        self.pixmap_scaled = pixmap_raw.scaled(picture_label.size(), QtCore.Qt.KeepAspectRatio)


class LogEntry(object):
    ID = ""
    login_time = -1
    logout_time = -1

    def __init__(self, ID, login_time, logout_time):
        self.ID = ID
        self.login_time = login_time
        self.logout_time = logout_time


class Constants(object):

    STUDENT_TABLE_ROWS = 4
    STUDENT_TABLE_COLUMNS = 9

    MENTOR_TABLE_ROWS = 2
    MENTOR_TABLE_COLUMNS = 9
