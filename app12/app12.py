from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, \
    QDialog, QVBoxLayout, QComboBox, QToolBar, QStatusBar, QMessageBox
import sys
import mysql.connector
import os
from PyQt6.QtGui import QAction, QIcon


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
        self.setMinimumSize(800, 600)
        
        file_menu_bar = self.menuBar().addMenu("&File")
        help_menu_bar = self.menuBar().addMenu("&Help")
        edit_menu_bar = self.menuBar().addMenu("&Edit")
        
        add_student_action = QAction(QIcon("app12/icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_bar.addAction(add_student_action)
        
        about_action = QAction("About", self)
        help_menu_bar.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        about_action.triggered.connect(self.about)
        
        search_action = QAction(QIcon("app12/icons/search.png"), "Search", self)
        edit_menu_bar.addAction(search_action)
        search_action.triggered.connect(self.search)
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
        
        # Create toolbar and toolbar elements
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)
        
        # Create status bar and its elements
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        
        # Detect a cell click
        self.table.cellClicked.connect(self.cell_clicked)
    
    def cell_clicked(self):
        edit_button = QPushButton("Edit Records")
        edit_button.clicked.connect(self.edit)
        delete_button = QPushButton("Delete Records")
        delete_button.clicked.connect(self.delete)
        
        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)
        
        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)
        
    
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
        
    def search(self):
        dialog = SearchDialog()
        dialog.exec()
        
    def edit(self):
        dialog = EditDialog()
        dialog.exec()
        
    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()
        
    def about(self):
        dialog = AboutDialog()
        dialog.exec()
        
    
class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """
        This app was created during the course "The Python Mega Course".
        Feel free to modify and reuse the app.
        """
        self.setText(content)
    
    

class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        
        layout = QVBoxLayout()
        
        # Get student data from selected row
        index = student_management_system.table.currentRow()
        student_name = student_management_system.table.item(index, 1).text()
        course_name = student_management_system.table.item(index, 2).text()
        mobile = student_management_system.table.item(index, 3).text()
        self.student_id = student_management_system.table.item(index, 0).text()
        
        # Add student name widget
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)
        
        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)
        
        # Add mobile widget
        self.mobile = QLineEdit(mobile)
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)
        
        # Add a submit button
        button = QPushButton("Update")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)
        
        self.setLayout(layout)
    
    def update_student(self):
        cnx = mysql.connector.connect(user=SQL_USER, password=SQL_PASSWORD,
                              host="localhost", database="my_db")
        cursor = cnx.cursor(buffered=True)
        my_query = '''UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s;'''
        cursor.execute(my_query, 
                       (self.student_name.text(), 
                        self.course_name.itemText(self.course_name.currentIndex()), 
                        self.mobile.text(), 
                        self.student_id))
        cnx.commit()
        cursor.close()
        cnx.close()
        
        # Refresh the table
        student_management_system.load_data()
        
        
class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")
        
        layout = QGridLayout()
        confirmation = QLabel("Are you sure you want to delete?")
        yes = QPushButton("Yes")
        no = QPushButton("No")
        
        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        
        self.setLayout(layout)
        
        yes.clicked.connect(self.delete_student)
        no.clicked.connect(self.close)
        
    def delete_student(self):
        # Get selected row index and student id 
        index = student_management_system.table.currentRow()
        student_id = student_management_system.table.item(index, 0).text()
        cnx = mysql.connector.connect(user=SQL_USER, password=SQL_PASSWORD,
                              host="localhost", database="my_db")
        cursor = cnx.cursor(buffered=True)
        my_query = '''DELETE FROM students WHERE id = %s;'''
        cursor.execute(my_query, (student_id, ))
        cnx.commit()
        cursor.close()
        cnx.close()
        
        # Refresh the table
        student_management_system.load_data()
        
        self.close()
        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Success")
        confirmation_widget.setText("The record was deleted succesfully!")
        confirmation_widget.exec()
        

    
class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        
        layout = QVBoxLayout()
        
        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)
        
        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)
        
        # Add mobile widget
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)
        
        # Add a submit button
        button = QPushButton("Submit")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)
        
        self.setLayout(layout)
    
    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        print(name, course, mobile)
        cnx = mysql.connector.connect(user=SQL_USER, password=SQL_PASSWORD,
                              host="localhost", database="my_db")
        cursor = cnx.cursor(buffered=True)
        my_query = '''INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s);'''
        cursor.execute(my_query, (name, course, mobile))
        cnx.commit()
        cursor.close()
        cnx.close()
        student_management_system.load_data()
        
        
class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Students")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        
        layout = QVBoxLayout()
        
        # Add search widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)
        
        # Add a search button
        button = QPushButton("Search")
        button.clicked.connect(self.search)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
    def search(self):
        name = self.student_name.text()
        cnx = mysql.connector.connect(user=SQL_USER, password=SQL_PASSWORD,
                              host="localhost", database="my_db")
        cursor = cnx.cursor(buffered=True)
        my_query = '''SELECT * FROM students WHERE name = %s;'''
        cursor.execute(my_query, (name,))
        rows = cursor.fetchall()
        print(rows)
        items = student_management_system.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            student_management_system.table.item(item.row(), 1).setSelected(True)
        cnx.commit()
        cursor.close()
        cnx.close()
                
                
        
        
app = QApplication(sys.argv)
student_management_system = MainWindow()
student_management_system.show()
student_management_system.load_data()
sys.exit(app.exec())
