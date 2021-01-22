class Customer:
    def __init__(self,firstname,surname,username,nationality_number,phone_number,password):
        self.firstname = firstname
        self.surname = surname
        self.nationality_number = nationality_number
        self.phone_number = phone_number
        self.password = password

class HostWebsite:
    def __init__(self,website_address):
        self.website_address = website_address

class TravelAgency:
    def __init__(self,name,address,phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

class TicketCollects:
    def __init__(self,flight_time,destination,source,ticket_id,price,tclass,airline,website_address,travel_agency_name):
        self.flight_time = flight_time
        self.destination = destination
        self.source = source
        self.ticket_id = ticket_id
        self.price = price
        self.tclass = tclass
        self.airline = airline
        self.website_address = website_address
        self.travel_agency_name = travel_agency_name
        
class TransactionBuy:
    def __init__(self,price_transaction_datetime,transaction_id,payment_service_provider,username,ticket_id,website_address):
        self.price_transaction_datetime = price_transaction_datetime
        self.transaction_id = transaction_id
        self.payment_service_provider = payment_service_provider
        self.username = username
        self.ticket_id = ticket_id
        self.website_address = website_address