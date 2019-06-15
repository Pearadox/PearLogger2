# Program starts here
# Creates GUI, reads in files, and starts running
import sys

if __name__ == "__main__":

    from PearLogger_UI import Ui_frontEnd
    from PearLogger_Core import Core

    core = Core()
    core.initialize()
    frontEnd = Ui_frontEnd()
