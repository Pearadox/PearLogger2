# front and back end GUI
import datetime
import operator
import os
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

from GUI.GUIGenerateReportDialog import Ui_GenerateReportDialog
from PearLogger_Utils import Profile


# Manages user interaction with GUI, passes on logistics to Core class
class GenerateReport_UI_backEnd(object):

    MONTH = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December')
    WEEKDAY = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    def initialize(self):
        earliestTime = sys.maxsize
        latestTime = -1
        for logEntry in dm.log:
            earliestTime = min(logEntry.login_time, earliestTime)
            latestTime = max(logEntry.logout_time, latestTime)
        if latestTime < earliestTime:
            return

        earliestDateTime = time.gmtime(earliestTime)
        latestDateTime = time.gmtime(latestTime)
        earliestQDate = QDate(earliestDateTime.tm_year, earliestDateTime.tm_mon, earliestDateTime.tm_mday)
        latestQDate = QDate(latestDateTime.tm_year, latestDateTime.tm_mon, latestDateTime.tm_mday)

        ui.start_dateEdit.setDate(earliestQDate)
        ui.end_dateEdit.setDate(latestQDate)
        ui.start_dateEdit.setDateRange(earliestQDate, latestQDate)
        ui.end_dateEdit.setDateRange(earliestQDate, latestQDate)

    def generateReportCall(self):
        # get category configuration
        categoryList = list()
        if ui.dawson_checkBox.isChecked(): categoryList.append(Profile.CATEGORY_STUDENT_DAWSON)
        if ui.pearland_checkBox.isChecked(): categoryList.append(Profile.CATEGORY_STUDENT_PEARLAND)
        if ui.turner_checkBox.isChecked(): categoryList.append(Profile.CATEGORY_STUDENT_TURNER)
        if ui.mentor_checkBox.isChecked(): categoryList.append(Profile.CATEGORY_MENTOR)
        if ui.teacher_checkBox.isChecked(): categoryList.append(Profile.CATEGORY_TEACHER)
        if ui.alumni_checkBox.isChecked(): categoryList.append(Profile.CATEGORY_ALUMNI)
        if ui.team_checkBox.isChecked(): categoryList.append(Profile.CATEGORY_TEAM)
        if ui.other_checkBox.isChecked(): categoryList.append(Profile.CATEGORY_OTHER)
        if len(categoryList) == 0:
            self.showError_popup("Generate Error", "Select at least one category")
            return

        # get time window configuration
        startQDate = ui.start_dateEdit.date()
        startDate_unix = (datetime.datetime(startQDate.year(), startQDate.month(), startQDate.day()) -
                          datetime.datetime(1970, 1, 1)).total_seconds()
        endQDate = ui.end_dateEdit.date()
        endDate_unix = (datetime.datetime(endQDate.year(), endQDate.month(), endQDate.day()) -
                          datetime.datetime(1970, 1, 1)).total_seconds()
        if endDate_unix < startDate_unix:
            self.showError_popup("Generate Error", "End date should be later than start date")
            return

        # get sort configuration
        sortMode = "time"
        if ui.sortTime_radioButton.isChecked():
            sortMode = "time"
        elif ui.sortID_radioButton.isChecked():
            sortMode = "id"
        elif ui.sortLength_radioButton.isChecked():
            sortMode = "length"

        # include log entries in end date too
        endDate_unix += 86400

        # sort log entries
        if sortMode == "time":
            dm.log.sort(key=lambda x: x.login_time)
        elif sortMode == "id":
            dm.log.sort(key=lambda x: int(x.ID))
        elif sortMode == "length":
            dm.log.sort(key=lambda x: x.length)

        meetingsDict = dict()  # k: ID, v: num meetings
        lengthDict = dict()  # k: ID, v: total seconds

        # prepare csv buffer
        csvWriteBuffer = list()
        for i in range(len(dm.log)+1):
            columns = list()
            for j in range(16):
                columns.append('')
            csvWriteBuffer.append(columns)

        # full log
        row = 0
        for LogEntry in dm.log:
            row += 1
            # skip days not in range
            if not (LogEntry.login_time > startDate_unix and LogEntry.logout_time < endDate_unix):
                continue

            loginDateTime = time.gmtime(LogEntry.login_time)
            logoutDateTime = time.gmtime(LogEntry.logout_time)
            lengthSeconds = LogEntry.logout_time - LogEntry.login_time

            ID = LogEntry.ID
            name = dm.peopleDict[ID].name
            category = Profile.CATEGORY__DICTIONARY[dm.peopleDict[ID].category]
            dateIn = self.WEEKDAY[loginDateTime.tm_wday] + ", " + self.MONTH[loginDateTime.tm_mon - 1] + " " + \
                     str("%02d" % loginDateTime.tm_mday) + ", " + str(loginDateTime.tm_year)
            dateOut = self.WEEKDAY[logoutDateTime.tm_wday] + ", " + self.MONTH[logoutDateTime.tm_mon - 1] + " " + \
                     str("%02d" % logoutDateTime.tm_mday) + ", " + str(logoutDateTime.tm_year)
            timeIn = str("%02d" % loginDateTime.tm_hour) + ":" + str("%02d" % loginDateTime.tm_min) + ":" + \
                     str("%02d" % loginDateTime.tm_sec)
            timeOut = str("%02d" % logoutDateTime.tm_hour) + ":" + str("%02d" % logoutDateTime.tm_min) + ":" + \
                     str("%02d" % logoutDateTime.tm_sec)
            length = str("%02d" % (int(lengthSeconds)/3600)) + ":" + str("%02d" % (int(lengthSeconds) % 3600/60)) + ":" + \
                      str("%02d" % (int(lengthSeconds) % 60))

            # skip if category not included
            if dm.peopleDict[ID].category not in categoryList:
                continue

            # add info to write buffer
            csvWriteBuffer[row][0] = str(ID)
            csvWriteBuffer[row][1] = name
            csvWriteBuffer[row][2] = category
            csvWriteBuffer[row][3] = dateIn
            csvWriteBuffer[row][4] = timeIn
            csvWriteBuffer[row][5] = dateOut
            csvWriteBuffer[row][6] = timeOut
            csvWriteBuffer[row][7] = length

            # record some information for overall summary later
            if ID not in meetingsDict:
                meetingsDict[ID] = 0
            if ID not in lengthDict:
                lengthDict[ID] = 0

            meetingsDict[ID] += 1
            lengthDict[ID] += lengthSeconds

        # ranked summary
        sortedRank = sorted(lengthDict.items(), key=operator.itemgetter(1))
        sortedRank.reverse()

        row = 0
        for tup in sortedRank:
            row += 1
            ID = tup[0]
            name = dm.peopleDict[ID].name
            category = Profile.CATEGORY__DICTIONARY[dm.peopleDict[ID].category]
            meetings = meetingsDict[ID]
            totalTime = str("%02d" % (int(tup[1])/3600)) + ":" + str("%02d" % (int(tup[1]) % 3600/60)) + ":" + \
                      str("%02d" % (int(tup[1]) % 60))

            csvWriteBuffer[row][11] = str(ID)
            csvWriteBuffer[row][12] = name
            csvWriteBuffer[row][13] = category
            csvWriteBuffer[row][14] = str(meetings)
            csvWriteBuffer[row][15] = totalTime

        csvWriteBuffer[0][0] = 'ID'
        csvWriteBuffer[0][1] = 'Name'
        csvWriteBuffer[0][2] = 'Category'
        csvWriteBuffer[0][3] = 'Date In'
        csvWriteBuffer[0][4] = 'Time In'
        csvWriteBuffer[0][5] = 'Date Out'
        csvWriteBuffer[0][6] = 'Time Out'
        csvWriteBuffer[0][7] = 'Length'
        csvWriteBuffer[0][8] = ''
        csvWriteBuffer[0][9] = ''
        csvWriteBuffer[0][10] = ''
        csvWriteBuffer[0][11] = 'ID'
        csvWriteBuffer[0][12] = 'Name'
        csvWriteBuffer[0][13] = 'Category'
        csvWriteBuffer[0][14] = 'Meetings Attended'
        csvWriteBuffer[0][15] = 'Total Time'

        # write array to csv file
        dt = datetime.datetime.now()
        filename = str(dt.month) + '-' + str(dt.day) + '-' + str(dt.year) + ' ' + \
                   str("%02d" % dt.hour) + str("%02d" % dt.minute)

        # make directory if it doesn't exist
        if not os.path.exists('data/Generated Reports'):
            os.makedirs('data/Generated Reports')

        report_file = open("data/Generated Reports/" + filename + ".csv", 'w')
        report_file.truncate(0)

        for r in range(len(csvWriteBuffer)):
            for c in range(len(csvWriteBuffer[r])):
                report_file.write('"' + csvWriteBuffer[r][c] + '",')
            report_file.write('\n')

        report_file.close()

        self.showInfo_popup("Generate Report", "Successfully generated report (data/Generated Reports/" + filename + ")")

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


class GenerateReport_UI_frontEnd(object):

    def post_initialization_tasks(self):
        backEnd.initialize()

    # constructor, initialize UI
    def initialize(self, dataManager):
        global dm
        dm = dataManager

        self.GenerateReportDialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint
                                            | QtCore.Qt.WindowCloseButtonHint)
        ui.setupUi(self.GenerateReportDialog)

        self.customConfiguration()
        self.post_initialization_tasks()

        self.GenerateReportDialog.exec_()

    # custom UI configurations
    def customConfiguration(self):
        ui.generateButton.clicked.connect(backEnd.generateReportCall)
        ui.sortTime_radioButton.setChecked(True)


dm = None
backEnd = GenerateReport_UI_backEnd()
ui = Ui_GenerateReportDialog()