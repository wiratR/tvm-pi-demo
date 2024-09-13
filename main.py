from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication([])
win = QMainWindow()

win.show()

sys.exit(app.exec_())