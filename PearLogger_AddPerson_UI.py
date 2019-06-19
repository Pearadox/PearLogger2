# front and back end GUI

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsOpacityEffect

import PearLogger_Core
import PearLogger_UI
from GUI.GUIAddPersonDialog import Ui_AddPersonDialog
from PearLogger_Utils import Profile

# Manages user interaction with GUI, passes on logistics to Core class
class Add_Person_Ui_backEnd(object):

    picture_filename = 'default.jpg'

    def initialize(self):
        # display default picture
        self.setPreview('data/profilepics/default.jpg')

    def browse_button_trigger(self):
        # create dialog to ask for file
        path = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "data/profilepics",
                                                     "Picture Files (*.jpg; *.png)")[0]
        #  return if user hits cancel
        if len(path) == 0:
            return
        try:
            index = path.index('data/profilepics/') + len('data/profilepics/')
            filename = path[index:]

            # create preview of picture
            self.setPreview(path)

            # set text of line edit to the file name
            frontEnd.ui.picture_file_line_edit.setText(filename)
        except Exception as e:
            print(e)
            print("Error with Picture")

    def preview_button_trigger(self):
        # set preview of label using lineedit
        self.setPreview('data/profilepics/' + frontEnd.ui.picture_file_line_edit.text())

    def addPerson_button_trigger(self):
        # make sure form is complete
        incompleteForm = False

        # get name
        person_name = frontEnd.ui.name_lineEdit.text()
        # make sure name is filled
        incompleteForm |= len(person_name) is 0

        # get category number by reverse dictionary
        category_number = -1
        # get combobox selected category name
        category_name = frontEnd.ui.category_comboBox.currentText()
        # find category number that matches name
        for num, name in Profile.CATEGORY__DICTIONARY.items():
            if name == category_name:
                category_number = num
                break
        # make sure category found
        incompleteForm |= category_number is -1

        # get picture name
        picture_filename = self.picture_filename

        # only add if form is complete
        if not incompleteForm:
            core.add_person(person_name, category_number, picture_filename)
            self.clearAllFields()
        else:
            print("Incomplete form")

    def clearAllFields(self):
        pass

    def setPreview(self, picture_path):
        #  add picture preview
        pixmap_raw = QtGui.QPixmap(picture_path)
        pixmap_scaled = pixmap_raw.scaled(frontEnd.ui.preview_label.size(), QtCore.Qt.KeepAspectRatio)

        # associate picture to the label
        frontEnd.ui.preview_label.setPixmap(pixmap_scaled)
        # align picture to center
        frontEnd.ui.preview_label.setAlignment(QtCore.Qt.AlignHCenter)


class Add_Person_Ui_frontEnd(object):

    def post_initialization_tasks(self):
        backEnd.initialize()

        self.ui.category_comboBox.addItem("")
        for category_name in Profile.CATEGORY__DICTIONARY.values():
            self.ui.category_comboBox.addItem(category_name)

    # constructor, initialize UI
    def initialize(self, add_person_ui, initialized_core):
        global frontEnd, core
        frontEnd = add_person_ui
        core = initialized_core

        self.AddPersonDialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint
                                            | QtCore.Qt.WindowCloseButtonHint)
        self.ui = Ui_AddPersonDialog()
        self.ui.setupUi(self.AddPersonDialog)

        self.customConfiguration()
        self.post_initialization_tasks()

        self.AddPersonDialog.exec_()

    # custom UI configurations
    def customConfiguration(self):
        self.ui.name_lineEdit.setFocus(True)
        self.ui.preview_browse_button.pressed.connect(backEnd.browse_button_trigger)
        self.ui.preview_button.pressed.connect(backEnd.preview_button_trigger)
        self.ui.add_person_button.pressed.connect(backEnd.addPerson_button_trigger)

frontEnd = None
core = None
backEnd = Add_Person_Ui_backEnd()