from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title to 'I think, therefore I am.'
        self.setWindowTitle('I think, therefore I am.')

        # Set the window dimensions to 300 pixels in width and 200 pixels in height, and position it at the top right corner of the screen with a distance of 100 pixels from the top and 200 pixels from the right. Use the setGeometry method of QWidget.
        self.setGeometry(100, 200, 300, 200)

        # Create two checkboxes with labels 'Immanuel Kant' and 'René Descartes' respectively. (QCheckBox)
        q1 = QCheckBox('Immanuel Kant')
        q2 = QCheckBox('René Descartes')

        # Set the initial state of the checkboxes to be unchecked via the setChecked method
        q1.setChecked(False)
        q2.setChecked(False)

        # Create a vertical layout and add the checkboxes to it (QVBoxLayout, addWidget)
        vl = QVBoxLayout()
        vl.addWidget(q1)
        vl.addWidget(q2)

        # Set the layout for the window
        self.setLayout(vl)


# Create the application object
app = QApplication([])
# Create the main window
window = MainWindow()
# Show the window
window.show()
# Run the event loop
app.exec()
