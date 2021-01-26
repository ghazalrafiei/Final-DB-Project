# from utils import str_to_class, quote, config
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import *
import json
import gui.darkTheme
import gui
import sys


def quote(string, char='\''):
    return char + str(string) + char


def str_to_class(s):
    return getattr(sys.modules['object.object'], s)


class Dialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

    def add_fields(self, fields, title='', query_type='', tab_name='' ):

        self.query_type = query_type
        self.tab_name = tab_name
        self.fields = fields
        self.title = title
        self.message = ''
        self.failed = False

        self.setWindowTitle(title)
        self.setPalette(gui.darkTheme.dark_palette)
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
                    self.message = gui.AirlineTicketSelling_db.delete(
                        table=self.tab_name, column=k, key=v)  # inja
                    if self.message is not None:
                        self.failed = True
                    # print('message')
                    # show_message(message)
                    break

        elif self.query_type == 'I':

            self.failed = False
            result = gui.AirlineTicketSelling_db.insert(obj)
            if self.message is not None:
                self.failed = True
            pass

        elif self.query_type == 'U':
            self.failed = False
            self.message = gui.AirlineTicketSelling_db.update(obj)  # inja
            if self.message is not None:
                self.failed = True
            pass

        elif self.query_type == 'O':
            self.failed = False
            self.message = gui.AirlineTicketSelling_db.exectue_query(inputs[0])
            if self.message is not None:
                self.failed = True
            pass

        self.close()
        if self.failed:
            gui.show_message(self.message)
        # refresh()
        # window.update()

    def closeEvent(self, event):
        event.accept()

  