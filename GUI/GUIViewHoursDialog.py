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
        ViewHours_Dialog.resize(590, 616)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewHours_Dialog.sizePolicy().hasHeightForWidth())
        ViewHours_Dialog.setSizePolicy(sizePolicy)
        self.lineEdit = QtWidgets.QLineEdit(ViewHours_Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 571, 31))
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(80)
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(ViewHours_Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 571, 551))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
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
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(ViewHours_Dialog)
        QtCore.QMetaObject.connectSlotsByName(ViewHours_Dialog)

    def retranslateUi(self, ViewHours_Dialog):
        _translate = QtCore.QCoreApplication.translate
        ViewHours_Dialog.setWindowTitle(_translate("ViewHours_Dialog", "View Hours"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ViewHours_Dialog", "Rank"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewHours_Dialog", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ViewHours_Dialog", "Logged Time"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ViewHours_Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ViewHours_Dialog", "Category"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewHours_Dialog = QtWidgets.QDialog()
    ui = Ui_ViewHours_Dialog()
    ui.setupUi(ViewHours_Dialog)
    ViewHours_Dialog.show()
    sys.exit(app.exec_())

