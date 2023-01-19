from datetime import datetime
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer
from ui_clock import Ui_MainWindow
import time

class Clock(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        time = datetime.now()
        self.hours = time.strftime("%H")
        self.minutes = time.strftime("%M")
        self.display_time()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(60000)
    
    def update_time(self):
        hours = time.strftime("%H")
        minutes = time.strftime("%M")
        self.hours = hours
        self.minutes = minutes
        self.display_time()
    
    def display_time(self):
        self.hours_label.setText(self.hours)
        self.minutes_label.setText(self.minutes)
