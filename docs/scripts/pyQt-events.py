from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Button title")
#         self.button = QPushButton('Click me!')
#         self.button.clicked.connect(self.onClick)  # subscribe
#         self.setCentralWidget(self.button)

#     def onClick(self):  # slot
#     print("clic!")


# app = QApplication([])
# window = Window()
# window.show()
# app.exec()

# 2
# coding: utf-8
# On doit importer QPushButton pour le bouton
# et QMessageBox pour le popup

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = QDialog(self)
        dlg.setWindowTitle("HELLO!")
        dlg.exec()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
