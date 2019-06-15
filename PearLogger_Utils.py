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
    picture_label = None
    category = -1

    # group box for table display
    groupBox = None

    def __init__(self, ID, name, picture_path, category):
        self.ID = ID
        self.name = name
        self.picture_path = picture_path
        self.category = category

        # construct picture label
        self.construct_picture_label()

        # construct entire groupBox
        self.construct_groupBox()

    def construct_groupBox(self):
        try:
            self.groupBox = QtWidgets.QGroupBox()

            # create label for name and ID
            personLabel = QtWidgets.QLabel(self.name + " (" + self.ID + ")")
            personLabel.setAlignment(QtCore.Qt.AlignCenter)
            personLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

           # put name/ID label and picture label together in one vertical box container
            vbox = QtWidgets.QVBoxLayout()
            vbox.addWidget(self.picture_label)
            vbox.addWidget(personLabel)
            vbox.addStretch(1)
            self.groupBox.setLayout(vbox)  # add the vbox to groupbox
        except Exception as e:
            print(e)

    def construct_picture_label(self):

        self.picture_label = QtWidgets.QLabel()

        # set maximum size of picture label
        self.picture_label.setMaximumSize(150,150)

        # create pixmap
        pixmap_raw = QtGui.QPixmap(self.picture_path)

        # scale pixmap with constant aspect ratio to match picture label
        pixmap_scaled = pixmap_raw.scaled(self.picture_label.size(), QtCore.Qt.KeepAspectRatio)

        # associate label with picture
        self.picture_label.setPixmap(pixmap_scaled)


class LogEntry(object):
    ID = ""
    login_time = -1
    logout_time = -1

    def __init__(self, ID, login_time, logout_time):
        self.ID = ID
        self.login_time = login_time
        self.logout_time = logout_time
