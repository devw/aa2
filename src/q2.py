from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Click me!", self)
        # option 1)  self.button.clicked.connect(handle_button_click)
        # option 2)  self.button.connect.clicked(handle_button_click)
        # option 3)  self.button.connect.clicked(self.handle_button_click)
        # option 4)  self.button.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        print("Button clicked!")


app = QApplication([])
main_window = MyMainWindow()
main_window.show()
app.exec()
