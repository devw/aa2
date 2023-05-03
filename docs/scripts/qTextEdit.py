# In PyQt, QTextEdit is a widget for editing and displaying multi-line text values. It is a graphical control element that allows users to enter and edit multiple lines of text.

# QTextEdit provides more advanced text input and editing capabilities than QLineEdit. It supports a rich text format, which allows the user to change the font, colour, and style of the text. It also supports text formatting options such as bullet lists, numbered lists, and tables.

### Exercise 
from PyQt6.QtWidgets import QApplication, QTextEdit
from PyQt6.QtCore import QCoreApplication

class MyWindow(): # Create a class that inherits from QMainWindow
    def __init__(self):
        super().__init__()
        # Set the window title to "My Window Title"
        self.textEdit = # create an instance of QTextEdit
        self.textEdit.setText() # set the text of a widget to "The first line of text."
        self.textEdit.append() # Add a second line to the widget equals to "The second line of text."


app = QCoreApplication.instance()
app = QApplication([])
window = MyWindow()
window.show()
app.exec()

### Solution

from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt6.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Title")
        self.textEdit = QTextEdit()
        self.textEdit.setText("The first line of text.")
        self.textEdit.append("Another text line!")
        # self.textEdit.textChanged.connect(self.text_changed)
        self.setCentralWidget(self.textEdit)

    # def text_changed(self):
    #     print("The text changed!")


app = QCoreApplication.instance()
app = QApplication([])
window = Window()
window.show()
app.exec()
           