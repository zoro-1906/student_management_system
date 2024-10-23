import sys
from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout,
                             QLineEdit, QPushButton, QMainWindow)
from PyQt6.QtGui import QAction
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About" ,self)
        help_menu_item.addAction(about_action)

# Initialize the QApplication and the main widget
app = QApplication(sys.argv)
age_calculator = MainWindow()
age_calculator.show()

sys.exit(app.exec())
