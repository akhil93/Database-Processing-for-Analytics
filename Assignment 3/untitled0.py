import re
import sqlite3
from sqlite3 import OperationalError

conn = sqlite3.connect('csc455_HW3.db')
c = conn.cursor()

# Open and read the file as a single buffer
fd = open('ZooDatabase.sql', 'r')
# Read as a single document (not individual lines)
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';' which separates them)
sqlCommands = sqlFile.split(';')

# Execute every command from the input file (separated by ";")
for command in sqlCommands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    
    try:
        command = re.sub('[\n\t]',"",command) # this removes all the whitespaces
        c.execute(command)
    except OperationalError, msg:
        print "Command skipped: ", msg
for command in sqlCommands:
    output =  c.execute(command).fetchall()
    for row in output:
        for value in row:
            print value, "\t",
        print "\n",
    print "\n"


c.close()
conn.commit()
conn.close()
