import object as ob
import database as db
# import psycopg2 as psg


if __name__ == '__main__':

    database_name = 'TicketBooking'
    user = 'postgres'
    password = 'Iran1234'
    host = 'localhost'
    port = 5432

    AirlineTicketSelling_db = db.DataBase(database_name, user , password, host, port)
    AirlineTicketSelling_db.connect()
    t = ob.TravelAgency('testName1','testAddr1','0912')

    AirlineTicketSelling_db.insert(t)

    
