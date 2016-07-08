/*
CREATE TABLE Authors
(
AuthorID VARCHAR2(10),
Lastname VARCHAR2(30),
Firstname VARCHAR2(30),
Birthdate DATE,

CONSTRAINT Authour_PK
  PRIMARY KEY(AuthorID)
);
CREATE TABLE Publishers
(
PublisherID VARCHAR2(10),
PublisherName VARCHAR2(30),
Address VARCHAR2(40),

CONSTRAINT Publisher_PK
  PRIMARY KEY(PublisherID)
);
CREATE TABLE Books(
ISBN VARCHAR2(15),
Title VARCHAR2(30),
PublisherID VARCHAR2(10),

CONSTRAINT ISBN_PK
  PRIMARY KEY(ISBN),

CONSTRAINT Pub_ID
  FOREIGN KEY(PublisherID)
    REFERENCES Publishers(PublisherID)
);
CREATE TABLE Writes
(
Book_ISBN VARCHAR2(15),
AuthorID VARCHAR2(10),
Book_Rank NUMBER(1),

CONSTRAINT Aut_FK
  FOREIGN KEY(AuthorID)
    REFERENCES Authors(AuthorID),
CONSTRAINT Book_FK
  FOREIGN KEY(Book_ISBN)
    REFERENCES Books(ISBN)
);
*/
-- q3
INSERT INTO Authors VALUES ('2','King', 'Stephen', '09-Sep-1947');
INSERT INTO Authors VALUES ('4', 'Asimov', 'Isaac', '02-Jan-1920');
INSERT INTO Authors VALUES ('7','Verne', 'Jules','08-Feb-1828');
INSERT INTO Authors VALUES ('37','Rowling', 'Joanne', '31-Jul-1965');

-- q4
INSERT INTO Publishers VALUES ('17', 'Bloomsbury Publishing', 'London Borough of Camden');
INSERT INTO Publishers VALUES ('18', 'Arthur A. Levine Books', 'London Borough of Camden');

--q5
INSERT INTO Books VALUES ('1111-111','Databases from outer space', '17');
INSERT INTO Books VALUES ('2222-222','Dark SQL', '17');
INSERT INTO Books VALUES ('3333-333','The night of living databases', '18');

--q6
INSERT INTO Writes VALUES ('1111-111','2','1');
INSERT INTO Writes VALUES ('1111-111','4','2');
INSERT INTO Writes VALUES ('2222-222','4','2');
INSERT INTO Writes VALUES ('2222-222','7','1');
INSERT INTO Writes VALUES ('3333-333','37','1');
INSERT INTO Writes VALUES ('3333-333','2','2');