from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QRadioButton


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # Create QCheckBox
        checkbox1 = QCheckBox('Option 1', self)
        checkbox1.setChecked(True)  # Set initial checked state
        checkbox1.stateChanged.connect(self.checkboxStateChanged)

        checkbox2 = QCheckBox('Option 2', self)
        checkbox2.stateChanged.connect(self.checkboxStateChanged)

        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)

        # Create QRadioButton
        radiobutton1 = QRadioButton('Option A', self)
        radiobutton1.setChecked(True)  # Set initial checked state
        radiobutton1.toggled.connect(self.radioButtonToggled)

        radiobutton2 = QRadioButton('Option B', self)
        radiobutton2.toggled.connect(self.radioButtonToggled)

        vbox.addWidget(radiobutton1)
        vbox.addWidget(radiobutton2)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Checkbox and Radiobutton Example')
        self.show()

    def checkboxStateChanged(self, state):
        sender = self.sender()
        if sender.isChecked():
            print(sender.text() + ' checked')
        else:
            print(sender.text() + ' unchecked')

    def radioButtonToggled(self):
        sender = self.sender()
        if sender.isChecked():
            print(sender.text() + ' selected')


app = QApplication([])
ex = Example()
app.exec()
