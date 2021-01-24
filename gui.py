import sys
import object as ob
import database as db
import yaml
import json
import object.object as ob

from utils import str_to_class, quote, config
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

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


class Dialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

    def add_fields(self, fields, title='', query_type='', tab_name=''):

        self.query_type = query_type
        self.tab_name = tab_name
        self.fields = fields
        self.title = title

        self.setWindowTitle(title)
        self.dlgLayout = QVBoxLayout()

        if query_type == 'D':
            self.dlgLayout.addWidget(QLabel('By any column(only one)'))
        # elif query == 'I':

        #     pass
        # elif query == 'U':

        #     pass
        elif query_type == 'O':
            self.dlgLayout.addWidget(QLabel('Write any query you want!'))

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

        json_string = '{ '
        for i in range(len(inputs)):
            json_string += quote(settings.schemas[t]['columns'][i],
                                 char='\"') + ' : ' + quote(inputs[i], char='\"') + ' , '
        json_string = json_string[:len(json_string) - 2]
        json_string += ' }'

        print(json_string)
        obj_json = json.loads(json_string)
        obj = str_to_class(t)(**obj_json)

        if self.query_type == 'D':
            AirlineTicketSelling_db.delete(obj)
            pass

        elif self.query_type == 'I':
            AirlineTicketSelling_db.insert(obj)
            pass

        elif self.query_type == 'U':
            AirlineTicketSelling_db.update(obj)
            pass

        elif self.query_type == 'O':
            AirlineTicketSelling_db.exectue_query(inputs[0])
            pass

        self.close()


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Airline Ticket Booking Database')
window.setFixedWidth(1200)
window.setFixedHeight(800)

layout = QGridLayout()
tabs = QTabWidget()


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
    table_view.setHorizontalHeaderLabels(cols)

    # Set Items
    for r in range(len(rows)):
        for c in range(len(cols)):
            value = str(rows[r][c])
            if cols[c] == 'password':
                value = '*' * 10
            content = QTableWidgetItem(value)

            content.setFlags(content.flags() ^ Qt.ItemIsEditable)
            table_view.setItem(r, c, content)

    current_tab.layout.addWidget(table_view)

    insert_dialog = Dialog()
    insert_dialog.add_fields(cols, 'I', t)
    insert_button = QPushButton('Insert')
    insert_button.clicked.connect(insert_dialog.show)

    delete_dialog = Dialog()
    delete_dialog.add_fields(cols, 'D', t)
    delete_button = QPushButton('Delete')
    delete_button.clicked.connect(delete_dialog.show)

    update_dialog = Dialog()
    update_dialog.add_fields(cols, 'U', t)
    update_button = QPushButton('Update')
    update_button.clicked.connect(update_dialog.show)

    opt_dialog = Dialog()
    opt_dialog.add_fields([''], 'O', t)
    optional_button = QPushButton('Optional SQL Query')
    optional_button.clicked.connect(opt_dialog.show)

    current_tab.layout.addWidget(insert_button)
    current_tab.layout.addWidget(delete_button)
    current_tab.layout.addWidget(update_button)
    current_tab.layout.addWidget(optional_button)

    current_tab.setLayout(current_tab.layout)


layout.addWidget(tabs, 0, 0)


window.setLayout(layout)
window.show()
sys.exit(app.exec_())
