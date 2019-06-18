# front and back end GUI

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsOpacityEffect

from GUI.GUIPearLog import Ui_mainWindow
from PearLogger_Core import Core
from PearLogger_Utils import Constants

# Manages user interaction with GUI, passes on logistics to Core class
class Ui_backEnd(object):

    student_table_rows = Constants.STUDENT_TABLE_ROWS
    mentor_table_rows = Constants.MENTOR_TABLE_ROWS

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
        core.signoutAll()

    # menu button, signs everyone out without clearing hours
    def clearAll_menu_trigger(self):
        core.clearAll()

    # menu button, popup GUI to view everyone's hours
    def viewHours_menu_trigger(self):
        pass

    # menu button, generates csv report of hours
    def generateReport_menu_trigger(self):
        pass

    # menu button, popup GUI to change options
    def changeRules_menu_trigger(self):
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

    # adds 1 row to the end of the student table
    def add_row_student(self):
        ui.studentTable.insertRow(self.student_table_rows)
        ui.studentTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.student_table_rows += 1

    # adds 1 row to the end of the mentor table
    def add_row_mentor(self):
        ui.mentorTable.insertRow(self.mentor_table_rows)
        ui.mentorTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mentor_table_rows += 1

    # removes 1 row from the end of the student table
    def remove_row_student(self):
        ui.studentTable.removeRow(self.student_table_rows - 1)
        self.student_table_rows -= 1

    # removes 1 from the end of the mentor table
    def remove_row_mentor(self):
        ui.mentorTable.removeRow(self.mentor_table_rows - 1)
        self.mentor_table_rows -= 1

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

    def setLeaderboard(self, rank, name, time, maxTime):
        widgets = self.get_leaderboard_widgets(rank)
        widgets[0].setText(name)
        widgets[1].setText(str(round(time, 1)))
        widgets[2].setMaximum(maxTime)
        widgets[2].setValue(time)

    # returns leaderboard widgets tuple given a rank ([0]=name label, [1]=time label, [2]=time progress bar)
    def get_leaderboard_widgets(self, rank):
        return {
            1: (ui.name_label_rank_1, ui.time_label_rank_1, ui.bar_rank_1),
            2: (ui.name_label_rank_2, ui.time_label_rank_2, ui.bar_rank_2),
            3: (ui.name_label_rank_3, ui.time_label_rank_3, ui.bar_rank_3),
            4: (ui.name_label_rank_4, ui.time_label_rank_4, ui.bar_rank_4),
            5: (ui.name_label_rank_5, ui.time_label_rank_5, ui.bar_rank_5),
            6: (ui.name_label_rank_6, ui.time_label_rank_6, ui.bar_rank_6),
            7: (ui.name_label_rank_7, ui.time_label_rank_7, ui.bar_rank_7),
            8: (ui.name_label_rank_8, ui.time_label_rank_8, ui.bar_rank_8),
            9: (ui.name_label_rank_9, ui.time_label_rank_9, ui.bar_rank_9),
            10: (ui.name_label_rank_10, ui.time_label_rank_10, ui.bar_rank_10)
        }.get(rank)


class Ui_frontEnd(object):

    # constructor, initialize UI
    def __init__(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        self.mainWindow = QtWidgets.QMainWindow()

        ui.setupUi(self.mainWindow)
        self.mainWindow.showFullScreen()

        self.customConfiguration()

        # initialize ID Boxes, must be done after app object created for some stupid reason
        core.initialize_IDBoxes()

        # initialize previous logins
        core.initialize_previous_logins()

        # update leaderboard
        core.updateLeaderboard()

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

        # connect - hitting 'ESC' escapes fullscreen
        self.mainWindow.keyPressEvent = self.window_keypress_event

        # connect - menu action buttons
        ui.actionSign_Out_All.triggered.connect(backEnd.signOutAll_menu_trigger)
        ui.actionClear_All.triggered.connect(backEnd.clearAll_menu_trigger)
        ui.actionView_Hours.triggered.connect(backEnd.viewHours_menu_trigger)
        ui.actionGenerate_Report.triggered.connect(backEnd.generateReport_menu_trigger)
        ui.actionChange_Rules.triggered.connect(backEnd.changeRules_menu_trigger)
        ui.actionExit_Fullscreen.triggered.connect(self.show_windowed)
        ui.actionFullscreen.triggered.connect(self.show_fullscreen)
        ui.actionReload_Data.triggered.connect(backEnd.reloadData_menu_trigger)
        ui.actionAdd_Person.triggered.connect(backEnd.addPerson_menu_trigger)

    def window_keypress_event(self, event):
        # pressing escapes switches to windowed mode
        if event.key() == QtCore.Qt.Key_Escape:
            self.show_windowed()

    def show_windowed(self):
        self.mainWindow.showMaximized()

    def show_fullscreen(self):
        self.mainWindow.showFullScreen()


def showErrorMessage_caller(message):
    backEnd.showError_message(message)


backEnd = Ui_backEnd()
ui = Ui_mainWindow()
core = Core()
