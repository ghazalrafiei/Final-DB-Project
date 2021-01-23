-- DELETE FROM customer;
-- DELETE FROM hostwebsite;
-- DELETE FROM travelagency;
-- DELETE FROM ticket_collects;
-- DELETE FROM transaction_buy;
-- INSERT INTO customer;

VALUES('ghazal','rafiei','ghazalrafiei','0022557555','09128190667','post'),
	('saba','ahmadi','sabahamadi123','02122761778','09016839283','pass1234'),
	('sara','gholami','saragholami','980918283','09128199983','Pass');	


INSERT INTO hostwebsite
VALUES('www.abc.com'),('www.arlinebook.com'),('www.ticketBooking.com'),('www.arlinebookingticket.com');

INSERT INTO travelagency 
VALUES ('StartTrek', 'st. Jones','22761778');

INSERT INTO ticketCollects
VALUES('January 8 04:05:06 1999 PST' , 'Spain', 'Netherland' , '2546', 1239.99 , 'First', 'Lufthansa' , 'www.abc.com', 'StartTrek'),
('May 23 04:05:06 1989 PST','Germany','Denmark' , '2245', 495, 'Economy', 'AirAsia', 'www.ticketBooking.com','StartTrek')
;


INSERT INTO transactionBuy
VALUES ( 1239.99, 'October 10 23:37:06 2020 PST' , 'FSDF234Dfa324n','PayPal', 'ghazalrafiei', '2546','www.arlinebook.com'),
	(495 , 'March 19 9:09:09 2021 PST' , 'sjdhf23874skd', 'Parsian', 'sabahamadi123', '2245', 'www.ticketBooking.com');
