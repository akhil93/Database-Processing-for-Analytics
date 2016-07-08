# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 02:32:43 2014

@author: Akhilkumar
"""
import sqlite3

# Creating a table called Information.
Information_Table = '''CREATE TABLE Information(
License_Number NUMBER(15) ,
Renewed DATE,
Status VARCHAR2(15),
Status_Date DATE,
Driver_Type VARCHAR2(20),
License_Type VARCHAR2(20),
Original_Issue_Date DATE,
Name VARCHAR(30),
Sex CHAR(7),
Chauffer_City CHAR(20),
Record_Number VARCHAR2(15) NOT NULL,

CONSTRAINT Rec_NumPK
  PRIMARY KEY(Record_Number) 
  
CONSTRAINT Information_FK1
    FOREIGN KEY (Chauffer_City) 
    REFERENCES CLocation(Chauffer_City)
);'''

# Creating a table called Location.
Location_Table = '''CREATE TABLE Location(
Chauffer_City VARCHAR2(30),
Chauffer_State VARCHAR2(15),

CONSTRAINT CLocPK 
    PRIMARY KEY (Chauffer_City)
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
fd = open('Public_Chauffeurs_Short.csv', 'r');
# As the fisrt row contains the row names, we should drop that row
allLines = fd.readlines()[1:]
fd.close()

for line in allLines:

    values = line.strip().split(',')

    # Replacing the NULL values with python NULL
    for i in range(len(values)):
        if values[i] == 'NULL':
            values[i] = None 

    # The first table should contain the first 10 and the 12 column
    Inf = values[:10] + [values[11]]
    # The second table should contain City & State column
    City = values[9:11]

    cursor.execute("INSERT INTO Information VALUES (?,?,?,?,?,?,?,?,?,?,?);", Inf)
    cursor.execute("INSERT OR IGNORE INTO Location VALUES (?,?);", City)


# For each table, print the row contents
for table in ['Information', 'Location']:
    allRows = cursor.execute("SELECT * FROM %s;" % table).fetchall()

    rowCount = 0 
    # For every row, print the results of the query above, separated by a tab
    for eachRow in allRows:
        print "ROW#"+str(rowCount),
        rowCount = rowCount+1
        for value in eachRow:
            print value, "\t",
        print "\n", # \n is the end of line symbol

# Finalize inserts and close the connection to the database
conn.commit()
conn.close()