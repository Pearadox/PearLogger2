# front and back end GUI
import time

from PyQt5 import QtCore, QtGui, QtWidgets

from GUI.GUIViewHoursDialog import Ui_ViewHours_Dialog
from PearLogger_Utils import Profile


# Manages user interaction with GUI, passes on logistics to Core class
class View_Hours_Ui_backEnd(object):

    ranks = dict()


    def initialize(self):
        # create sorted time list of tuples
        self.sortedTimes = sorted(dm.loggedTime.items(), key=lambda kv: kv[1], reverse=True)

        # create keyword model for search function
        self.create_model()

        # assign ranks
        self.assignRanks()

        # populate table with everything
        self.populateTable()

    # gets called when something is typed in the search bar
    def lineEdit_textChanged(self):
        self.populateTable(frontEnd.ui.lineEdit.text())

    def assignRanks(self):
        # loop through sorted times
        row = 0
        for (ID, time) in self.sortedTimes:
            self.ranks[ID] = row + 1
            row += 1

    def populateTable(self, search = ""):
        # clear table
        self.reset_table()

        # keep track of row number
        row = 0

        # keep track of number skipped to reduce row count later
        skipped = 0

        # set row count to number of entries
        frontEnd.ui.tableWidget.setRowCount(len(self.sortedTimes))

        # loop through sorted times
        for (ID, time) in self.sortedTimes:
            # get profile
            profile = dm.peopleDict[ID]

            # get name for filtering
            name = profile.name

            # filter, skip if no keyword query
            if search != "":
                try:
                    # try to find search inside name
                    str(name).lower().index(search.lower())
                except:
                    # search not found inside name, try ID
                    try:
                        str(ID).index(search)
                    except:
                        # not found, continue loop
                        skipped += 1
                        continue

            # create labels and customize them
            rank_label = QtWidgets.QLabel(str(self.ranks[ID]) + "  ")
            rank_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

            name_label = QtWidgets.QLabel(name + "  ")
            name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

            time_label = QtWidgets.QLabel(self.to_timestamp(time) + "  ")
            time_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

            ID_label = QtWidgets.QLabel(ID + "  ")
            ID_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

            category_label = QtWidgets.QLabel(Profile.CATEGORY__DICTIONARY.get(profile.category) + "  ")
            category_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

            frontEnd.ui.tableWidget.setCellWidget(row, 0, rank_label)
            frontEnd.ui.tableWidget.setCellWidget(row, 1, name_label)
            frontEnd.ui.tableWidget.setCellWidget(row, 2, time_label)
            frontEnd.ui.tableWidget.setCellWidget(row, 3, ID_label)
            frontEnd.ui.tableWidget.setCellWidget(row, 4, category_label)

            row += 1

        # remove skipped rows
        frontEnd.ui.tableWidget.setRowCount(len(self.sortedTimes)-skipped)

    # creates keyword model for search
    def create_model(self):
        self.keywords = []

        # loop through sortedTimes to get all the IDs (we don't really need the time)
        for (ID, time) in self.sortedTimes:
            # also add the name
            name = dm.peopleDict[ID].name
            self.keywords.append(ID)
            self.keywords.append(name)

    def reset_table(self):
        # clear table
        frontEnd.ui.tableWidget.clear()

        # add table column labels back
        frontEnd.ui.tableWidget.setHorizontalHeaderLabels(['Rank', 'Name', 'Logged Time', 'ID', 'Category'])

    def to_timestamp(self, seconds):
        return time.strftime('%H:%M:%S', time.gmtime(seconds))


class View_Hours_Ui_frontEnd(object):

    def post_initialization_tasks(self):
        backEnd.initialize()

    # constructor, initialize UI
    def initialize(self, dataManager):
        global dm, frontEnd
        dm = dataManager
        frontEnd = self

        self.ViewHoursDialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint
                                            | QtCore.Qt.WindowCloseButtonHint)
        self.ui = Ui_ViewHours_Dialog()
        self.ui.setupUi(self.ViewHoursDialog)

        self.customConfiguration()
        self.post_initialization_tasks()

        self.ViewHoursDialog.exec_()

    # custom UI configurations
    def customConfiguration(self):
        # focus on line edit
        self.ui.lineEdit.setFocus(True)

        self.ViewHoursDialog.setFixedHeight(620)
        self.ViewHoursDialog.setFixedWidth(650)

        # text changed action for lineEdit
        self.ui.lineEdit.textChanged.connect(backEnd.lineEdit_textChanged)

        # change column widths individually
        self.ui.tableWidget.setColumnWidth(0, 45)  # rank
        self.ui.tableWidget.setColumnWidth(1, 180)  # name
        self.ui.tableWidget.setColumnWidth(2, 100)  # logged time
        self.ui.tableWidget.setColumnWidth(3, 100)  # ID
        self.ui.tableWidget.setColumnWidth(4, 80)  # Category

frontEnd = None
dm = None
backEnd = View_Hours_Ui_backEnd()