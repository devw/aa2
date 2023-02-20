from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt6.QtGui import QPalette, QColor


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        for x in range(10):
            for y in range(10):
                if (x + y) % 2 == 0:
                    layout.addWidget(Color('white'), x, y)
                else:
                    layout.addWidget(Color('black'), x, y)

        layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()


# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt6.QtCore import QCoreApplication


# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Button title")
#         self.button = QPushButton('Click me!')
#         self.button.clicked.connect(self.onClick)
#         self.setCentralWidget(self.button)

#     def onClick(self):
#         print("clic!")


# app = QCoreApplication.instance()
# if app is None:
#     app = QApplication([])
# window = Window()
# window.show()
# app.exec()


# #### color

# # import sys
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
# # from PyQt5.QtGui import QColor, QPalette
# # from PyQt5.QtCore import QCoreApplication
# # class Color(QWidget):
# #   def __init__(self, color):
# #     super().__init__()
# #     self.setAutoFillBackground(True)
# #     self.myPalette = self.palette()
# #     self.myPalette.setColor(QPalette.Window, QColor(color))
# #     self.setPalette(self.myPalette)

# # class Window(QMainWindow):
# #   def __init__(self):
# #     super().__init__()
# #     self.setWindowTitle("Vertical Box Layouts")
# #     self.layout = QVBoxLayout()
# #     self.layout.addWidget(Color('red'))
# #     self.layout.addWidget(Color('blue'))
# #     self.widget = QWidget()
# #     self.widget.setLayout(self.layout)
# #     self.setCentralWidget(self.widget)

# # app = QCoreApplication.instance()
# # if app is None:
# #   app = QApplication(sys.argv)
# # window = Window()
# # window.show()
# # app.exec_()

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
# from PyQt5.QtGui import QColor, QPalette
# from PyQt5.QtCore import QCoreApplication

# class Color(QWidget):
#   def __init__(self, color):
#     super().__init__()
#     self.setAutoFillBackground(True)
#     self.myPalette = self.palette()
#     self.myPalette.setColor(QPalette.Window, QColor(color))
#     self.setPalette(self.myPalette)

# class Window(QMainWindow):
#   def __init__(self):
#     super().__init__()
#     self.setWindowTitle("Les Grid Layout")
#     self.layout = QGridLayout()
#     self.layout.addWidget(Color('red'),0,0)
#     self.layout.addWidget(Color('green'),1,0)
#     self.layout.addWidget(Color('blue'),1,1)
#     self.layout.addWidget(Color('purple'),2,1)
#     self.widget = QWidget()
#     self.widget.setLayout(self.layout)
#     self.setCentralWidget(self.widget)

# app = QCoreApplication.instance()
# if app is None:
#   app = QApplication(sys.argv)
# window = Window(QMainWindow()
# window.show()
# app.exec_()
