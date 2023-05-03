from PyQt6.QtWidgets import QApplication

class MyWidget(): # Create a class that inherits from QWidget

    def __init__(self):
        super().__init__()
        vbox = None # Create a vertical layout widget via the QVBoxLayout widget
       
        self.line_edit = None  # Create a QLineEdit widget
        # add the  QLineEdit widget to the vertical layout widget via the addWidget method

        
        self.button = None # Create a QPushButton widget 
        # Add the button widget to the vertical layout widget via the addWidget method
        # Create a connection between a SIGNAL (clicked) and a SLOT that is triggered when the button is clicked.

        self.label = None  # Create a QLabel widget to display the text
         # add the label widget to the vertical layout widget via the addWidget method

        # Add the vertical layout widget to MyWidget class via the setLayout method

    def display_text(self):
        text = None # Get the text from the QLineEdit widget via the text method

        msg_box = None  # Create QMessageBox popup widget
        # Display the text in a QMessageBox popup via the setText method
        msg_box.exec()


app = QApplication([])
widget = MyWidget()
widget.show()
app.exec()

#########################!SECTION

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout, QPushButton, QMessageBox

class MyWidget(QWidget): # Create a class that inherits from QWidget

    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout() # Create a vertical layout widget via the QVBoxLayout widget
       
        self.line_edit = QLineEdit()  # Create a QLineEdit widget
        vbox.addWidget(self.line_edit) # add the  QLineEdit widget to the vertical layout widget via the addWidget method

        
        self.button = QPushButton("Push me!") # Create a QPushButton widget 
        vbox.addWidget(self.button) # Add the button widget to the vertical layout widget via the addWidget method
        self.button.clicked.connect(self.display_text) # Create a connection between a SIGNAL (clicked) and a SLOT that is triggered when the button is clicked.

        self.label = QLabel()  # Create a QLabel widget to display the text
        vbox.addWidget(self.label) # add the label widget to the vertical layout widget via the addWidget method

        self.setLayout(vbox) # Add the vertical layout widget to MyWidget class via the setLayout method

    def display_text(self):
        text = self.line_edit.text() # Get the text from the QLineEdit widget via the text method

        msg_box = QMessageBox()  # Create QMessageBox popup widget
        msg_box.setText(text)
        # Display the text in a QMessageBox popup via the setText method
        msg_box.exec()


app = QApplication([])
widget = MyWidget()
widget.show()
app.exec()





#################

# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

# class MyWidget2(QWidget):

#     def __init__(self):
#         super().__init__()
#         vbox = QVBoxLayout() # Create a vertical layout via the QVBoxLayout widget
       
#         self.line_edit = QLineEdit()  # Create a QLineEdit widget
#         vbox.addWidget(self.line_edit)

        
#         self.button = QPushButton("Display Text") # Create a QPushButton widget
#         self.button.clicked.connect(self.display_text)
#         vbox.addWidget(self.button)

#         self.label = QLabel()  # Create a QLabel widget to display the text
#         vbox.addWidget(self.label)

#         self.setLayout(vbox) # Set the layout of the widget

#     def display_text(self):
#         text = self.line_edit.text()  # Get the text from the QLineEdit widget

#         msg_box = QMessageBox() # Display the text in a QMessageBox popup
#         msg_box.setText("You typed: " + text)
#         msg_box.exec()


# app = QApplication([])
# widget = MyWidget2()
# widget.show()
# app.exec()
