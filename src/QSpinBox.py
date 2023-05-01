# Import the necessary classes from PyQt5.QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title to `Storming of the Bastille`
        self.setWindowTitle('Storming of the Bastille')

        # Set the window dimensions to 300 pixels in width and 200 pixels in height, and position it at the top right corner of the screen with a distance of 100 pixels from the top and 200 pixels from the right. Use the setGeometry method of QWidget.
        self.setGeometry(100, 200, 300, 200)

        # Create a vertical box layout to organize the widget's contents (QVBoxLayout)
        qVBoxLayout = QVBoxLayout()

        # Create a new QSpinBox widget (QSpinBox)
        qSpinBox = QSpinBox()

        # Set the minimum (1779) and maximum (1799) values for the spin box (setMinimum, setMaximum).
        qSpinBox.setMinimum(1779)
        qSpinBox.setMaximum(1799)

        # Set the initial value for the spin box (setValue)
        qSpinBox.setValue(1780)

        # Add the spin box to the layout (addWidget)
        qVBoxLayout.addWidget(qSpinBox)

        # Set the layout for the widget
        self.setLayout(qVBoxLayout)


# Create a new QApplication instance
app = QApplication([])
# Create the main window
window = MainWindow()
# Show the window
window.show()
# Run the event loop
app.exec()
