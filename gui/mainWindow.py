import sys
import yaml
import json
import gui.dialogBox
import gui.darkTheme
import database as db

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import *


class GUI(QWidget):
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Airline Ticket Booking Database')
        self.setFixedWidth(1250)
        self.setFixedHeight(700)
        self.setPalette(gui.darkTheme.dark_palette)
        self.counter = 0

    def CreateTabs(self, database=db.DataBase()):

        tab_index = 0

        if self.counter != 0:
            tab_index = self.tabs.currentIndex()

        self.counter += 1

        if self.layout():
            QWidget().setLayout(self.layout())

        self.tabs = QTabWidget()
        self.laylay = QGridLayout()

        self.database = database
        self.insert_dialogs = []
        self.delete_dialogs = []
        self.update_dialogs = []
        self.opt_dialogs = []
        self.tabs_array = []
        self.tables = []

        for t in self.database.schemas.keys():
            current_tab = QWidget()

            rows = database.get(t)
            cols = database.schemas[t]['columns']

            self.tabs.addTab(current_tab, t)
            current_tab.layout = QVBoxLayout()

            table_view = QTableWidget()

            table_view.setFixedSize(1200, 500)
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
                    if cols[c] == 'password' and value != '':
                        value = '*' * 10
                    content = QTableWidgetItem(value)

                    content.setFlags(content.flags() ^ Qt.ItemIsEditable)
                    table_view.setItem(r, c, content)

            table_view.resizeRowsToContents()
            table_view.resizeColumnsToContents()
        
            self.tables.append(table_view)
            current_tab.layout.addWidget(table_view)

            insert_dialog = gui.dialogBox.Dialog()
            insert_dialog.add_fields(
                cols,
                query_type='I',
                tab_name=t,
                title='Insert',
                mainwindow=self,
                database=self.database)
            insert_button = QPushButton('Insert')
            insert_button.clicked.connect(insert_dialog.show)
            self.insert_dialogs.append(insert_dialog)

            delete_dialog = gui.dialogBox.Dialog()
            delete_dialog.add_fields(
                cols,
                query_type='D',
                tab_name=t,
                title='Delete',
                mainwindow=self,
                database=self.database)
            delete_button = QPushButton('Delete')
            delete_button.clicked.connect(delete_dialog.show)
            self.delete_dialogs.append(delete_dialog)

            update_dialog = gui.dialogBox.Dialog()
            update_dialog.add_fields(
                cols,
                query_type='U',
                tab_name=t,
                title='Update',
                mainwindow=self,
                database=self.database)
            update_button = QPushButton('Update')
            update_button.clicked.connect(update_dialog.show)
            self.update_dialogs.append(update_dialog)

            opt_dialog = gui.dialogBox.Dialog()
            opt_dialog.add_fields(
                [''],
                query_type='O',
                tab_name=t,
                title='Optional SQL',
                mainwindow=self,
                database=self.database)
            optional_button = QPushButton('Optional SQL Query')
            optional_button.clicked.connect(opt_dialog.show)
            self.opt_dialogs.append(opt_dialog)

            current_tab.layout.addWidget(insert_button)
            current_tab.layout.addWidget(delete_button)
            current_tab.layout.addWidget(update_button)
            current_tab.layout.addWidget(optional_button)
            current_tab.setLayout(current_tab.layout)
            self.tabs_array.append(current_tab)

        self.tabs.setCurrentIndex(tab_index)

        self.laylay.addWidget(self.tabs)
        self.setLayout(self.laylay)
