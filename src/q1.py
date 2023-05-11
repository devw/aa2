# Look at the following code and select the correct option among the 4 proposed to set the window title to "my title" in a PyQt application.

from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication([])
main_window = QMainWindow()
# option 1)  self.setWindowTitle("my title")
# option 2)  QMainWindow.setWindowTitle("my title")
# option 3)  main_window.setWindowTitle("my title")
# option 4)  QApplication.setWindowTitle("my title")
main_window.show()
app.exec()
