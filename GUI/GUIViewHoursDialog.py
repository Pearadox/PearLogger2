# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewHoursDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewHours_Dialog(object):
    def setupUi(self, ViewHours_Dialog):
        ViewHours_Dialog.setObjectName("ViewHours_Dialog")
        ViewHours_Dialog.resize(1030, 616)
        self.lineEdit = QtWidgets.QLineEdit(ViewHours_Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 1011, 31))
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(80)
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(ViewHours_Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 1011, 551))
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)

        self.retranslateUi(ViewHours_Dialog)
        QtCore.QMetaObject.connectSlotsByName(ViewHours_Dialog)

    def retranslateUi(self, ViewHours_Dialog):
        _translate = QtCore.QCoreApplication.translate
        ViewHours_Dialog.setWindowTitle(_translate("ViewHours_Dialog", "View Hours"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ViewHours_Dialog", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewHours_Dialog", "Logged Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ViewHours_Dialog", "School"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ViewHours_Dialog", "ID"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewHours_Dialog = QtWidgets.QDialog()
    ui = Ui_ViewHours_Dialog()
    ui.setupUi(ViewHours_Dialog)
    ViewHours_Dialog.show()
    sys.exit(app.exec_())

