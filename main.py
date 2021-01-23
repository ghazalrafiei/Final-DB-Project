import object as ob
import database as db
import yaml

from utils import *
from PyQt5.QtWidgets import *
import sys


if __name__ == '__main__':

    # should they be out of main?!
    

    # print(AirlineTicketSelling_db.get('Customer'))

    print(f'\x1b[0;37;40m' + '\nWindow Openned.')

    app = QApplication(sys.argv)
    screen = Window()
    screen.setFixedWidth(1000)
    screen.setFixedHeight(600)
    screen.show()
    sys.exit(app.exec_())

    # t = ob.TravelAgency('testName201', 'testAddr1120', '23456789087')
    # AirlineTicketSelling_db.insert(t)
    # g = AirlineTicketSelling_db.get('travelagency')
    print('end')
