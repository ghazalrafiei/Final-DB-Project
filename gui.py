import sys
# from tables import *
import database as db
import yaml

from utils import *
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication,QHeaderView QDialog, QLabel, QWidget, QTabWidget, QGridLayout, QHBoxLayout, QPushButton, QDialogButtonBox, QLineEdit, QVBoxLayout, QFormLayout, QToolBar, QStatusBar
# from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *


class Dialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

    def add_fields(self, fields, title='خر'):

        self.fields = fields
        self.setWindowTitle('title')
        self.dlgLayout = QVBoxLayout()
        self.formLayout = QFormLayout()
        self.text_boxes = []
        for f in fields:
            qle = QLineEdit()
            self.text_boxes.append(qle)
            self.formLayout.addRow(f, qle)

        self.dlgLayout.addLayout(self.formLayout)
        self.okay_button = QPushButton('Okay')
        self.cancel_button = QPushButton('Cancel')
        self.okay_button.clicked.connect(self.ok_get)
        self.cancel_button.clicked.connect(self.close)

        # Add Action
        self.dlgLayout.addWidget(self.okay_button)
        self.dlgLayout.addWidget(self.cancel_button)

        self.setLayout(self.dlgLayout)
        return self

    def ok_get(self):
        inputs = []
        for i in self.text_boxes:
            inputs.append(i.text())
            i.clear()
            print(inputs)
            # Call database functions
            # reload home
        self.close()


# MAIN:
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


def print_zert():
    print('zer')


for t in settings.schemas.keys():

    rows = AirlineTicketSelling_db.get(t)
    cols = AirlineTicketSelling_db.schemas[t]['columns']
    current_tab = QWidget()

    tabs.addTab(current_tab, t)
    current_tab.layout = QVBoxLayout()

    table_view = QTableWidget()
    table_view.setFixedSize(1150, 600)
    table_view.setRowCount(len(rows))
    table_view.setColumnCount(len(cols))
    table_view.horizontalHeader().setStretchLastSection(True)
    table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    # Set Columns Names:
    for c in range(len(cols)):
        table_view.setItem(0, c, QTableWidgetItem(cols[c]))
    table_view.setHorizontalHeaderLabels(cols)

    # Set Items
    for r in range(len(rows)):
        for c in range(len(cols)):

            content = QTableWidgetItem(str(rows[r][c]))
            content.setFlags(content.flags() ^ Qt.ItemIsEditable)
            table_view.setItem(r, c, content)

    current_tab.layout.addWidget(table_view)

    a = Dialog()
    a.add_fields(['a'])

    insert_button = QPushButton('Insert')
    insert_button.clicked.connect(a.show)
    delete_button = QPushButton('Delete')
    delete_button.clicked.connect(a.show)
    update_button = QPushButton('Update')
    update_button.clicked.connect(a.show)
    optional_button = QPushButton('Optional SQL Query')
    optional_button.clicked.connect(a.show)

    current_tab.layout.addWidget(insert_button)
    current_tab.layout.addWidget(delete_button)
    current_tab.layout.addWidget(update_button)
    current_tab.layout.addWidget(optional_button)

    current_tab.setLayout(current_tab.layout)


layout.addWidget(tabs, 0, 0)


window.setLayout(layout)
window.show()
sys.exit(app.exec_())
