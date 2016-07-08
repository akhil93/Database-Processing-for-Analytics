# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 22:57:05 2014

@author: Akhilkumar
"""

# #

import sqlite3

CTable = """
CREATE TABLE Chauffeurs
(
    LicenseNumber NUMBER, 
    Renewed VARCHAR(6), 
    Status VARCHAR(15),
    StatusDate VARCHAR(9), 
    DriverType VARCHAR(16), 
    LicenseType VARCHAR(9), 
    OriginalIssueDate VARCHAR(9), 
    Name VARCHAR(32), 
    Sex VARCHAR(6), 
    ChauffeurCity VARCHAR(25), 
    RecordNumber VARCHAR(11) NOT NULL,

    CONSTRAINT Chauffeurs_PK
    PRIMARY KEY (RecordNumber), 

    CONSTRAINT Chauffeurs_FK1
    FOREIGN KEY (ChauffeurCity) 
    REFERENCES CLocation(ChauffeurCity)
);
"""

CLocTable = """
CREATE TABLE CLocation
(
    ChauffeurCity VARCHAR(25),
    ChauffeurState VARCHAR(2),

    CONSTRAINT CLocPK 
    PRIMARY KEY (ChauffeurCity) 
);
"""

# Open a connection to database
conn = sqlite3.connect("StudentDatabase.db")

# Request a cursor from the database
cursor = conn.cursor()

# Get rid of the student table if we already created it
cursor.execute("DROP TABLE IF EXISTS Chauffeurs;")
cursor.execute("DROP TABLE IF EXISTS CLocation;")

cursor.execute(CTable)
cursor.execute(CLocTable)

fd = open('Public_Chauffeurs_Short.csv', 'r');
# Read all lines, but drop the first one ([1:] starts from 2nd line)
allLines = fd.readlines()[1:]
fd.close()

for line in allLines:

    valuesList = line.strip().split(',')

    # Replace the NULL values with proper NULL
    for index in range(len(valuesList)):
        if valuesList[index] == 'NULL':
            valuesList[index] = None # None is the NULL for python

    # Take the first 10 columns plus the 12th value
    # Note that + can append lists, i.e. [1,2,3]+[4,5] = [1,2,3,4,5]
    chList = valuesList[:10] + [valuesList[11]]
    # Take the 10th and 11th column (City, State)
    cityList = valuesList[9:11]

    cursor.execute("INSERT INTO Chauffeurs VALUES (?,?,?,?,?,?,?,?,?,?,?);", chList)
    cursor.execute("INSERT OR IGNORE INTO CLocation VALUES (?,?);", cityList)
 
# For each table, print the row contents
for table in ['Chauffeurs', 'CLocation']:
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

#
#