# front and back end GUI

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsOpacityEffect

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
            main_backEnd.showError_popup(
                "Profile Picture Location Error", "Please move the picture under data/profilepics/ and try again")

    def preview_button_trigger(self):
        # set preview of label using lineedit
        self.setPreview('data/profilepics/' + frontEnd.ui.picture_file_line_edit.text())

    # sends all data to core -> data manager and adds to file
    def addPerson_button_trigger(self):
        # make sure form is complete
        incompleteForm = False

        # get name
        person_name = str.strip(frontEnd.ui.name_lineEdit.text())
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

        # get graduation year if person is student
        graduation_year = -1
        if category_number is 1 or category_number is 2 or category_number is 3:
            graduation_year = frontEnd.ui.graduation_year_spinBox.value()

        # get picture name
        picture_filename = str.strip(frontEnd.ui.picture_file_line_edit.text())
        # set to default if empty
        if len(picture_filename) == 0:
            picture_filename = "default.jpg"

        # only add if form is complete
        if not incompleteForm:
            core.add_person(person_name, category_number, picture_filename, graduation_year, main_backEnd)
            self.clearAllFields()
        else:
            print("Incomplete form")
            main_backEnd.showError_popup("Incomplete Form","Name and Category must be filled in.")

    # clears all input fields
    def clearAllFields(self):
        self.setPreview('data/profilepics/default.jpg')
        frontEnd.ui.name_lineEdit.setText("")
        frontEnd.ui.picture_file_line_edit.setText("")
        frontEnd.ui.category_comboBox.setCurrentIndex(0)
        pass

    # sets picture preview
    def setPreview(self, picture_path):
        # default picture if path is incomplete
        if picture_path == 'data/profilepics/':
            picture_path = 'data/profilepics/default.jpg'

        #  add picture preview
        pixmap_raw = QtGui.QPixmap(picture_path)
        pixmap_scaled = pixmap_raw.scaled(frontEnd.ui.preview_label.size(), QtCore.Qt.KeepAspectRatio)

        # associate picture to the label
        frontEnd.ui.preview_label.setPixmap(pixmap_scaled)
        # align picture to center
        frontEnd.ui.preview_label.setAlignment(QtCore.Qt.AlignHCenter)

    def comboBox_index_trigger(self):
        index = frontEnd.ui.category_comboBox.currentIndex()
        if index is 1 or index is 2 or index is 3:
            frontEnd.ui.graduation_year_spinBox.setDisabled(False)
        else:
            frontEnd.ui.graduation_year_spinBox.setDisabled(True)


class Add_Person_Ui_frontEnd(object):

    def post_initialization_tasks(self):
        backEnd.initialize()

        self.ui.category_comboBox.addItem("")

        for category_name in Profile.CATEGORY__DICTIONARY.values():
            self.ui.category_comboBox.addItem(category_name)

    # constructor, initialize UI
    def initialize(self, add_person_ui, initialized_core, initialized_main_backEnd):
        global frontEnd, core, main_backEnd
        frontEnd = add_person_ui
        core = initialized_core
        main_backEnd = initialized_main_backEnd

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
        self.ui.category_comboBox.currentIndexChanged.connect(backEnd.comboBox_index_trigger)


main_backEnd = None
frontEnd = None
core = None
backEnd = Add_Person_Ui_backEnd()