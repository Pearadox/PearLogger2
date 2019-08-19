# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminTool.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.logTab = QtWidgets.QWidget()
        self.logTab.setObjectName("logTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.logTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.logTableWidget = QtWidgets.QTableWidget(self.logTab)
        self.logTableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.logTableWidget.setRowCount(0)
        self.logTableWidget.setColumnCount(7)
        self.logTableWidget.setObjectName("logTableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.logTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.logTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.logTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.logTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.logTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.logTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.logTableWidget.setHorizontalHeaderItem(6, item)
        self.logTableWidget.horizontalHeader().setVisible(True)
        self.logTableWidget.horizontalHeader().setHighlightSections(True)
        self.logTableWidget.horizontalHeader().setStretchLastSection(True)
        self.logTableWidget.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.logTableWidget, 1, 0, 1, 1)
        self.rewriteLogButton = QtWidgets.QPushButton(self.logTab)
        self.rewriteLogButton.setObjectName("rewriteLogButton")
        self.gridLayout_2.addWidget(self.rewriteLogButton, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addButton = QtWidgets.QPushButton(self.logTab)
        self.addButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_2.addWidget(self.addButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.logTab, "")
        self.directoryTab = QtWidgets.QWidget()
        self.directoryTab.setObjectName("directoryTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.directoryTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rewriteDirectoryButton = QtWidgets.QPushButton(self.directoryTab)
        self.rewriteDirectoryButton.setObjectName("rewriteDirectoryButton")
        self.gridLayout_3.addWidget(self.rewriteDirectoryButton, 1, 0, 1, 1)
        self.directoryTableWidget = QtWidgets.QTableWidget(self.directoryTab)
        self.directoryTableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.directoryTableWidget.setRowCount(0)
        self.directoryTableWidget.setColumnCount(5)
        self.directoryTableWidget.setObjectName("directoryTableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.directoryTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.directoryTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.directoryTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.directoryTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.directoryTableWidget.setHorizontalHeaderItem(4, item)
        self.directoryTableWidget.horizontalHeader().setStretchLastSection(True)
        self.directoryTableWidget.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.directoryTableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.directoryTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PearLogger Admin Tool"))
        item = self.logTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Del"))
        item = self.logTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.logTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date In"))
        item = self.logTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date Out"))
        item = self.logTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Login"))
        item = self.logTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Logout"))
        item = self.logTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Time Logged"))
        self.rewriteLogButton.setText(_translate("MainWindow", "Rewrite Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logTab), _translate("MainWindow", "Modify Logs"))
        self.rewriteDirectoryButton.setText(_translate("MainWindow", "Rewrite Directory"))
        item = self.directoryTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Del"))
        item = self.directoryTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.directoryTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name"))
        item = self.directoryTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Picture"))
        item = self.directoryTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Category"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.directoryTab), _translate("MainWindow", "Modify Directory"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
