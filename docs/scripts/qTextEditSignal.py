# In PyQt, QTextEdit is a widget for editing and displaying multi-line text values. It is a graphical control element that allows users to enter and edit multiple lines of text.

# QTextEdit provides more advanced text input and editing capabilities than QLineEdit. It supports a rich text format, which allows the user to change the font, colour, and style of the text. It also supports text formatting options such as bullet lists, numbered lists, and tables.

### Exercise 
from PyQt6.QtWidgets import QApplication, QTextEdit
from PyQt6.QtCore import QCoreApplication

class MyWindow(): # Create a class that inherits from QMainWindow
    def __init__(self): 
        super().__init__()
        # Set the window title to "My Window Title" via the "setWindowTitle" method
        # create an instance of QTextEdit Widget (<WIDGET>)
        # set the text of the <WIDGET> to "The first line of text." via the "setText" method
        # set the text of the sendon line of the <WIDGET> to "The second line of text." via the "append" method
        <WIDGET>.<SIGNAL>.connect(<SLOT>) # Create a connection between a SIGNAL and a SLOT that is triggered when the text contents of the widget change.
        self.setCentralWidget(<WIDGET>) # Set the WIDGET as the central widget of the QMainWindow. 

    # Create a slot that prints the text "The text changed!" in your terminal



app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MyWindow()
window.show()
app.exec()
           

### Solution 
from PyQt6.QtWidgets import QApplication, QTextEdit, QMainWindow
from PyQt6.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Title")
        self.textEdit = QTextEdit()
        self.textEdit.setText("The first line of text.")
        self.textEdit.append("Another text line!")
        self.textEdit.textChanged.connect(self.text_changed)
        self.setCentralWidget(self.textEdit)

    def text_changed(self):
        print("The text changed!")


app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = Window()
window.show()
app.exec()
           