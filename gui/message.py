from PyQt5.QtWidgets import QMessageBox
from gui import darkTheme

def show_message(message=''):
    msg = QMessageBox()
    msg.setPalette(darkTheme.dark_palette)
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Query Failed")
    msg.setInformativeText(message)
    msg.setWindowTitle("Error")
    msg.setEscapeButton(QMessageBox.Ok)
    msg.show()
    msg.exec_()

