drop table customer, hostwebsite, travelagency, ticketcollects, transactionbuy cascade;

CREATE TABLE Customer ( 
	firstname 			VARCHAR(30),
 	surname 			VARCHAR(30), 
 	username 			VARCHAR(30) NOT NULL, 
	nationality_number              BIGINT, 
	phone_number 		        BIGINT, 
	password 			VARCHAR(30), 
	 
	PRIMARY KEY(username), 
	UNIQUE(nationality_number,phone_number) 
);

CREATE TABLE HostWebsite (
	website_address VARCHAR(100) NOT NULL,
	PRIMARY KEY(website_address) 
);

CREATE TABLE TravelAgency ( 
	name 		 VARCHAR(30) NOT NULL, 
	address 	 VARCHAR(200), 
	phone_number     BIGINT, 
	
	PRIMARY KEY(name), 
	UNIQUE(phone_number)
);

CREATE TABLE TicketCollects ( 
	flight_time     TIMESTAMP WITH TIME ZONE, --Normally does not keep time zone 
	destination     VARCHAR(30), 
	source 		VARCHAR(30), 
	ticket_id 	VARCHAR(30) NOT NULL, 
	price 		FLOAT, 
	tclass 		VARCHAR(10), 
	airline 	VARCHAR(30), 
	
	website_address     VARCHAR(100), 
	travel_agency_name  VARCHAR(30),
	
	FOREIGN KEY (website_address) 	 REFERENCES HostWebsite(website_address) ON DELETE CASCADE ON UPDATE CASCADE, 
	FOREIGN KEY (travel_agency_name) REFERENCES TravelAgency(name) ON DELETE CASCADE ON UPDATE CASCADE, 
	 
	PRIMARY KEY(ticket_id) 
);
    
CREATE TABLE TransactionBuy ( 
	price	 				 FLOAT,
	transaction_datetime 	                 TIMESTAMP WITH TIME ZONE, 
	transaction_id 			         VARCHAR(30) NOT NULL,
	payment_service_provider                 VARCHAR(30), 
	
	username 				 VARCHAR(30), 
	ticket_id 				 VARCHAR(30) NOT NULL, 
	website_address 		         VARCHAR(100), 
	
	FOREIGN KEY(username) 		 REFERENCES Customer(username), 
	FOREIGN KEY(ticket_id) 		 REFERENCES TicketCollects(ticket_id) ON DELETE CASCADE ON UPDATE CASCADE, 
	FOREIGN KEY(website_address)     REFERENCES HostWebsite(website_address) ON DELETE CASCADE ON UPDATE CASCADE, 
	
	PRIMARY KEY(transaction_id) 
	
	);
