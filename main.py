import gui.mainWindow as window
import sys
import utils
import database as db

from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':

    settings = utils.config(file='config.yml')
    settings.import_settings()

    AirlineTicketBooking_db = db.DataBase(
        settings.database_name,
        settings.user,
        settings.password,
        settings.host,
        settings.port,
        settings.schemas)
    AirlineTicketBooking_db.connect()

    app = QApplication(sys.argv)
    graphic = window.GUI()
    graphic.CreateTabs(AirlineTicketBooking_db)
    graphic.show()
    sys.exit(app.exec_())

    
    print('end')
