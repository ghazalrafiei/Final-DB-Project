import sys
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
print(AirlineTicketSelling_db)


def show_message(message=''):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Query Failed")
    msg.setInformativeText(message)
    msg.setWindowTitle("Error")
    msg.setEscapeButton(QMessageBox.Ok)
    msg.show()
    msg.exec_()


class Dialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

    def add_fields(self, fields, title='', query_type='', tab_name=''):

        self.query_type = query_type
        self.tab_name = tab_name
        self.fields = fields
        self.title = title
        self.message = ''
        self.failed = False

        self.setWindowTitle(title)
        self.dlgLayout = QVBoxLayout()

        if query_type == 'D':
            self.dlgLayout.addWidget(
                QLabel('By any column(only one)\nIf many, deletes by the first non-empty value.'))

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
            if query_type == 'O':
                qle.setFixedSize(300, 200)
                qle.setAlignment(Qt.AlignCenter)
            if f == 'password':
                qle.setEchoMode(QLineEdit.PasswordEchoOnEdit)
            self.text_boxes.append(qle)
            self.formLayout.addRow(f.replace('_', ' ').title(), qle)

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
        inputs = {}
        for i in range(len(self.text_boxes)):
            inputs[self.fields[i]] = self.text_boxes[i].text()
            self.text_boxes[i].clear()

        json_string = json.dumps(inputs)
        obj_json = json.loads(json_string)
        obj = str_to_class(self.tab_name)(**obj_json)

        if self.query_type == 'D':  # Deletes by the first non-empty value
            for k in inputs.keys():
                v = inputs[k]
                if v != '':
                    self.message = AirlineTicketSelling_db.delete(
                        table=self.tab_name, column=k, key=v)  # inja
                    if self.message != None:
                        self.failed = True
                    # print('message')
                    # show_message(message)
                    break

        elif self.query_type == 'I':

            self.failed = False
            result = AirlineTicketSelling_db.insert(obj)
            if self.message != None:
                self.failed = True
            pass

        elif self.query_type == 'U':
            self.failed = False
            self.message = AirlineTicketSelling_db.update(obj)  # inja
            if self.message != None:
                self.failed = True
            pass

        elif self.query_type == 'O':
            self.failed = False
            self.message = AirlineTicketSelling_db.exectue_query(inputs[0])
            if self.message != None:
                self.failed = True
            pass

        self.close()
        refresh()
        # window.update()

    def closeEvent(self, event):
        event.accept()
        if self.failed:
            show_message(self.message)
        # refresh()


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Airline Ticket Booking Database')
window.setFixedWidth(1250)
window.setFixedHeight(600)

layout = QGridLayout()
tabs = QTabWidget()
insert_dialogs = []
delete_dialogs = []
update_dialogs = []
opt_dialogs = []


def refresh(first=False):
    layout = QGridLayout()
    window.setLayout(layout)
    tabs = QTabWidget()
    for t in settings.schemas.keys():
        current_tab = QWidget()

        rows = AirlineTicketSelling_db.get(t)
        cols = AirlineTicketSelling_db.schemas[t]['columns']

        tabs.addTab(current_tab, t)
        current_tab.layout = QVBoxLayout()

        table_view = QTableWidget()
        table_view.setFixedSize(1200, 400)
        table_view.setRowCount(len(rows))
        table_view.setColumnCount(len(cols))
        table_view.horizontalHeader().setStretchLastSection(True)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Set Columns Names:
        table_view.setHorizontalHeaderLabels(
            [c.replace('_', ' ').title() for c in cols])

        # Set Items
        for r in range(len(rows)):
            for c in range(len(cols)):
                value = str(rows[r][c])
                if cols[c] == 'password':
                    value = '*' * 10
                content = QTableWidgetItem(value)

                content.setFlags(content.flags() ^ Qt.ItemIsEditable)
                table_view.setItem(r, c, content)

        table_view.resizeRowsToContents()
        table_view.resizeColumnsToContents()

        current_tab.layout.addWidget(table_view)

        insert_dialog = Dialog()
        insert_dialog.add_fields(
            cols,
            query_type='I',
            tab_name=t,
            title='Insert')
        insert_button = QPushButton('Insert')
        insert_button.clicked.connect(insert_dialog.show)
        insert_dialogs.append(insert_dialog)

        delete_dialog = Dialog()
        delete_dialog.add_fields(
            cols,
            query_type='D',
            tab_name=t,
            title='Delete')
        delete_button = QPushButton('Delete')
        delete_button.clicked.connect(delete_dialog.show)
        delete_dialogs.append(delete_dialog)

        update_dialog = Dialog()
        update_dialog.add_fields(
            cols,
            query_type='U',
            tab_name=t,
            title='Update')
        update_button = QPushButton('Update')
        update_button.clicked.connect(update_dialog.show)
        update_dialogs.append(update_dialog)

        opt_dialog = Dialog()
        opt_dialog.add_fields(
            [''],
            query_type='O',
            tab_name=t,
            title='Optional SQL ')
        optional_button = QPushButton('Optional SQL Query')
        optional_button.clicked.connect(opt_dialog.show)
        opt_dialogs.append(opt_dialog)

        current_tab.layout.addWidget(insert_button)
        current_tab.layout.addWidget(delete_button)
        current_tab.layout.addWidget(update_button)
        current_tab.layout.addWidget(optional_button)

        current_tab.setLayout(current_tab.layout)

    layout.addWidget(tabs, 0, 0)
    if first:
        window.setLayout(layout)
    else:
        window.update()


refresh(first=True)
window.show()
sys.exit(app.exec_())
