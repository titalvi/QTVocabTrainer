# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""
TO-DO:
 - start building HTML table in display (for glossary)
 - implement XML database
 - get fetch and manipulate XML database with lxml (https://lxml.de/tutorial.html)
 - create second view/window for exercises

COMPLETED:
 - automatically create link for source language word to source dictionary information (i.e. OED etc)
 - add current files to GitHub repo (https://github.com/titalvi/QtVocabTrainer)
"""


from PyQt5 import QtWidgets
from untitled import Ui_Dialog # Importing our generated file
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
"""
from PyQt5 import QtWidgets # import PyQt5 widgets
import sys

# Create the application object
app = QtWidgets.QApplication(sys.argv)

# Create the form object
first_window = QtWidgets.QWidget()

# Set window size
first_window.resize(400, 300)

# Set the form title
first_window.setWindowTitle("Welcome to QtVocabTrainer!")

# Show form
first_window.show()

# Run the program
sys.exit(app.exec())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""



class mywindow(QtWidgets.QDialog):


    def __init__(self):
        super(mywindow, self).__init__()

        self.ui = Ui_Dialog()

        self.ui.setupUi(self)


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())

