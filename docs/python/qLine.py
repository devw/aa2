import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit
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
    app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
