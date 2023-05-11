# Look at the following code and select the correct option among the 2 proposed to create the MyWidget class that inherits from the QWidget class.
from PyQt5.QtWidgets import QWidget


# option 1
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

# option 2


class MyWidget(self):
    def __init__(QWidget):
        super().__init__()
