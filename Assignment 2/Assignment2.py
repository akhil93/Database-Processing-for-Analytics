# -*- coding: utf-8 -*-
"""
Created on Tue Oct 07 23:09:43 2014

@author: Akhilkumar
"""
import csv
import sqlite3

# Creating a table called Information.
Information_Table = '''CREATE TABLE Information(
License_Number NUMBER(15),
Renewed DATE,
Status VARCHAR2(15),
Status_Date DATE,
Driver_Type VARCHAR2(20),
License_Type VARCHAR2(20),
Original_Issue_Date DATE,
Name VARCHAR(20),
Sex CHAR(7),
Chauffer_City CHAR(20),
Record_Number VARCHAR2(15) NOT NULL,

CONSTRAINT Rec_NumPK
  PRIMARY KEY(Record_Number) 
);'''

# Creating a table called Location.
Location_Table = '''CREATE TABLE Location(
Chauffer_City VARCHAR2(30),
Chauffer_State VARCHAR2(15),

CONSTRAINT City_FK
  FOREIGN KEY(Chauffer_City)
	REFERENCES INFORMATION(Chauffer_City)
);'''


# To open a connection to database
conn = sqlite3.connect("Assignment2.db")

#Request a cursor from the database
cursor = conn.cursor()

# Incase the tables is already present, then drop the tables.
cursor.execute("DROP TABLE IF EXISTS Information")
cursor.execute("DROP TABLE IF EXISTS Location")
# If there is no table with such name, then create Assignment2.db
cursor.execute(Information_Table)
cursor.execute(Location_Table)

# Let's open a file to populate the Information table in python
with open('Public_Chauffeurs_Short_hw3.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('Public_Chauffeurs_Short1_hw3.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9],rows[10]) for rows in reader}
cursor.executemany('''INSERT OR IGNORE INTO Information (License_Number,Renewed,Status,Status_Date,Driver_Type,
                    License_Type,Original_Issue_Date,Name,Sex,Chauffer_City,Record_Number) VALUES (?,?,?,?,?,?,?,?,?,?,?);''',mydict)

# Let's open a file to populate the Location table in python
with open('City.csv', mode='r') as infile1:
    reader1 = csv.reader(infile1)
    with open('City1.csv', mode='w') as outfile1:
        writer1 = csv.writer(outfile1)
        mydict1 = {(rows[0],rows[1]) for rows in reader1}
cursor.executemany('''INSERT OR IGNORE INTO Location (Chauffer_City,Chauffer_State) VALUES (?,?);''',mydict1)

conn.commit()
conn.close()