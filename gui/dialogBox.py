from utils import str_to_class, quote, config
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import *

import json
from gui import darkTheme, mainWindow, messageBox
import database as dbs


class Dialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

    def add_fields(
            self,
            fields,
            title='',
            query_type='',
            tab_name='',
            database=dbs.DataBase(),
            mainwindow=''):

        self.query_type = query_type
        self.tab_name = tab_name
        self.fields = fields
        self.title = title
        self.message = ''
        self.failed = False
        self.db = database
        self.mainwindow = mainwindow

        self.update_to = ''

        self.optional = ''

        self.setWindowTitle(title)
        self.setPalette(darkTheme.dark_palette)
        self.dlgLayout = QVBoxLayout()

        self.formLayout = QFormLayout()
        self.text_boxes = []

        # Creating Dialog Box Elements
        if query_type == 'O':
            self.dlgLayout.addWidget(QLabel('Write any query you want!'))

            qle = QTextEdit()
            qle.setFixedSize(300, 200)            
            self.optional = qle
            self.formLayout.addRow(qle)

        elif query_type == 'U':

            self.dlgLayout.addWidget(QLabel('Be updated to?'))
            qle = QLineEdit()
            qle.setAlignment(Qt.AlignCenter)

            self.update_to = qle
            self.formLayout.addRow(qle)

        elif query_type == 'I':
            for f in fields:

                qle = QLineEdit()
                if f == 'password':
                    qle.setEchoMode(QLineEdit.Password)
                self.text_boxes.append(qle)
                self.formLayout.addRow(f.replace('_', ' ').title(), qle)
        
        elif query_type == 'D':
            self.dlgLayout.addWidget(
                    QLabel('Are you sure?'))

        self.dlgLayout.addLayout(self.formLayout)

        self.okay_button = QPushButton('Okay')
        self.cancel_button = QPushButton('Cancel')

        self.okay_button.clicked.connect(self.ok_get)
        self.cancel_button.clicked.connect(self.cancel_get)

        # Add Action
        self.dlgLayout.addWidget(self.okay_button)
        self.dlgLayout.addWidget(self.cancel_button)

        self.setLayout(self.dlgLayout)
        return self

    def cancel_get(self):
        self.close()
        self.mainwindow.CreateTabs(self.db)
        
    def ok_get(self):
        inputs = {}
        for i in range(len(self.text_boxes)):
            if self.text_boxes[i].text() != '':
                inputs[self.fields[i]] = self.text_boxes[i].text()
            else:
                inputs[self.fields[i]] = 'NULL_VALUE'
            self.text_boxes[i].clear()

        json_string = json.dumps(inputs)
        obj_json = json.loads(json_string)
        obj = str_to_class(self.tab_name)(**obj_json)

        if self.query_type == 'D':  

            self.failed = False

            current_column = ''
            current_value = ''
            try:
                for t in self.mainwindow.tables:
                    if t.objectName() == self.tab_name:
                        current_column = self.db.schemas[self.tab_name]['columns'][t.currentColumn()]
                        break
            except:
                pass
            self.message = self.db.delete(self.tab_name, current_column,current_value)

            if self.message is not None:
                self.failed = True

        elif self.query_type == 'I':

            self.failed = False
            self.message = self.db.insert(obj)
            if self.message is not None:
                self.failed = True
            pass
        elif self.query_type == 'U':  # WRITE THE QUERY
            self.failed = False


            u_column = ''
            current_value = ''
            for t in self.mainwindow.tables:
                if t.objectName() == self.tab_name:
                    current_value = t.selectedItems()[0].text()
                    u_column = self.db.schemas[self.tab_name]['columns'][t.currentColumn()]
                    break

            self.message = self.db.update(
                self.tab_name,
                u_column,
                self.update_to.text(),
                current_value)

            if self.message is not None:
                self.failed = True

        elif self.query_type == 'O':
            self.failed = False
            err , self.message = self.db.exectue_query(self.optional.toPlainText())
            if err == 1:
                self.failed = True
            pass

        self.close()
        self.mainwindow.CreateTabs(self.db)
        if self.query_type == 'O' and self.failed != True:
            messageBox.show_message(self.message, err = False)
        if self.failed:
            messageBox.show_message(self.message)