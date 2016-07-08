# -*- coding: utf-8 -*-
"""
Created on Tue Oct 07 23:09:43 2014

@author: Akhilkumar
"""
import os
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

# To open a connection to database
conn = sqlite3.connect("Assignment2.db")

#Request a cursor from the database
cursor = conn.cursor()

# Incase the table is already present, then drop the table.
cursor.execute("DROP TABLE IF EXISTS Information")

# If there is no table with such name, then create Assignment2.db
cursor.execute(Information_Table)

# Let's open a file for reading data into python
FD =  open("Public_Chauffeurs_Short.csv","r")
allLines = FD.readlines()
FD.close()
for line in allLines:
    valueList = line.strip()
    cursor.executemany('''INSERT OR IGNORE INTO Information (License_Number,Renewed,Status,Status_Date,Driver_Type,
                    License_Type,Original_Issue_Date,Name,Sex,Chauffer_City,Record_Number) VALUES (?,?,?,?,?,?,?,?,?,?,?);''',valueList)
conn.commit()
conn.close()