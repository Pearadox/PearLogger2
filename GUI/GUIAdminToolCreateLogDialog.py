# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminToolCreateLogDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogEntryDialog(object):
    def setupUi(self, LogEntryDialog):
        LogEntryDialog.setObjectName("LogEntryDialog")
        LogEntryDialog.resize(206, 78)
        self.formLayout = QtWidgets.QFormLayout(LogEntryDialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(LogEntryDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(LogEntryDialog)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.submitButton = QtWidgets.QPushButton(LogEntryDialog)
        self.submitButton.setObjectName("submitButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.submitButton)

        self.retranslateUi(LogEntryDialog)
        QtCore.QMetaObject.connectSlotsByName(LogEntryDialog)

    def retranslateUi(self, LogEntryDialog):
        _translate = QtCore.QCoreApplication.translate
        LogEntryDialog.setWindowTitle(_translate("LogEntryDialog", "Create Log Entry"))
        self.label.setText(_translate("LogEntryDialog", "ID:"))
        self.submitButton.setText(_translate("LogEntryDialog", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogEntryDialog = QtWidgets.QDialog()
    ui = Ui_LogEntryDialog()
    ui.setupUi(LogEntryDialog)
    LogEntryDialog.show()
    sys.exit(app.exec_())
