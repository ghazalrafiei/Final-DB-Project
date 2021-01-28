DELETE FROM customer;
DELETE FROM hostwebsite;
DELETE FROM travelagency;
DELETE FROM ticketCollects;
DELETE FROM transactionBuy;
INSERT INTO customer 
VALUES('ghazal','rafraf','ghazalrafiei','0022557555','09128190667','passpass'),
	('user','test1','usertest1','02122761778','09016839283','pass1234'),
	('user1','test2','usertest2','980918283','09128199983','PaSs');	


INSERT INTO hostwebsite
VALUES('www.abc.com'),('www.airlinebook.com'),('www.ticketBooking.com'),('www.airlinebookingticket.com');

INSERT INTO travelagency 
VALUES ('StartTrek', 'st. Jones','22761778'),('ABC','st. idk','9824878273');

INSERT INTO ticketCollects
VALUES('January 8 04:05:06 1999 PST' , 'Spain', 'Netherland' , '2546', 1239.99 , 'First', 'Lufthansa' , 'www.abc.com', 'StartTrek'),
('May 23 04:05:06 1989 PST','Germany','Denmark' , '2245', 495, 'Economy', 'AirAsia', 'www.ticketBooking.com','StartTrek');


INSERT INTO transactionBuy
VALUES ( 1239.99, 'October 10 23:37:06 2020 PST' , 'FSDF234Dfa324n','PayPal', 'ghazalrafiei', '2546','www.airlinebook.com'),
	(495 , 'March 19 9:09:09 2021 PST' , 'sjdhf23874skd', 'Parsian', 'usertest1', '2245', 'www.ticketBooking.com');
