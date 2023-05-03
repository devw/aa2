from PyQt6.QtWidgets import QApplication, QTextEdit, QMainWindow

# Create a class that inherits from QMainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Add a title to the main widget via "setWindowTitle" method
        self.setWindowTitle("My title")

        # create an instance of QTextEdit widget
        qTextEdit = QTextEdit()

        # Add a line to QTextEdit widget via "setText" method
        qTextEdit.setText("1st line")

        # Add a 2nd line to QTextEdit widget via "append" method
        qTextEdit.append("2nd line.")

        # Create a connection btw QTextEdit widget and a slot via the "textChanged" event.
        qTextEdit.textChanged.connect(self.printBla)

        # Add QTextEdit widget to the main widget via "setCentralWidget"
        self.setCentralWidget(qTextEdit)

    def printBla(self):
        print("bla bla")


app = QApplication([])
window = MyWindow()
window.show()
app.exec()
