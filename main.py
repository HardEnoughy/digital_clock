from PySide6.QtWidgets import QApplication
from clock import Clock

app = QApplication()
window = Clock()
window.show()
app.exec()
