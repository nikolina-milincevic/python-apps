from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, \
    QDialog, QVBoxLayout
import sys
import mysql.connector
import os
from PyQt6.QtGui import QAction


SQL_USER = os.getenv("sql_user")
SQL_PASSWORD = os.getenv("sql_password")

# first I made a table in my database called "my_db"
# and I added some values with the following:
# INSERT INTO my_db.students VALUES 
# (1, "John Smith", "Math", "49111222333"),
# (2, "Asha Patel", "Astronomy", "49222333444"),
# (3, "Lokesh Rana", "Biology", "49333444555"),
# (4, "Andy Johnson", "Physics", "4811001100"),
# (5, "Kasia Popescu", "Astronomy", "42001001111"),
# (6, "Paula Zephyr", "Astronomy", "4901011100");


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        
        file_menu_bar = self.menuBar().addMenu("&File")
        help_menu_bar = self.menuBar().addMenu("&Help")
        
        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_bar.addAction(add_student_action)
        
        about_action = QAction("About", self)
        help_menu_bar.addAction(about_action)
        # help item didn't show so I need to type next line as well
        # otherwise it would be unnecessary
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
    
    def load_data(self):
        cnx = mysql.connector.connect(user=SQL_USER, password=SQL_PASSWORD,
                              host="localhost", database="my_db")
        cursor = cnx.cursor(buffered=True)
        my_query = '''SELECT * FROM students;'''
        cursor.execute(my_query)
        rows = cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row in enumerate(rows):
            self.table.insertRow(row_number)
            for column_number, cell in enumerate(row):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(cell)))
        cnx.commit()
        cursor.close()
        cnx.close()
        
    def insert(self):
        dialog = InsertDialog()
        dialog.exec()
        
    
class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        
        layout = QVBoxLayout()
        
        student_name = QLineEdit()
        student_name.setPlaceholderText("Name")
        layout.addWidget(student_name)
        
        self.setLayout(layout)
                
                
        
        
app = QApplication(sys.argv)
student_management_system = MainWindow()
student_management_system.show()
student_management_system.load_data()
sys.exit(app.exec())
