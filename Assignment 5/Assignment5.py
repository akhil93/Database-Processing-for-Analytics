# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 23:04:56 2014

@author: Akhilkumar
"""

import urllib2
import json
import sqlite3
from pandas import DataFrame

# crating a tweet table
tweet_table = '''CREATE TABLE TWEET(
created_at DATE,
id_str NUMBER(30),
text VARCHAR2(140),
source VARCHAR2(200),
in_reply_to_user_id NUMBER(30),
in_reply_to_screen_name VARCHAR2(30),
in_reply_to_status_id NUMBER(35),
retweet_count NUMBER(3),
contributors NULL,

CONSTRAINT id_PK
  PRIMARY KEY(id_str));
  
'''

# creating a table which stores user information

user_data = ''' CREATE TABLE USER(
id NUMBER(30),
name VARCHA2(20),
screen_name VARCHAR2(30),
description VARCHAR2(250),
friends_count NUMBER(5),

CONSTRAINT id_FK
    FOREIGN KEY(id)
	REFERENCES INFORMATION(id_str)
);'''


# creating a Database
conn = sqlite3.connect("Assignment4.db")
cursor = conn.cursor()

# if table alrady exists, then drop them
cursor.execute("DROP TABLE IF EXISTS TWEET")
cursor.execute("DROP TABLE IF EXISTS USER")

# executing the tables on sqlite3
cursor.execute(tweet_table)
cursor.execute(user_data)

#getting the twitter data.
webFD = urllib2.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Assignment5.txt")
lines = webFD.readlines()

# creating an empty list to store all the non parsed tweet data.
problematic_tweets = []
# creating an empty list to store all the parsed tweet data.
tweet_data = []

# for every line in the data check if the tweet data is parsable or not. 
# if it can be parsed then load it as json object and add it to list, if not then add it to other list.
for tweet in lines:
    try:
        tdict = json.loads(tweet)
        tweet_data.append(tdict)
    except ValueError:
        problematic_tweets.append(tweet)
        
# Subsetting to get the first 7000 tweet data.

tweet_7k = tweet_data[0:7000]

# lets extract the user data from the above file.
# creating an empty list to capture the data.


for i in range(7000):
    cursor.execute("INSERT OR IGNORE INTO USER VALUES (?,?,?,?,?);", (tweet_7k[i]['user']['id'],tweet_7k[i]['user']['name'],tweet_7k[i]['user']['screen_name'],tweet_7k[i]['user']['description'],tweet_7k[i]['user']['friends_count']))

for i in range(7000):
    cursor.execute("INSERT OR IGNORE INTO TWEET VALUES (?,?,?,?,?,?,?,?,?);",(tweet_7k[i][ "created_at"], 
    tweet_7k[i]["id_str"], tweet_7k[i]["text"], tweet_7k[i]["source"],tweet_7k[i]["in_reply_to_user_id"],
    tweet_7k[i]["in_reply_to_screen_name"], tweet_7k[i]["in_reply_to_status_id"], tweet_7k[i]["retweet_count"],
    tweet_7k[i]["contributors"]))
    
df = DataFrame()

df['text'] = map(lambda tweet_7k:tweet_7k['text'], tweet_7k)

big_text = ""
for i in range(7000):
    a = df['text'][i]
    big_text = big_text + a

words = big_text.split(" ")
dCount = {}
for word in words:
    if not dCount.has_key(word):
        dCount[word] = 0
    dCount[word] = dCount[word]+1

countKeys = dCount.keys()
countVals = dCount.values()
countPairs = zip(countVals, countKeys)

countPairs.sort(reverse = True)
# The words are now sorted by descending frequency
print countPairs

countPairs[0:4]

    











