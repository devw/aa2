# Write a program that displays 9 buttons diagonally. A click on a button returns a dialogue box with the number of the button clicked.

from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gridLayout = QGridLayout()
        self.setWindowTitle('Window title')
        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.gridLayout)
        self.show()

        for i in range(1, 10):
            btn = QPushButton('Btn' + ' ' + str(i), self)
            btn.clicked.connect(self.displayBtn)
            self.gridLayout.addWidget(btn, i, i)

    def displayBtn(self):
        text = self.sender().text()
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText(text)
        dlg.show()


app = QApplication([])

window = MainWindow()
window.show()
app.exec()
