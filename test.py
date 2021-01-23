import database as db
import object as ob
import time
from utils import *
import yaml

ts_settings = config(file='config.yml')
ts_settings.import_settings()

test_db = db.DataBase(
    ts_settings.database_name,
    ts_settings.user,
    ts_settings.password,
    ts_settings.host,
    ts_settings.port,
    ts_settings.schemas)
test_db.connect()

print('____________________________INSERT_______________________________')
test_db.insert(ob.Customer('test1', 'test1', 'test1', 22, 22, ''))
test_db.insert(ob.Customer('test1', 'test1', 'test1', 22, 23, 'pass'))  # Error
test_db.insert(ob.Customer('test1', 'test2', 'test2', 24, 25, 'pass'))  # Error
test_db.insert(ob.TravelAgency('test1', 'street1', '0912'))
test_db.insert(ob.TravelAgency('test1', 'street2', '0914'))  # Error

test_db.insert(
    ob.TicketCollects(
        time.time(),
        'des1',
        's1',
        'E415',
        '22000',
        'F',
        'Mahan',
        'www.sample.com',
        'airline1'))
test_db.insert(
    ob.TicketCollects(
        time.time(),
        'des2',
        's1',
        'E415',
        '22000',
        'F',
        'Mahan',
        'www.sample.com',
        'airline1'))  # Error
print('____________________________DELETE_______________________________')

# ob.Customer()
test_db.delete('Customer', 'username', 'test1')
test_db.delete('Customer', 'username', 'test10')  # Error
print('_______________________________GET____________________________')

print(test_db.get('TicketCollects'))
print(test_db.get('TransactionBuy'))
print('_______________________________INSERT____________________________')

test_db.insert(ob.HostWebsite('www.web1.com'))
test_db.insert(ob.HostWebsite('www.web2.com'))
test_db.insert(ob.HostWebsite('www.web3.com'))
test_db.insert(ob.HostWebsite('www.web1.com'))  # Error
print('__________________________________UPDATE_________________________')

test_db.update(
    'Hostwebsite',
    'website_address',
    'www.NewWeb.com',
    'website_address',
    'www.web1.com')
test_db.update(
    'Hostwebsie',
    'website_address',
    'www.NewWeb.com',
    'website_address',
    'www.web1.com')  # Error
test_db.update(
    'Hostwebsite',
    'website_address',
    'www.NewWeb.com',
    'website_address',
    'www.web8.com')  # Error


print('______________________________GET_____________________________')

print(test_db.get('hostwebsite'))

print('_____________________________DONE______________________________')

print(f'{bcolors.OKGREEN}Testing Done')
