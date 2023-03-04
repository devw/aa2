from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class Window(QMainWindow):

    def onClick(self):  # slot
        self.counter += 1
        print("click " + str(self.counter) + " !")

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.setWindowTitle("Button title")
        self.button = QPushButton('Click me!')
        self.button.clicked.connect(self.onClick)  # subscribe
        self.setCentralWidget(self.button)


app = QApplication([])
window = Window()
window.show()
app.exec()
