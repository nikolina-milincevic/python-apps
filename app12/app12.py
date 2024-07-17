from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
     QLineEdit, QPushButton, QMainWindow, QTableWidget
import sys

from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        
        file_menu_bar = self.menuBar().addMenu("&File")
        help_menu_bar = self.menuBar().addMenu("&Help")
        
        add_student_action = QAction("Add Student", self)
        file_menu_bar.addAction(add_student_action)
        
        about_action = QAction("About", self)
        help_menu_bar.addAction(about_action)
        # help item didn't show so I need to type next line as well
        # otherwise it would be unnecessary
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        
        
        
app = QApplication(sys.argv)
student_management_system = MainWindow()
student_management_system.show()
sys.exit(app.exec())
