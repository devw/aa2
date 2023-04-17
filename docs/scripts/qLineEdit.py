# The QMainWindow is a widget used as a top-level window that provides a window with a menu bar and a central widget area where the application's main content is displayed. 
# The QLineEdit is a widget used for inputting single-line text values. It is a graphical control element that allows users to enter and edit text.
# Please finish writing the code to create a widget that enables users to input single-line text values.

# from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
# from PyQt6.QtCore import QCoreApplication

# class Window(): # Create a class that inherits from QMainWindow
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle() # Set the window title to "My Window Title"
#         self.lineEdit = QLineEdit()
#         self.lineEdit.setMaxLength() # set the maximum number of characters that can be entered to 15 chars
#         self.lineEdit.setPlaceholderText() # set the placeholder text of the input field to "Enter your text"
#         self.setCentralWidget() # set the widget QLineEdit as the central widget of the QMainWindow. 

# app = QCoreApplication.instance()
# app = QApplication([])
# window = Window()
# window.show()
# app.exec()


from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtCore import QCoreApplication

class Window(QMainWindow): # Create a class that inherits from QMainWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window Title") # Set the window title to "My Window Title"
        self.lineEdit = QLineEdit()
        # self.lineEdit.setMaxLength(10)
        self.lineEdit.setPlaceholderText("Enter your text") # set the placeholder text of the input field to "Enter your text"
        self.setCentralWidget(self.lineEdit) # set the widget QLineEdit as the central widget of the QMainWindow. 

app = QCoreApplication.instance()
app = QApplication([])
window = Window()
window.show()
app.exec()
