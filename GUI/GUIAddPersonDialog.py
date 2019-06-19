# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddPersonDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PearLogger_Utils import Profile


class Ui_AddPersonDialog(object):
    def setupUi(self, AddPersonDialog):
        AddPersonDialog.setObjectName("AddPersonDialog")
        AddPersonDialog.resize(350, 450)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        AddPersonDialog.setFont(font)
        self.preview_label = QtWidgets.QLabel(AddPersonDialog)
        self.preview_label.setGeometry(QtCore.QRect(100, 160, 150, 150))
        self.preview_label.setStyleSheet("border:1px solid rgb(0, 0, 0); ")
        self.preview_label.setText("")
        self.preview_label.setObjectName("preview_label")
        self.picture_file_line_edit = QtWidgets.QLineEdit(AddPersonDialog)
        self.picture_file_line_edit.setGeometry(QtCore.QRect(40, 320, 271, 20))
        self.picture_file_line_edit.setObjectName("picture_file_line_edit")
        self.preview_browse_button = QtWidgets.QPushButton(AddPersonDialog)
        self.preview_browse_button.setGeometry(QtCore.QRect(70, 350, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.preview_browse_button.setFont(font)
        self.preview_browse_button.setObjectName("preview_browse_button")
        self.preview_button = QtWidgets.QPushButton(AddPersonDialog)
        self.preview_button.setGeometry(QtCore.QRect(180, 350, 100, 25))
        self.preview_button.setObjectName("preview_button")
        self.name_label = QtWidgets.QLabel(AddPersonDialog)
        self.name_label.setGeometry(QtCore.QRect(40, 30, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_label.setObjectName("name_label")
        self.name_label_2 = QtWidgets.QLabel(AddPersonDialog)
        self.name_label_2.setGeometry(QtCore.QRect(20, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_label_2.setFont(font)
        self.name_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_label_2.setObjectName("name_label_2")
        self.picture_label = QtWidgets.QLabel(AddPersonDialog)
        self.picture_label.setGeometry(QtCore.QRect(100, 130, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.picture_label.setFont(font)
        self.picture_label.setAlignment(QtCore.Qt.AlignCenter)
        self.picture_label.setObjectName("picture_label")
        self.name_lineEdit = QtWidgets.QLineEdit(AddPersonDialog)
        self.name_lineEdit.setGeometry(QtCore.QRect(100, 30, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        self.name_lineEdit.setFont(font)
        self.name_lineEdit.setText("")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.category_comboBox = QtWidgets.QComboBox(AddPersonDialog)
        self.category_comboBox.setGeometry(QtCore.QRect(100, 71, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        self.category_comboBox.setFont(font)
        self.category_comboBox.setObjectName("category_comboBox")
        self.add_person_button = QtWidgets.QPushButton(AddPersonDialog)
        self.add_person_button.setGeometry(QtCore.QRect(40, 390, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_person_button.setFont(font)
        self.add_person_button.setObjectName("add_person_button")

        self.retranslateUi(AddPersonDialog)
        QtCore.QMetaObject.connectSlotsByName(AddPersonDialog)

    def retranslateUi(self, AddPersonDialog):
        _translate = QtCore.QCoreApplication.translate
        AddPersonDialog.setWindowTitle(_translate("AddPersonDialog", "Add Person"))
        self.preview_browse_button.setText(_translate("AddPersonDialog", "Browse"))
        self.preview_button.setText(_translate("AddPersonDialog", "Preview"))
        self.name_label.setText(_translate("AddPersonDialog", "Name"))
        self.name_label_2.setText(_translate("AddPersonDialog", "Category"))
        self.picture_label.setText(_translate("AddPersonDialog", "Picture"))
        self.add_person_button.setText(_translate("AddPersonDialog", "Add Person"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddPersonDialog = QtWidgets.QDialog()
    ui = Ui_AddPersonDialog()
    ui.setupUi(AddPersonDialog)
    AddPersonDialog.show()
    sys.exit(app.exec_())

