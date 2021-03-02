DELETE FROM customer;
DELETE FROM hostwebsite;
DELETE FROM travelagency;
DELETE FROM ticketCollects;
DELETE FROM transactionBuy;
INSERT INTO customer 
VALUES('ghazal','rafraf','ghazalrafiei','0022557555','09128190667','passpass'),
	('user','test1','usertest1','02122761778','09016839283','pass1234'),
	('user1','test2','usertest2','980918283','09128199983','PaSs'),
	('user2','test3','usertest3','293874928','2039842934','ldsjfsd'),
	('user3','test4','usertest4','23423','234234','oidfosdf');	


INSERT INTO hostwebsite
VALUES('www.abc.com'),('www.airlinebook.com'),('www.ticketBooking.com'),('www.airlinebookingticket.com'),('www.ticketticket.com'),('www.myWebsite.com'),('www.AWebsite.com');

INSERT INTO travelagency 
VALUES ('StarTrek', 'st. Jones','22761778'),('ABC','st. idk','9824878273'),
	('Moonlight','st. here', '234234'),('XYZ','st. there','134234');

INSERT INTO ticketCollects
VALUES('January 8 04:05:06 1999 PST' , 'Spain', 'Netherland' , '2546', 1239.99 , 'First', 'Lufthansa' , 'www.abc.com', 'StarTrek'),
('May 23 04:05:06 1989 PST','Germany','Denmark' , '2245', 495, 'Economy', 'AirAsia', 'www.ticketBooking.com','StarTrek'),
('2021-12-02', 'Tehran' , 'Sari','7787',1231,'Economy','Mahan','www.myWebsite.com','Moonlight')
;


INSERT INTO transactionBuy
VALUES ( 1239.99, 'October 10 23:37:06 2020 PST' , 'FSDF234Dfa324n','PayPal', 'ghazalrafiei', '2546','www.airlinebook.com'),
	(495 , 'March 19 9:09:09 2021 PST' , 'sjdhf23874skd', 'Parsian', 'usertest1', '2245', 'www.ticketBooking.com'),
	(2342,'1989-1-09', 'lkf987qd','PayPal','usertest2','7787','www.abc.com');
