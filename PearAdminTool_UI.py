# !!!!!!!!!
#
# Ask me if you have trouble running this!!!
#
# !!!!!!!!!



# front and back end GUI
import datetime
import operator
import re
import time
from pathlib import Path

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QCheckBox

from CustomQt.ComboBoxNoScroll import ComboBoxNoScroll
from GUI import GUIAdminTool, GUIAdminToolPasswordDialog, GUIAdminToolCreateLogDialog

# Manages user interaction with GUI, passes on logistics to Core class
from PearLogger_Utils import Profile, LogEntry


class Ui_backEnd(object):
    peopleList = list()
    log = list()

    def __init__(self):
        self.IDReverseSort = True
        self.timeReverseSort = True
        self.lengthReverseSort = True

    def readLog(self):
        # open file
        log_file = Path("data/log.pear")

        # create file if it doesn't exist
        if not log_file.exists():
            #  create new people file
            file = open("data/log.pear", 'w')
            file.close()

        # process logs
        self.log.clear()
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

                    # record the data
                    self.log.append(LogEntry(ID, login_time, logout_time))

                except:
                    print("ERROR: Parsing error in log file (data/log.pear, line " + str(lineCount) + ")")
        print("Loaded data/log.pear")

    def readDirectory(self):
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
        self.peopleList.clear()
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
                    picture_path = str.strip(delimited[2])
                    category = int(str.strip(delimited[3]))

                    # record the data
                    self.peopleList.append(Profile(ID, name, picture_path, category))

                except Exception as e:
                    print(e)
                    print("ERROR: Parsing error in people file (data/people.pear, line " + str(lineCount) + ")")
        print("Loaded data/people.pear")

    def constructLogRow(self, row, LogEntry):
        loginSeconds = LogEntry.login_time
        logoutSeconds = LogEntry.logout_time

        loginDateTime = time.gmtime(loginSeconds)
        logoutDateTime = time.gmtime(logoutSeconds)

        loginDateString = str(loginDateTime.tm_mon) + '/' + str(loginDateTime.tm_mday) + '/' + str(
            loginDateTime.tm_year)
        logoutDateString = str(logoutDateTime.tm_mon) + '/' + str(logoutDateTime.tm_mday) + '/' + str(
            logoutDateTime.tm_year)
        loginTimeString = str(loginDateTime.tm_hour) + ':' + str(loginDateTime.tm_min) + ':' + str(
            loginDateTime.tm_sec)
        logoutTimeString = str(logoutDateTime.tm_hour) + ':' + str(logoutDateTime.tm_min) + ':' + str(
            logoutDateTime.tm_sec)
        deltaTimeString = str(datetime.timedelta(seconds=logoutSeconds - loginSeconds))

        delete_cbox = QCheckBox()
        ID_lEdit = QLineEdit(str(LogEntry.ID))
        dateIn_lEdit = QLineEdit(loginDateString)
        dateOut_lEdit = QLineEdit(logoutDateString)
        login_lEdit = QLineEdit(loginTimeString)
        logout_lEdit = QLineEdit(logoutTimeString)
        delta_lEdit = QLineEdit(deltaTimeString)

        ID_lEdit.setStyleSheet("border: none")
        dateIn_lEdit.setStyleSheet("border: none")
        dateOut_lEdit.setStyleSheet("border: none")
        login_lEdit.setStyleSheet("border: none")
        logout_lEdit.setStyleSheet("border: none")
        delta_lEdit.setStyleSheet("border: none")

        ID_lEdit.setReadOnly(True)
        dateIn_lEdit.setReadOnly(False)
        dateOut_lEdit.setReadOnly(False)
        login_lEdit.setReadOnly(False)
        logout_lEdit.setReadOnly(False)
        delta_lEdit.setReadOnly(True)

        ui.logTableWidget.setCellWidget(row, 0, delete_cbox)
        ui.logTableWidget.setCellWidget(row, 1, ID_lEdit)
        ui.logTableWidget.setCellWidget(row, 2, dateIn_lEdit)
        ui.logTableWidget.setCellWidget(row, 3, dateOut_lEdit)
        ui.logTableWidget.setCellWidget(row, 4, login_lEdit)
        ui.logTableWidget.setCellWidget(row, 5, logout_lEdit)
        ui.logTableWidget.setCellWidget(row, 6, delta_lEdit)

    def constructDirectoryRow(self, row, profile):
        delete_cbox = QCheckBox()
        ID_lEdit = QLineEdit(str(profile.ID))
        name_lEdit = QLineEdit(profile.name)
        picture_lEdit = QLineEdit(profile.picture_path)

        scrollArea = QtWidgets.QScrollArea()
        frmScroll = QtWidgets.QFrame(scrollArea)
        category_comboBox = ComboBoxNoScroll(frmScroll)

        index = 0
        for num, description in Profile.CATEGORY__DICTIONARY.items():
            category_comboBox.addItem(description)

            if int(profile.category) == num:
                category_comboBox.setCurrentIndex(index)
            index += 1

        ID_lEdit.setReadOnly(True)
        name_lEdit.setReadOnly(False)
        picture_lEdit.setReadOnly(False)

        ID_lEdit.setStyleSheet('border: none')
        name_lEdit.setStyleSheet('border: none')
        picture_lEdit.setStyleSheet('border: none')
        category_comboBox.setStyleSheet('border: none')

        ui.directoryTableWidget.setCellWidget(row, 0, delete_cbox)
        ui.directoryTableWidget.setCellWidget(row, 1, ID_lEdit)
        ui.directoryTableWidget.setCellWidget(row, 2, name_lEdit)
        ui.directoryTableWidget.setCellWidget(row, 3, picture_lEdit)
        ui.directoryTableWidget.setCellWidget(row, 4, category_comboBox)

    def populateLogTable(self):
        ui.logTableWidget.setRowCount(len(self.log))
        currentRow = 0
        for LogEntry in self.log:
            self.constructLogRow(currentRow, LogEntry)
            currentRow += 1

    def populateDirectoryTable(self):
        ui.directoryTableWidget.setRowCount(len(self.peopleList))
        currentRow = 0

        ui.directoryTableWidget.setColumnWidth(0, 25)
        ui.directoryTableWidget.setColumnWidth(1, 70)
        ui.directoryTableWidget.setColumnWidth(2, 250)
        ui.directoryTableWidget.setColumnWidth(3, 350)
        ui.directoryTableWidget.setColumnWidth(4, 45)

        self.peopleList.sort(key = lambda x: int(x.ID))
        for profile in self.peopleList:
            self.constructDirectoryRow(currentRow, profile)
            currentRow += 1

    def rewriteLogCall(self):
        fileBuffer = ""

        for row in range(0, ui.logTableWidget.rowCount()):
            delete = ui.logTableWidget.cellWidget(row, 0).isChecked()
            if delete: continue

            try:
                ID = ui.logTableWidget.cellWidget(row, 1).text()
                dateIn = ui.logTableWidget.cellWidget(row, 2).text()
                dateOut = ui.logTableWidget.cellWidget(row, 3).text()
                login = ui.logTableWidget.cellWidget(row, 4).text()
                logout = ui.logTableWidget.cellWidget(row, 5).text()

                login_unix = self.datetimeStringtoUnix(dateIn, login)
                logout_unix = self.datetimeStringtoUnix(dateOut, logout)

                if logout_unix < login_unix:
                    self.showError_popup("Log Table Error", "Logout time is before login time: Row " + str(row))
                    return

                if logout_unix == 0 or login_unix == 0:
                    self.showError_popup("Log Table Error",
                                         "Time not filled out (Today is not the epoch!): Row " + str(row))
                    return

                logText = str(ID) + ";" + str(login_unix) + ";" + str(logout_unix) + "\n"

                fileBuffer += logText

            except Exception as e:
                print(e)
                self.showError_popup("Log Table Error", "Error parsing log table: Row " + str(row))
                return

        log_file = open("data/log.pear", 'w')
        log_file.write(fileBuffer)
        log_file.close()
        print("Rewrote data/log.pear")
        self.showInfo_popup("Rewrite Success", "Rewrote data/log.pear")
        self.readLog()
        self.populateLogTable()

    def rewriteDirectoryCall(self):
        fileBuffer = ""

        for row in range(0, ui.directoryTableWidget.rowCount()):
            delete = ui.directoryTableWidget.cellWidget(row, 0).isChecked()
            if delete: continue

            try:
                ID = ui.directoryTableWidget.cellWidget(row, 1).text()
                name = ui.directoryTableWidget.cellWidget(row, 2).text()
                picture = ui.directoryTableWidget.cellWidget(row, 3).text()
                category = '-1'

                for num, description in Profile.CATEGORY__DICTIONARY.items():
                    selectedText = ui.directoryTableWidget.cellWidget(row, 4).currentText()

                    if selectedText == description:
                        category = str(num)
                        continue

                directoryText = ID + ";" + name + ";" + picture + ";" + category + "\n"
                fileBuffer += directoryText

            except Exception as e:
                print(e)
                self.showError_popup("Directory Table Error", "Error parsing directory table: Row " + str(row))
                return

        log_file = open("data/people.pear", 'w')
        log_file.write(fileBuffer)
        log_file.close()
        print("Rewrote data/people.pear")
        self.showInfo_popup("Rewrite Success", "Rewrote data/people.pear")
        self.readDirectory()
        self.populateDirectoryTable()

    def showError_popup(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)  # set the icon of the prompt
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)  # set the buttons available on the prompt
        msg.exec_()

    def showInfo_popup(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)  # set the icon of the prompt
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)  # set the buttons available on the prompt
        msg.exec_()

    def datetimeStringtoUnix(self, date, time):
        date_delim = re.split('/', date)
        month = int(date_delim[0])
        day = int(date_delim[1])
        year = int(date_delim[2])

        time_delim = re.split(':', time)
        h = int(time_delim[0])
        m = int(time_delim[1])
        s = int(time_delim[2])

        date_unix = (datetime.datetime(year, month, day) -
                       datetime.datetime(1970, 1, 1)).total_seconds()

        time_in_seconds = h * 3600 + m * 60 + s

        total_unix = int(date_unix + time_in_seconds)
        return total_unix

    # sort modes: "id", "time", "length"
    def sortLog(self, column):
        reverseSort = False
        if column == 1:
            sort_mode = "id"
            self.IDReverseSort = not self.IDReverseSort
            reverseSort = self.IDReverseSort
        elif column >= 2 and column <= 5:
            sort_mode = "time"
            self.timeReverseSort = not self.timeReverseSort
            reverseSort = self.timeReverseSort
        elif column == 6:
            sort_mode = "length"
            self.lengthReverseSort = not self.lengthReverseSort
            reverseSort = self.lengthReverseSort
        else: return

        print("Sort column: " + str(column))

        # make copy of table
        table_copy = dict()
        sortColumn = dict()
        for row in range(0, ui.logTableWidget.rowCount()):
            table_copy[row] = [
                ui.logTableWidget.cellWidget(row, 0).isChecked(),
                ui.logTableWidget.cellWidget(row, 1).text(),
                ui.logTableWidget.cellWidget(row, 2).text(),
                ui.logTableWidget.cellWidget(row, 3).text(),
                ui.logTableWidget.cellWidget(row, 4).text(),
                ui.logTableWidget.cellWidget(row, 5).text(),
                ui.logTableWidget.cellWidget(row, 6).text()
            ]

            if sort_mode == "id":
                sortColumn[row] = int(table_copy[row][1])
            elif sort_mode == "time":
                logout_unix = self.datetimeStringtoUnix(table_copy[row][3], table_copy[row][5])
                sortColumn[row] = logout_unix
            elif sort_mode == "length":
                login_unix = self.datetimeStringtoUnix(table_copy[row][2], table_copy[row][4])
                logout_unix = self.datetimeStringtoUnix(table_copy[row][3], table_copy[row][5])
                length = logout_unix - login_unix
                sortColumn[row] = length

        sortedColumn = sorted(sortColumn.items(), key=operator.itemgetter(1))
        if reverseSort: sortedColumn.reverse()

        for sorted_row in range(0, ui.logTableWidget.rowCount()):
            row = tuple(sortedColumn[sorted_row])[0]

            checkbox = QCheckBox()
            lineEdit1 = QLineEdit(table_copy[row][1])
            lineEdit2 = QLineEdit(table_copy[row][2])
            lineEdit3 = QLineEdit(table_copy[row][3])
            lineEdit4 = QLineEdit(table_copy[row][4])
            lineEdit5 = QLineEdit(table_copy[row][5])
            lineEdit6 = QLineEdit(table_copy[row][6])

            checkbox.setChecked(table_copy[row][0])

            lineEdit1.setStyleSheet("border: none")
            lineEdit2.setStyleSheet("border: none")
            lineEdit3.setStyleSheet("border: none")
            lineEdit4.setStyleSheet("border: none")
            lineEdit5.setStyleSheet("border: none")
            lineEdit6.setStyleSheet("border: none")

            lineEdit1.setReadOnly(True)
            lineEdit2.setReadOnly(False)
            lineEdit3.setReadOnly(False)
            lineEdit4.setReadOnly(False)
            lineEdit5.setReadOnly(False)
            lineEdit6.setReadOnly(True)

            ui.logTableWidget.setCellWidget(sorted_row, 0, checkbox)
            ui.logTableWidget.setCellWidget(sorted_row, 1, lineEdit1)
            ui.logTableWidget.setCellWidget(sorted_row, 2, lineEdit2)
            ui.logTableWidget.setCellWidget(sorted_row, 3, lineEdit3)
            ui.logTableWidget.setCellWidget(sorted_row, 4, lineEdit4)
            ui.logTableWidget.setCellWidget(sorted_row, 5, lineEdit5)
            ui.logTableWidget.setCellWidget(sorted_row, 6, lineEdit6)


class Ui_frontEnd(object):
    # CHANGE THIS BEFORE PACKAGING
    PASSWORD = ""

    def post_initialization_tasks(self):
        pass

    # constructor, initialize UI
    def __init__(self):
        import sys
        global ui

        self.app = QtWidgets.QApplication(sys.argv)
        self.PasswordDialog = QtWidgets.QDialog(None,
                                                QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.CreateLogEntryDialog = QtWidgets.QDialog(None,
                                                      QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.MainWindow = QtWidgets.QMainWindow(None,
                                                QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)

        self.passwordUI = GUIAdminToolPasswordDialog.Ui_Dialog()
        self.createLogUI = GUIAdminToolCreateLogDialog.Ui_LogEntryDialog()

        self.passwordUI.setupUi(self.PasswordDialog)
        self.createLogUI.setupUi(self.CreateLogEntryDialog)
        ui.setupUi(self.MainWindow)

        self.customConfiguration()
        self.PasswordDialog.show()
        self.CreateLogEntryDialog.hide()
        self.MainWindow.hide()

        self.post_initialization_tasks()
        sys.exit(self.app.exec_())

    def checkPassword(self):
        input = self.passwordUI.lineEdit.text()
        if input == self.PASSWORD:
            self.PasswordDialog.hide()
            self.MainWindow.show()
            backEnd.readDirectory()
            backEnd.readLog()
            backEnd.populateDirectoryTable()
            backEnd.populateLogTable()
        else:
            backEnd.showError_popup("Wrong Password", "Try again, but better.")

    # custom UI configurations
    def customConfiguration(self):
        self.passwordUI.submitButton.clicked.connect(self.checkPassword)
        self.createLogUI.submitButton.clicked.connect(self.addLogEntrySubmitCall)

        ui.addButton.clicked.connect(self.addLogEntryAddCall)
        ui.tabWidget.setCurrentIndex(0)
        ui.rewriteLogButton.clicked.connect(backEnd.rewriteLogCall)
        ui.rewriteDirectoryButton.clicked.connect(backEnd.rewriteDirectoryCall)
        ui.logTableWidget.horizontalHeader().sectionClicked.connect(backEnd.sortLog)

    def addLogEntryAddCall(self):
        self.CreateLogEntryDialog.show()
        self.createLogUI.lineEdit.setFocus()

    def addLogEntrySubmitCall(self):
        self.CreateLogEntryDialog.hide()
        IDEntry = self.createLogUI.lineEdit.text()
        self.createLogUI.lineEdit.clear()

        if len(IDEntry) == 0 or not IDEntry.isdigit():
            return

        ui.logTableWidget.insertRow(0)
        backEnd.constructLogRow(0, LogEntry(IDEntry, 0, 0))


ui = GUIAdminTool.Ui_MainWindow()
backEnd = Ui_backEnd()
frontEnd = QtWidgets
