# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PearLog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        mainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("G:/Private/Pictures/Pearadox Logo.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("background-color: rgb(230,230,230)")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.studentTable = QtWidgets.QTableWidget(self.centralwidget)
        self.studentTable.setGeometry(QtCore.QRect(10, 0, 1532, 682))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentTable.sizePolicy().hasHeightForWidth())
        self.studentTable.setSizePolicy(sizePolicy)
        self.studentTable.setAlternatingRowColors(False)
        self.studentTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.studentTable.setGridStyle(QtCore.Qt.DotLine)
        self.studentTable.setWordWrap(False)
        self.studentTable.setCornerButtonEnabled(False)
        self.studentTable.setRowCount(4)
        self.studentTable.setColumnCount(9)
        self.studentTable.setObjectName("studentTable")
        self.studentTable.horizontalHeader().setVisible(False)
        self.studentTable.horizontalHeader().setDefaultSectionSize(170)
        self.studentTable.horizontalHeader().setHighlightSections(False)
        self.studentTable.verticalHeader().setVisible(False)
        self.studentTable.verticalHeader().setDefaultSectionSize(170)
        self.studentTable.verticalHeader().setHighlightSections(False)
        self.mentorTable = QtWidgets.QTableWidget(self.centralwidget)
        self.mentorTable.setGeometry(QtCore.QRect(10, 690, 1532, 342))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mentorTable.sizePolicy().hasHeightForWidth())
        self.mentorTable.setSizePolicy(sizePolicy)
        self.mentorTable.setAlternatingRowColors(False)
        self.mentorTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.mentorTable.setShowGrid(True)
        self.mentorTable.setGridStyle(QtCore.Qt.DotLine)
        self.mentorTable.setWordWrap(False)
        self.mentorTable.setCornerButtonEnabled(False)
        self.mentorTable.setRowCount(2)
        self.mentorTable.setColumnCount(9)
        self.mentorTable.setObjectName("mentorTable")
        self.mentorTable.horizontalHeader().setVisible(False)
        self.mentorTable.horizontalHeader().setDefaultSectionSize(170)
        self.mentorTable.verticalHeader().setVisible(False)
        self.mentorTable.verticalHeader().setDefaultSectionSize(170)
        self.mentorTable.verticalHeader().setHighlightSections(True)
        self.mentorTable.verticalHeader().setStretchLastSection(False)
        self.loginLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.loginLineEdit.setGeometry(QtCore.QRect(1550, 0, 361, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginLineEdit.sizePolicy().hasHeightForWidth())
        self.loginLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.loginLineEdit.setFont(font)
        self.loginLineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.loginLineEdit.setText("")
        self.loginLineEdit.setMaxLength(13)
        self.loginLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.loginLineEdit.setObjectName("loginLineEdit")
        self.leaderboardTable = QtWidgets.QTableWidget(self.centralwidget)
        self.leaderboardTable.setGeometry(QtCore.QRect(1550, 330, 361, 702))
        self.leaderboardTable.setGridStyle(QtCore.Qt.DotLine)
        self.leaderboardTable.setRowCount(10)
        self.leaderboardTable.setColumnCount(1)
        self.leaderboardTable.setObjectName("leaderboardTable")
        self.leaderboardTable.horizontalHeader().setVisible(False)
        self.leaderboardTable.horizontalHeader().setDefaultSectionSize(360)
        self.leaderboardTable.horizontalHeader().setHighlightSections(False)
        self.leaderboardTable.verticalHeader().setVisible(False)
        self.leaderboardTable.verticalHeader().setDefaultSectionSize(70)
        self.leaderboardTable.verticalHeader().setHighlightSections(False)
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(1550, 70, 361, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.errorLabel.setFont(font)
        self.errorLabel.setText("")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuPeople = QtWidgets.QMenu(self.menubar)
        self.menuPeople.setObjectName("menuPeople")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionOptions = QtWidgets.QAction(mainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.actionView_Hours = QtWidgets.QAction(mainWindow)
        self.actionView_Hours.setObjectName("actionView_Hours")
        self.actionGenerate_Report = QtWidgets.QAction(mainWindow)
        self.actionGenerate_Report.setObjectName("actionGenerate_Report")
        self.actionReload_Data = QtWidgets.QAction(mainWindow)
        self.actionReload_Data.setObjectName("actionReload_Data")
        self.actionAdd_Person = QtWidgets.QAction(mainWindow)
        self.actionAdd_Person.setObjectName("actionAdd_Person")
        self.actionSign_Out_All = QtWidgets.QAction(mainWindow)
        self.actionSign_Out_All.setObjectName("actionSign_Out_All")
        self.actionClear_All = QtWidgets.QAction(mainWindow)
        self.actionClear_All.setObjectName("actionClear_All")
        self.actionModify_Person = QtWidgets.QAction(mainWindow)
        self.actionModify_Person.setObjectName("actionModify_Person")
        self.menuActions.addAction(self.actionSign_Out_All)
        self.menuActions.addAction(self.actionClear_All)
        self.menuPeople.addAction(self.actionAdd_Person)
        self.menuPeople.addAction(self.actionModify_Person)
        self.menuPeople.addSeparator()
        self.menuPeople.addAction(self.actionView_Hours)
        self.menuFile.addAction(self.actionGenerate_Report)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOptions)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionReload_Data)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuPeople.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.menuActions.setTitle(_translate("mainWindow", "Actions"))
        self.menuPeople.setTitle(_translate("mainWindow", "People"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.actionOptions.setText(_translate("mainWindow", "Options"))
        self.actionView_Hours.setText(_translate("mainWindow", "View Hours"))
        self.actionGenerate_Report.setText(_translate("mainWindow", "Generate Report"))
        self.actionReload_Data.setText(_translate("mainWindow", "Reload Data"))
        self.actionAdd_Person.setText(_translate("mainWindow", "Add Person"))
        self.actionSign_Out_All.setText(_translate("mainWindow", "Sign Out All"))
        self.actionClear_All.setText(_translate("mainWindow", "Clear All"))
        self.actionModify_Person.setText(_translate("mainWindow", "Modify Person"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

