import sys
# from tables import *
import database as db
import yaml

from utils import *
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QWidget, QTabWidget, QGridLayout, QHBoxLayout, QPushButton, QDialogButtonBox, QLineEdit, QVBoxLayout, QFormLayout, QToolBar, QStatusBar
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Dialog(QDialog):
    """Dialog."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        # for i in columns!
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Job:', QLineEdit())
        formLayout.addRow('Hobbies:', QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)


# QlineEdit for text box
settings = config(file='config.yml')
settings.import_settings()

AirlineTicketSelling_db = db.DataBase(
    settings.database_name,
    settings.user,
    settings.password,
    settings.host,
    settings.port,
    settings.schemas)
AirlineTicketSelling_db.connect()

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Airline Ticket Booking Database')
window.setFixedWidth(1200)
window.setFixedHeight(800)

layout = QGridLayout()
tabs = QTabWidget()

for t in settings.schemas.keys():

    table = AirlineTicketSelling_db.get(t)
    print(table)
    rows = table
    cols = AirlineTicketSelling_db.schemas[t]['columns']
    current_tab = QWidget()

    tabs.addTab(current_tab, t)
    current_tab.layout = QVBoxLayout()

    table_view = QTableWidget()
    table_view.setFixedSize(400,400)
    table_view.setRowCount(len(rows))
    table_view.setColumnCount(len(cols))
    #Set Columns Names:
    for c in range(len(cols)):
        table_view.setItem(0,c , QTableWidgetItem(cols[c]))
    #Set Items
    for r in range(len(rows)):
        for c in range(len(cols)):
            table_view.setItem(r+1, c , QTableWidgetItem(str(table[r][c-1])))
    

    current_tab.layout.addWidget(table_view)
    current_tab.layout.addWidget(QPushButton('Insert'))
    current_tab.layout.addWidget(QPushButton('Update'))
    current_tab.layout.addWidget(QPushButton('Delete'))
    current_tab.layout.addWidget(QPushButton('Optional SQL Query'))

    current_tab.setLayout(current_tab.layout)


layout.addWidget(tabs, 0, 0)


window.setLayout(layout)
window.show()
sys.exit(app.exec_())


# class Window(QWidget):

#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         label1 = QLabel("Widget in Tab 1.")
#         tabwidget = QTabWidget()
#         for t in AirlineTicketSelling_db.schemas.keys():
#             label = QLabel(f'label_{t}')
#             tabwidget.addTab(label, t)

#         layout.addWidget(tabwidget, 0, 0)
# app = QApplication(sys.argv)
# screen = Window()
# screen.setFixedWidth(1000)
# screen.setFixedHeight(600)
# screen.show()
# sys.exit(app.exec_())
# if __name__ == '__main__':
#     pass
