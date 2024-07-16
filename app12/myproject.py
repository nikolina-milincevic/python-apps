from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout,\
    QLineEdit, QPushButton, QComboBox
import sys
    

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()
        
        # Create widgets:
        distance_label = QLabel("Distance:")
        self.distance_edit = QLineEdit()
        hours_label = QLabel("Time (hours):")
        self.hours_edit = QLineEdit()
        
        self.combobox = QComboBox()
        self.combobox.addItem("Metric (km)")
        self.combobox.addItem("Imperial (miles)")
        
        calculate_button = QPushButton("Calculate speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")
        
        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_edit, 0, 1)
        grid.addWidget(hours_label, 1, 0)
        grid.addWidget(self.hours_edit, 1, 1)
        grid.addWidget(self.combobox, 0, 2)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        
        self.setLayout(grid)
        
    def calculate_speed(self):
        s = int(self.distance_edit.text())
        t = int(self.hours_edit.text())
        speed = s/t
        if self.combobox.currentText() == "Metric (km)":
            tekst = "km/h"
        else:
            tekst = "mph"
        self.output_label.setText(f"Average speed is {speed} {tekst}.")
        
        
        
app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())