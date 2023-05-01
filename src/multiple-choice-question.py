
# Import the necessary classes from PyQt6.QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox


# Create a class that inherits from QWidget
class MultipleChoiceQuestion(QWidget):
    def __init__(self, question, choices, correct_answer):
        super().__init__()

        # Set the window title to "Multiple Choice Question" (setWindowTitle)
        self.setWindowTitle("Multiple Choice Question")

        # Create a vertical box layout (QVBoxLayout) for the window
        qVBoxLayout = QVBoxLayout()

        # Create a label to display the question text (QLabel)
        question_label = QLabel(question)

        # Add to the "vertical box layout" the question
        qVBoxLayout.addWidget(question_label)

        # Create a list of checkboxes (QCheckBox) for each answer choice
        self.qCheckBoxes = []
        for choice in choices:
            self.qCheckBoxes.append(QCheckBox(choice))

        # Add to the "vertical box layout" the checkboxes
        for qCheckBox in self.qCheckBoxes:
            qVBoxLayout.addWidget(qCheckBox)

        # Create a button to check the answer (QPushButton)
        button = QPushButton("Check")

        # Add the button to the  "vertical box layout"
        qVBoxLayout.addWidget(button)

        # Create a connection btw the button and a slot via the "clicked" event.
        button.clicked.connect(self.check_answer)

        # Set the layout in the window
        self.setLayout(qVBoxLayout)

    def check_answer(self):
        # Check if the selected answer is correct (QCheckBox.isChecked, QCheckBox.text)
        answers = []
        for qCheckBox in self.qCheckBoxes:
            if qCheckBox.isChecked():
                answers.append(qCheckBox.text())
        # Create two message boxes (QMessageBox)
        # Set the QMessageBox title to Correct!/Incorrect! (setWindowTitle)
        # Set the QMessageBox text to "Congratulations! Your answer is correct". (setText)
        # Run the event loop on the two message boxes
        if answers == correct_answer:
            print("Correct")
            qMessageBox = QMessageBox()
            qMessageBox.setWindowTitle("Correct!")
            qMessageBox.setText("Congratulations! Your answer is correct")
            qMessageBox.exec()
        else:
            print("Correct")
            qMessageBox = QMessageBox()
            qMessageBox.setWindowTitle("Incorrect!")
            qMessageBox.setText("Sorry! Your answer is incorrect")
            qMessageBox.exec()


# Create a new QApplication instance
app = QApplication([])
# Create the multiple choice question widget
question = "What is the capital of France?"
choices = ["Paris", "London", "Berlin", "Madrid"]
correct_answer = ["Paris"]
window = MultipleChoiceQuestion(question, choices, correct_answer)
# Show the window
window.show()
# Run the event loop
app.exec()
