# front and back end GUI
import datetime
import re
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from GUI.GUIOptionsDialog import Ui_optionsDialog
from PearLogger_Utils import Profile, Constants

# Manages user interaction with GUI, passes on logistics to Core class
class Options_Ui_backEnd(object):

    currentDayType = "NULL"

    def initialize(self):
        self.initialize_leaderboard_checkboxes()
        self.initialize_time_rules("Weekday", False)

    # initialize check boxes
    def initialize_leaderboard_checkboxes(self):
        # add leaderboard visiblitiy config entry if it doesn't exist
        if 'Leaderboard_Visible_Categories' not in dm.config.keys():
            dm.config['Leaderboard_Visible_Categories'] = '1,2,3,11,12,13,21,22'

        # get list config of visible boxes
        visible_categories = re.split(',', dm.config['Leaderboard_Visible_Categories'])

        if str(Profile.CATEGORY_STUDENT_DAWSON) in visible_categories:
            frontEnd.ui.student_dawson_checkBox.setChecked(True)
        if str(Profile.CATEGORY_STUDENT_PEARLAND) in visible_categories:
            frontEnd.ui.student_pearland_checkBox.setChecked(True)
        if str(Profile.CATEGORY_STUDENT_TURNER) in visible_categories:
            frontEnd.ui.student_turner_checkBox.setChecked(True)
        if str(Profile.CATEGORY_ALUMNI) in visible_categories:
            frontEnd.ui.alumni_checkBox.setChecked(True)
        if str(Profile.CATEGORY_MENTOR) in visible_categories:
            frontEnd.ui.mentor_checkBox.setChecked(True)
        if str(Profile.CATEGORY_TEACHER) in visible_categories:
            frontEnd.ui.teacher_checkBox.setChecked(True)
        if str(Profile.CATEGORY_TEAM) in visible_categories:
            frontEnd.ui.team_checkBox.setChecked(True)
        if str(Profile.CATEGORY_OTHER) in visible_categories:
            frontEnd.ui.other_checkBox.setChecked(True)

    def initialize_time_rules(self, dayType, askSave=True):

        if askSave:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Save Dialog')
            msgBox.setText('Do you want to save your current configuration for ' + self.currentDayType + '?')
            msgBox.addButton(QtWidgets.QPushButton('Save'), QMessageBox.YesRole)
            msgBox.addButton(QtWidgets.QPushButton('Don\'t Save'), QMessageBox.NoRole)
            msgBox.addButton(QtWidgets.QPushButton('Cancel'), QMessageBox.RejectRole)
            reply = msgBox.exec_()

            if reply == QMessageBox.AcceptRole:
                print("Saving time config: " + self.currentDayType)
                self.record_time_rules_config()
            elif reply == QMessageBox.DestructiveRole:
                return


        # get current config
        try:
            self.currentDayType = dayType

            # enable configs
            enable_time_limit_config = dm.config['Enable_Time_Limit_' + dayType] is '1'
            enable_time_window_config = dm.config['Enable_Time_Window_' + dayType] is '1'

            # time limits
            time_limit_minimum_config = float(dm.config['Minimum_Hours_' + dayType])
            time_limit_maximum_config = float(dm.config['Maximum_Hours_' + dayType])

            # window time
            # split with ':' delimiter to get individual hours and minutes
            open_delimited = re.split(':', dm.config['Window_Open_' + dayType])
            close_delimited = re.split(':', dm.config['Window_Close_' + dayType])
            # calculate seconds
            time_window_open_weekday_seconds_config = int(open_delimited[0]) * 3600 + int(open_delimited[1]) * 60
            time_window_close_weekday_seconds_config = int(close_delimited[0]) * 3600 + int(close_delimited[1]) * 60

            # set widget values based on current config
            if dayType is "Weekday":
                frontEnd.ui.weekday_radioButton.setChecked(True)
            elif dayType is "Saturday":
                frontEnd.ui.saturday_radioButton.setChecked(True)
            elif dayType is "Sunday":
                frontEnd.ui.sunday_radioButton.setChecked(True)
            frontEnd.ui.time_length_limit_checkBox.setChecked(enable_time_limit_config)
            frontEnd.ui.time_window_checkBox.setChecked(enable_time_window_config)
            frontEnd.ui.minimum_hours_spinBox.setValue(time_limit_minimum_config)
            frontEnd.ui.maximum_hours_spinBox.setValue(time_limit_maximum_config)
            frontEnd.ui.window_open_timeEdit.setTime(
                QtCore.QTime(int(time_window_open_weekday_seconds_config/3600), int(time_window_open_weekday_seconds_config%3600/60)))
            frontEnd.ui.window_close_timeEdit.setTime(
                QtCore.QTime(int(time_window_close_weekday_seconds_config/3600), int(time_window_close_weekday_seconds_config%3600/60)))

            # turn on labels based on checkbox state
            self.time_length_limit_checkbox_action()
            self.time_window_checkbox_action()
        except Exception as e:
            # config file is bad
            main_ui.showError_popup(
                "Configuration File Error", "Time limit/window configuration invalid (data/config.pear). "
                                            "Delete file and restart program to reconfigure.")

    def weekday_radioButton_action(self):
        self.initialize_time_rules("Weekday")

    def saturday_radioButton_action(self):
        self.initialize_time_rules("Saturday")

    def sunday_radioButton_action(self):
        self.initialize_time_rules("Sunday")

    def time_length_limit_checkbox_action(self):
        visibility = frontEnd.ui.time_length_limit_checkBox.isChecked()
        frontEnd.ui.minimum_hours_label.setVisible(visibility)
        frontEnd.ui.maximum_hours_label.setVisible(visibility)
        frontEnd.ui.minimum_hours_spinBox.setVisible(visibility)
        frontEnd.ui.maximum_hours_spinBox.setVisible(visibility)

    def time_window_checkbox_action(self):
        visibility = frontEnd.ui.time_window_checkBox.isChecked()
        frontEnd.ui.window_open_label.setVisible(visibility)
        frontEnd.ui.window_close_label.setVisible(visibility)
        frontEnd.ui.window_open_timeEdit.setVisible(visibility)
        frontEnd.ui.window_close_timeEdit.setVisible(visibility)

    # records leaderboard checkboxes into config file
    def record_leaderboard_checkbox_config(self):
        # create list confiig of visible boxes
        visible_categories = list()

        if frontEnd.ui.student_dawson_checkBox.isChecked():
            visible_categories.append(str(Profile.CATEGORY_STUDENT_DAWSON))
        if frontEnd.ui.student_pearland_checkBox.isChecked():
            visible_categories.append(str(Profile.CATEGORY_STUDENT_PEARLAND))
        if frontEnd.ui.student_turner_checkBox.isChecked():
            visible_categories.append(str(Profile.CATEGORY_STUDENT_TURNER))
        if frontEnd.ui.alumni_checkBox.isChecked():
            visible_categories.append(str(Profile.CATEGORY_ALUMNI))
        if frontEnd.ui.mentor_checkBox.isChecked():
            visible_categories.append(str(Profile.CATEGORY_MENTOR))
        if frontEnd.ui.teacher_checkBox.isChecked():
            visible_categories.append(str(Profile.CATEGORY_TEACHER))
        if frontEnd.ui.team_checkBox.isChecked():
            visible_categories.append(str(Profile.CATEGORY_TEAM))
        if frontEnd.ui.other_checkBox.isChecked():
            visible_categories.append(str(Profile.CATEGORY_OTHER))

        # change list to comma-delimited string
        dm.config['Leaderboard_Visible_Categories'] = ','.join(visible_categories)

    def record_time_rules_config(self):
        dm.config['Enable_Time_Limit_' + self.currentDayType] = '1' if frontEnd.ui.time_length_limit_checkBox.isChecked() else '0'
        dm.config['Enable_Time_Window_' + self.currentDayType] = '1' if frontEnd.ui.time_window_checkBox.isChecked() else '0'
        dm.config['Minimum_Hours_' + self.currentDayType] = str(frontEnd.ui.minimum_hours_spinBox.value())
        dm.config['Maximum_Hours_' + self.currentDayType] = str(frontEnd.ui.maximum_hours_spinBox.value())

        # get QTime from window
        open_time = frontEnd.ui.window_open_timeEdit.time()
        close_time = frontEnd.ui.window_close_timeEdit.time()

        dm.config['Window_Open_' + self.currentDayType] = str(open_time.hour()) + ":" + str(open_time.minute())
        dm.config['Window_Close_' + self.currentDayType] = str(close_time.hour()) + ":" + str(close_time.minute())

    # action when button pressed
    def apply_button_action(self):
        # record checkbox config
        self.record_leaderboard_checkbox_config()
        # update leaderboard
        core.updateLeaderboard()

        # record time limit/window config
        self.record_time_rules_config()

        # update config file
        dm.rewriteConfig()

class Options_Ui_frontEnd(object):

    def post_initialization_tasks(self):
        backEnd.initialize()

    # constructor, initialize UI
    def initialize(self, coreInstance, dataManager, main_ui_instance):
        global dm, frontEnd, core, main_ui
        core = coreInstance
        dm = dataManager
        frontEnd = self
        main_ui = main_ui_instance

        self.OptionsDialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint
                                            | QtCore.Qt.WindowCloseButtonHint)
        self.ui = Ui_optionsDialog()
        self.ui.setupUi(self.OptionsDialog)

        self.customConfiguration()
        self.post_initialization_tasks()

        self.OptionsDialog.exec_()

    # custom UI configurations
    def customConfiguration(self):
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.apply_button.clicked.connect(backEnd.apply_button_action)
        self.ui.time_length_limit_checkBox.clicked.connect(backEnd.time_length_limit_checkbox_action)
        self.ui.time_window_checkBox.clicked.connect(backEnd.time_window_checkbox_action)
        self.ui.weekday_radioButton.clicked.connect(backEnd.weekday_radioButton_action)
        self.ui.saturday_radioButton.clicked.connect(backEnd.saturday_radioButton_action)
        self.ui.sunday_radioButton.clicked.connect(backEnd.sunday_radioButton_action)


main_ui = None
frontEnd = None
dm = None
core = None
backEnd = Options_Ui_backEnd()