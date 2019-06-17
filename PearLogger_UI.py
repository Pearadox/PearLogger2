# front and back end GUI

import _thread
import copy
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsOpacityEffect

from GUI.GUIPearLog import Ui_mainWindow
from PearLogger_Core import Core

# Manages user interaction with GUI, passes on logistics to Core class
class Ui_backEnd(object):

    # triggered when hitting enter on login lineEdit
    def signIn_lineEdit_trigger(self):
        # get ID login entry, ignore if not an integer
        try:
            # get ID value from lineEdit
            ID = str(int(ui.loginLineEdit.text()))
        except Exception as e:
            print(e)
            # entry is invalid, ignore it
            self.showError_message("Error: ID Entry must be a number")
            return

        # pass login to core, check for successful log in
        successful = core.log(ID)

        # clear line if login was successful
        if successful:
            ui.loginLineEdit.setText('')

    # menu button, signs everyone out
    def signOutAll_menu_trigger(self):
        pass

    # menu button, signs everyone out without clearing hours
    def clearAll_menu_trigger(self):
        pass

    # menu button, popup GUI to view everyone's hours
    def viewHours_menu_trigger(self):
        pass

    # menu button, generates csv report of hours
    def generateReport_menu_trigger(self):
        pass

    # menu button, popup GUI to change options
    def options_menu_trigger(self):
        pass

    # menu button, reloads data read from files
    def reloadData_menu_trigger(self):
        pass

    # menu button, pop GUI to add person
    def addPerson_menu_trigger(self):
        pass

    # creates ID box with name, picture, and ID in table
    def setIDBox(self, groupBox, isStudent, row, column):
        if isStudent:
            ui.studentTable.setCellWidget(row, column, groupBox)
        else:
            ui.mentorTable.setCellWidget(row, column, groupBox)

    def removeIDBox(self, isStudent, row, column):
        if isStudent:
            ui.studentTable.removeCellWidget(row, column)
        else:
            ui.mentorTable.removeCellWidget(row, column)

    # show formatted error message under sign-in lineEdit
    def showError_message(self, error_message):
        # red-colored text, set label to message
        ui.errorLabel.setText("<html><hea   d/><body><p><span style=\" color:#dc0000;\">"+error_message+"</span></p></body></html>")

        # add fading animation
        self.effect = QGraphicsOpacityEffect()
        ui.errorLabel.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(3000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    # makes a prompt window with an Error icon
    def showError_popup(title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)  # set the icon of the prompt
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.resize()
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)  # set the buttons available on the prompt
        msg.exec()

    # makes a prompt window with a Information icon
    def showInfo_popup(title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)  # set the icon of the prompt
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.resize(500, 500)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)  # set the buttons available on the prompt
        msg.exec()



class Ui_frontEnd(object):

    # constructor, initialize UI
    def __init__(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QtWidgets.QMainWindow()

        ui.setupUi(mainWindow)
        mainWindow.showMaximized()
        mainWindow.show()

        self.customConfiguration()

        # initialize ID Boxes, must be done after app object created for some stupid reason
        core.initialize_IDBoxes()

        # initialize previous logins
        core.initialize_previous_logins()

        sys.exit(app.exec_())

    # custom UI configurations
    def customConfiguration(self):
        # make cells unselectable
        ui.studentTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        ui.mentorTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # focus on line edit
        ui.loginLineEdit.setFocus()

        # connect - hitting 'ENTER' on signin line edit
        ui.loginLineEdit.returnPressed.connect(backEnd.signIn_lineEdit_trigger)

        # connect - menu action buttons
        ui.actionSign_Out_All.triggered.connect(backEnd.signOutAll_menu_trigger)
        ui.actionClear_All.triggered.connect(backEnd.clearAll_menu_trigger)
        ui.actionView_Hours.triggered.connect(backEnd.viewHours_menu_trigger)
        ui.actionGenerate_Report.triggered.connect(backEnd.generateReport_menu_trigger)
        ui.actionOptions.triggered.connect(backEnd.options_menu_trigger)
        ui.actionReload_Data.triggered.connect(backEnd.reloadData_menu_trigger)
        ui.actionAdd_Person.triggered.connect(backEnd.addPerson_menu_trigger)


def showErrorMessage_Caller(message):
    backEnd.showError_message(message)


backEnd = Ui_backEnd()
ui = Ui_mainWindow()
core = Core()
