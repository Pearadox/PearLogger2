# front and back end GUI
import datetime
import re
import time
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QLabel, QLineEdit, QCheckBox, QComboBox

from CustomQt.ComboBoxNoScroll import ComboBoxNoScroll
from GUI import GUIAdminTool, GUIAdminToolPasswordDialog, GUIAdminToolCreateLogDialog

# Manages user interaction with GUI, passes on logistics to Core class
from PearLogger_Utils import Profile, LogEntry


class Ui_backEnd(object):
    peopleList = list()
    log = list()

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

    def populateLogTable(self):
        ui.logTableWidget.setRowCount(len(self.log))
        currentRow = len(self.log) - 1
        for LogEntry in self.log:
            self.constructLogRow(currentRow, LogEntry)
            currentRow -= 1

    def populateDirectoryTable(self):
        ui.directoryTableWidget.setRowCount(len(self.peopleList))
        currentRow = 0

        ui.directoryTableWidget.setColumnWidth(0, 25)
        ui.directoryTableWidget.setColumnWidth(1, 70)
        ui.directoryTableWidget.setColumnWidth(2, 250)
        ui.directoryTableWidget.setColumnWidth(3, 350)
        ui.directoryTableWidget.setColumnWidth(4, 45)

        for profile in self.peopleList:
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

            ui.directoryTableWidget.setCellWidget(currentRow, 0, delete_cbox)
            ui.directoryTableWidget.setCellWidget(currentRow, 1, ID_lEdit)
            ui.directoryTableWidget.setCellWidget(currentRow, 2, name_lEdit)
            ui.directoryTableWidget.setCellWidget(currentRow, 3, picture_lEdit)
            ui.directoryTableWidget.setCellWidget(currentRow, 4, category_comboBox)

            currentRow += 1

    def rewriteLogCall(self):
        fileBuffer = ""

        for i in range(1, ui.logTableWidget.rowCount() + 1):
            row = ui.logTableWidget.rowCount() - i
            delete = ui.logTableWidget.cellWidget(row, 0).isChecked()
            if delete: continue

            try:
                ID = ui.logTableWidget.cellWidget(row, 1).text()
                dateIn = ui.logTableWidget.cellWidget(row, 2).text()
                dateOut = ui.logTableWidget.cellWidget(row, 3).text()
                login = ui.logTableWidget.cellWidget(row, 4).text()
                logout = ui.logTableWidget.cellWidget(row, 5).text()

                dateIn_delim = re.split('/', dateIn)
                dateOut_delim = re.split('/', dateOut)
                dateIn_month = int(dateIn_delim[0])
                dateIn_day = int(dateIn_delim[1])
                dateIn_year = int(dateIn_delim[2])
                dateOut_month = int(dateOut_delim[0])
                dateOut_day = int(dateOut_delim[1])
                dateOut_year = int(dateOut_delim[2])

                login_delim = re.split(':', login)
                logout_delim = re.split(':', logout)
                login_h = int(login_delim[0])
                login_m = int(login_delim[1])
                login_s = int(login_delim[2])
                logout_h = int(logout_delim[0])
                logout_m = int(logout_delim[1])
                logout_s = int(logout_delim[2])

                dateIn_unix = (datetime.datetime(dateIn_year, dateIn_month, dateIn_day) -
                               datetime.datetime(1970, 1, 1)).total_seconds()
                dateOut_unix = (datetime.datetime(dateOut_year, dateOut_month, dateOut_day) -
                                datetime.datetime(1970, 1, 1)).total_seconds()

                login_seconds = login_h * 3600 + login_m * 60 + login_s
                logout_seconds = logout_h * 3600 + logout_m * 60 + logout_s

                login_unix = int(dateIn_unix + login_seconds)
                logout_unix = int(dateOut_unix + logout_seconds)

                if logout_unix < login_unix:
                    self.showError_popup("Log Table Error", "Logout time is before login time: Row " + str(row))
                    return

                if logout_unix == 0 or login_unix == 0:
                    self.showError_popup("Log Table Error",
                                         "Time not filled out (Today is not the epoch!): Row " + str(row))

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
                print(category)

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
        ui.addButton.clicked.connect(self.addLogEntryAddCall)
        ui.tabWidget.setCurrentIndex(0)
        ui.rewriteLogButton.clicked.connect(backEnd.rewriteLogCall)
        ui.rewriteDirectoryButton.clicked.connect(backEnd.rewriteDirectoryCall)
        self.createLogUI.submitButton.clicked.connect(self.addLogEntrySubmitCall)

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
frontEnd = Ui_frontEnd()
