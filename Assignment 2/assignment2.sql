CREATE TABLE INFORMATION(
Record_Number VARCHAR2(15) NOT NULL,
License_Number VARCHAR2(15),
Renewed DATE,
Status VARCHAR2(15),
Status_Date DATE,
Driver_Type VARCHAR2(20),
License_Type VARCHAR2(20),
Original_Issue_Date DATE,
Name VARCHAR(20),
Sex CHAR(7),
Chauffer_City CHAR(20),

CONSTRAINT Rec_NumPK
  PRIMARY KEY(Record_Number)
);

CREATE TABLE Location(
Chauffer_City VARCHAR2(30),
Chauffer_State VARCHAR2(15),

CONSTRAINT City_FK
  FOREIGN KEY(Chauffer_City)
	REFERENCES INFORMATION(Chauffer_City)
);

DROP TABLE Animal;

-- ACategory: Animal category 'common', 'rare', 'exotic'.  May be NULL
-- TimeToFeed: Time it takes to feed the animal (hours)
CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR2(30) NOT NULL,
  ACategory VARCHAR2(18),
  
  TimeToFeed NUMBER(4,2),  
  
  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);


INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);
INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);
INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);
INSERT INTO Animal VALUES(4, 'Grizzly bear', NULL, 2.5);
INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.5);
INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.75);
INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.75);
INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.75);
INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.25);
INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.25);
INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.5);

select AName from Animal where TimeToFeed < 1.5;
select AName, TimeToFeed from Animal where ACategory = 'rare' order by TimeToFeed;
select AName, ACategory from Animal where AName like '%bear';
select AName from Animal where ACATEGORY is null;
SELECT AName from ANIMAL where ACategory = 'rare' and TIMETOFEED BETWEEN 1 and 2.5;
select AName from Animal where ACATEGORY != 'common' and AName like '%tiger';
select min(TimeToFeed),max(TimeToFeed) from Animal;
select avg(TimeToFeed) from ANIMAL where ACATEGORY = 'rare';
 