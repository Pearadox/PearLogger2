#this combo box scrolls only if opend before.
#if the mouse is over the combobox and the mousewheel is turned,
# the mousewheel event of the scrollWidget is triggered
from PyQt5 import QtGui, QtCore, QtWidgets


class ComboBoxNoScroll(QtWidgets.QComboBox):
    def __init__(self, scrollWidget=None, *args, **kwargs):
        super(ComboBoxNoScroll, self).__init__(*args, **kwargs)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.installEventFilter(self)

    def eventFilter(self, QObject, QEvent):
        if QEvent.type() == QEvent.Wheel:
            return True
        return False
