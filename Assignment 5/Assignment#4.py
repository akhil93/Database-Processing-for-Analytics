# -*- coding: utf-8 -*-
"""
Created on Sun Nov 02 19:24:54 2014

@author: Akhilkumar
"""
import urllib2
import json
import sqlite3

#import io

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

conn = sqlite3.connect("Assignment4.db")

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS TWEET")
cursor.execute(tweet_table)

webFD = urllib2.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Assignment4.txt")
tweet = webFD.readline()
tweet = tweet.split("EndOfTweet")
tweet_records = [json.loads(line) for line in tweet]
attributes = ("created_at", "id_str", "text", "source", "in_reply_to_user_id", 
              "in_reply_to_screen_name", "in_reply_to_status_id", "retweet_count",
              "contributors")
              
#changing Nulls              
for i in tweet_records:
    for key in i:
        if i[key] == None:
            i[key] = "NULL"           
        

i = 0
for single_tweet in tweet_records:
    cursor.execute("INSERT INTO TWEET VALUES (?,?,?,?,?,?,?,?,?);",(tweet_records[i][ "created_at"], 
    tweet_records[i]["id_str"], tweet_records[i]["text"], tweet_records[i]["source"],tweet_records[i]["in_reply_to_user_id"],
    tweet_records[i]["in_reply_to_screen_name"], tweet_records[i]["in_reply_to_status_id"], tweet_records[i]["retweet_count"],
    tweet_records[i]["contributors"]))
    i = i + 1
cursor.execute("SELECT * FROM TWEET;").fetchall()
    
#conn.commit()
#conn.close()
#conn.commit()


