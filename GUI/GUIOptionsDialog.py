# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OptionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_optionsDialog(object):
    def setupUi(self, optionsDialog):
        optionsDialog.setObjectName("optionsDialog")
        optionsDialog.resize(888, 601)
        self.tabWidget = QtWidgets.QTabWidget(optionsDialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 891, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.log_rules_tab = QtWidgets.QWidget()
        self.log_rules_tab.setObjectName("log_rules_tab")
        self.time_length_limit_checkBox = QtWidgets.QCheckBox(self.log_rules_tab)
        self.time_length_limit_checkBox.setGeometry(QtCore.QRect(50, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(15)
        self.time_length_limit_checkBox.setFont(font)
        self.time_length_limit_checkBox.setObjectName("time_length_limit_checkBox")
        self.minimum_hours_label = QtWidgets.QLabel(self.log_rules_tab)
        self.minimum_hours_label.setGeometry(QtCore.QRect(50, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.minimum_hours_label.setFont(font)
        self.minimum_hours_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.minimum_hours_label.setObjectName("minimum_hours_label")
        self.minimum_hours_spinBox = QtWidgets.QDoubleSpinBox(self.log_rules_tab)
        self.minimum_hours_spinBox.setGeometry(QtCore.QRect(170, 100, 91, 31))
        self.minimum_hours_spinBox.setDecimals(1)
        self.minimum_hours_spinBox.setMaximum(999.0)
        self.minimum_hours_spinBox.setObjectName("minimum_hours_spinBox")
        self.maximum_hours_label = QtWidgets.QLabel(self.log_rules_tab)
        self.maximum_hours_label.setGeometry(QtCore.QRect(40, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.maximum_hours_label.setFont(font)
        self.maximum_hours_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maximum_hours_label.setObjectName("maximum_hours_label")
        self.maximum_hours_spinBox = QtWidgets.QDoubleSpinBox(self.log_rules_tab)
        self.maximum_hours_spinBox.setGeometry(QtCore.QRect(170, 140, 91, 31))
        self.maximum_hours_spinBox.setDecimals(1)
        self.maximum_hours_spinBox.setMaximum(999.0)
        self.maximum_hours_spinBox.setObjectName("maximum_hours_spinBox")
        self.time_window_checkBox = QtWidgets.QCheckBox(self.log_rules_tab)
        self.time_window_checkBox.setGeometry(QtCore.QRect(50, 190, 201, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(15)
        self.time_window_checkBox.setFont(font)
        self.time_window_checkBox.setObjectName("time_window_checkBox")
        self.window_open_label = QtWidgets.QLabel(self.log_rules_tab)
        self.window_open_label.setGeometry(QtCore.QRect(20, 230, 141, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.window_open_label.setFont(font)
        self.window_open_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.window_open_label.setObjectName("window_open_label")
        self.window_close_label = QtWidgets.QLabel(self.log_rules_tab)
        self.window_close_label.setGeometry(QtCore.QRect(20, 270, 141, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.window_close_label.setFont(font)
        self.window_close_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.window_close_label.setObjectName("window_close_label")
        self.window_open_timeEdit = QtWidgets.QTimeEdit(self.log_rules_tab)
        self.window_open_timeEdit.setGeometry(QtCore.QRect(170, 230, 118, 31))
        self.window_open_timeEdit.setObjectName("window_open_timeEdit")
        self.window_close_timeEdit = QtWidgets.QTimeEdit(self.log_rules_tab)
        self.window_close_timeEdit.setGeometry(QtCore.QRect(170, 270, 118, 31))
        self.window_close_timeEdit.setObjectName("window_close_timeEdit")
        self.tabWidget.addTab(self.log_rules_tab, "")
        self.leaderboard_tab = QtWidgets.QWidget()
        self.leaderboard_tab.setObjectName("leaderboard_tab")
        self.label = QtWidgets.QLabel(self.leaderboard_tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.student_dawson_checkBox = QtWidgets.QCheckBox(self.leaderboard_tab)
        self.student_dawson_checkBox.setGeometry(QtCore.QRect(30, 50, 151, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.student_dawson_checkBox.setFont(font)
        self.student_dawson_checkBox.setObjectName("student_dawson_checkBox")
        self.student_pearland_checkBox = QtWidgets.QCheckBox(self.leaderboard_tab)
        self.student_pearland_checkBox.setGeometry(QtCore.QRect(30, 80, 151, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.student_pearland_checkBox.setFont(font)
        self.student_pearland_checkBox.setObjectName("student_pearland_checkBox")
        self.student_turner_checkBox = QtWidgets.QCheckBox(self.leaderboard_tab)
        self.student_turner_checkBox.setGeometry(QtCore.QRect(30, 110, 151, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.student_turner_checkBox.setFont(font)
        self.student_turner_checkBox.setObjectName("student_turner_checkBox")
        self.alumni_checkBox = QtWidgets.QCheckBox(self.leaderboard_tab)
        self.alumni_checkBox.setGeometry(QtCore.QRect(30, 140, 151, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.alumni_checkBox.setFont(font)
        self.alumni_checkBox.setObjectName("alumni_checkBox")
        self.mentor_checkBox = QtWidgets.QCheckBox(self.leaderboard_tab)
        self.mentor_checkBox.setGeometry(QtCore.QRect(30, 170, 151, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.mentor_checkBox.setFont(font)
        self.mentor_checkBox.setObjectName("mentor_checkBox")
        self.teacher_checkBox = QtWidgets.QCheckBox(self.leaderboard_tab)
        self.teacher_checkBox.setGeometry(QtCore.QRect(30, 200, 151, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.teacher_checkBox.setFont(font)
        self.teacher_checkBox.setObjectName("teacher_checkBox")
        self.team_checkBox = QtWidgets.QCheckBox(self.leaderboard_tab)
        self.team_checkBox.setGeometry(QtCore.QRect(30, 230, 151, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.team_checkBox.setFont(font)
        self.team_checkBox.setObjectName("team_checkBox")
        self.other_checkBox = QtWidgets.QCheckBox(self.leaderboard_tab)
        self.other_checkBox.setGeometry(QtCore.QRect(30, 260, 151, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.other_checkBox.setFont(font)
        self.other_checkBox.setObjectName("other_checkBox")
        self.tabWidget.addTab(self.leaderboard_tab, "")
        self.apply_button = QtWidgets.QPushButton(optionsDialog)
        self.apply_button.setGeometry(QtCore.QRect(750, 570, 121, 23))
        self.apply_button.setObjectName("apply_button")

        self.retranslateUi(optionsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(optionsDialog)

    def retranslateUi(self, optionsDialog):
        _translate = QtCore.QCoreApplication.translate
        optionsDialog.setWindowTitle(_translate("optionsDialog", "Options"))
        self.time_length_limit_checkBox.setText(_translate("optionsDialog", "Time Length Limit"))
        self.minimum_hours_label.setText(_translate("optionsDialog", "Minimum Hours:"))
        self.maximum_hours_label.setText(_translate("optionsDialog", "Maximum Hours:"))
        self.time_window_checkBox.setText(_translate("optionsDialog", "Time Window"))
        self.window_open_label.setText(_translate("optionsDialog", "Window Open Time:"))
        self.window_close_label.setText(_translate("optionsDialog", "Window Close Time:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log_rules_tab), _translate("optionsDialog", "Log Rules"))
        self.label.setText(_translate("optionsDialog", "Visible Categories"))
        self.student_dawson_checkBox.setText(_translate("optionsDialog", "Student (Dawson)"))
        self.student_pearland_checkBox.setText(_translate("optionsDialog", "Student (Pearland)"))
        self.student_turner_checkBox.setText(_translate("optionsDialog", "Student (Turner)"))
        self.alumni_checkBox.setText(_translate("optionsDialog", "Alumni"))
        self.mentor_checkBox.setText(_translate("optionsDialog", "Mentor"))
        self.teacher_checkBox.setText(_translate("optionsDialog", "Teacher"))
        self.team_checkBox.setText(_translate("optionsDialog", "Team"))
        self.other_checkBox.setText(_translate("optionsDialog", "Other"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.leaderboard_tab), _translate("optionsDialog", "Leaderboard"))
        self.apply_button.setText(_translate("optionsDialog", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    optionsDialog = QtWidgets.QDialog()
    ui = Ui_optionsDialog()
    ui.setupUi(optionsDialog)
    optionsDialog.show()
    sys.exit(app.exec_())

