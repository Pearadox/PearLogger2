# front and back end GUI
import re
import time

from PyQt5 import QtCore, QtGui, QtWidgets

from GUI.GUIOptionsDialog import Ui_optionsDialog
from PearLogger_Utils import Profile, Constants

# Manages user interaction with GUI, passes on logistics to Core class
class Options_Ui_backEnd(object):

    def initialize(self):
        self.initialize_leaderboard_checkboxes()
        self.initialize_time_rules()

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

    def initialize_time_rules(self):
        # set widget values based on current config
        

        # turn on labels based on checkbox state
        self.time_length_limit_checkbox_action()
        self.time_window_checkbox_action()

    def time_length_limit_checkbox_action(self):
        frontEnd.ui.minimum_hours_label.setVisible(frontEnd.ui.time_length_limit_checkBox.isChecked())
        frontEnd.ui.maximum_hours_label.setVisible(frontEnd.ui.time_length_limit_checkBox.isChecked())
        frontEnd.ui.minimum_hours_spinBox.setVisible(frontEnd.ui.time_length_limit_checkBox.isChecked())
        frontEnd.ui.maximun_hours_spinBox.setVisible(frontEnd.ui.time_length_limit_checkBox.isChecked())

    def time_window_checkbox_action(self):
        frontEnd.ui.window_open_label.setVisible(frontEnd.ui.time_window_checkBox.isChecked())
        frontEnd.ui.window_close_label.setVisible(frontEnd.ui.time_window_checkBox.isChecked())
        frontEnd.ui.window_open_timeEdit.setVisible(frontEnd.ui.time_window_checkBox.isChecked())
        frontEnd.ui.window_close_timeEdit.setVisible(frontEnd.ui.time_window_checkBox.isChecked())

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

    # action when button pressed
    def apply_button_action(self):
        # check box config
        self.record_leaderboard_checkbox_config()
        # update leaderboard to show filter
        core.updateLeaderboard()

        # update config file
        dm.rewriteConfig()

class Options_Ui_frontEnd(object):

    def post_initialization_tasks(self):
        backEnd.initialize()

    # constructor, initialize UI
    def initialize(self, coreInstance, dataManager):
        global dm, frontEnd, core
        core = coreInstance
        dm = dataManager
        frontEnd = self

        self.OptionsDialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint
                                            | QtCore.Qt.WindowCloseButtonHint)
        self.ui = Ui_optionsDialog()
        self.ui.setupUi(self.OptionsDialog)

        self.customConfiguration()
        self.post_initialization_tasks()

        self.OptionsDialog.exec_()

    # custom UI configurations
    def customConfiguration(self):
        self.ui.apply_button.clicked.connect(backEnd.apply_button_action)
        self.ui.time_length_limit_checkBox.clicked.connect(backEnd.time_length_limit_checkbox_action)
        self.ui.time_window_checkBox.clicked.connect(backEnd.time_window_checkbox_action)


frontEnd = None
dm = None
core = None
backEnd = Options_Ui_backEnd()