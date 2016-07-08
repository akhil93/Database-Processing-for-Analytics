# -*- coding: utf-8 -*-
"""
Created on Sun Nov 02 19:24:54 2014

@author: Akhilkumar
"""
import pandas as pd
from pandas import DataFrame,Series
import urllib2
import json
import sqlite3
from io import open
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
              
#changing Nulls              
for i in tweet_records:
    for key in i:
        if i[key] == None:
            i[key] = "NULL"   
    
attributes = ("created_at", "id_str", "text", "source", "in_reply_to_user_id", 
              "in_reply_to_screen_name", "in_reply_to_status_id", "retweet_count",
              "contributors")
tweet_data = DataFrame(columns = attributes)
j = 0
created_at = []
for j in range(len(tweet_records)):
    x = tweet_records[j]["created_at"]
    created_at.append(x.encode("utf-8"))
tweet_data["created_at"] = created_at

j = 0
id_str = []
for j in range(len(tweet_records)):
    x = tweet_records[j]["id_str"]
    id_str.append(x.encode("utf-8"))
tweet_data["id_str"] = id_str

j = 0
text = []
for j in range(len(tweet_records)):
    x = tweet_records[j]["text"]
    text.append(x.encode("utf-8"))
tweet_data["text"] = text

j = 0
source = []
for j in range(len(tweet_records)):
    x = tweet_records[j]["source"]
    source.append(x.encode("utf-8"))
tweet_data["source"] = source

j = 0
in_reply_to_user_id = []
for j in range(len(tweet_records)):
    x = tweet_records[j]["in_reply_to_user_id"]
    in_reply_to_user_id.append(x)
tweet_data["in_reply_to_user_id"] = in_reply_to_user_id

j = 0
in_reply_to_screen_name = []
for j in range(len(tweet_records)):
    x = tweet_records[j]["in_reply_to_screen_name"]
    in_reply_to_screen_name.append(x.encode("utf-8"))
tweet_data["in_reply_to_screen_name"] = in_reply_to_screen_name

j = 0
in_reply_to_status_id = []
for j in range(len(tweet_records)):
    x = tweet_records[j]["in_reply_to_status_id"]
    in_reply_to_status_id.append(x)
tweet_data["in_reply_to_status_id"] = in_reply_to_status_id

j = 0
retweet_count = []
for j in range(len(tweet_records)):
    x = tweet_records[j]["retweet_count"]
    retweet_count.append(x)
tweet_data["retweet_count"] = retweet_count

j = 0
contributors = []
for j in range(len(tweet_records)):
    x = tweet_records[j]["contributors"]
    contributors.append(x.encode("utf-8"))
tweet_data["contributors"] = contributors


def df2sqlite(dataframe, db_name = "import.sqlite", tbl_name = "tweet"):
 
  import sqlite3
  conn=sqlite3.connect(db_name)
  cur = conn.cursor()                                 
 
  wildcards = ','.join(['?'] * len(dataframe.columns))              
  data = [tuple(x) for x in dataframe.values]
 
  cur.execute("drop table if exists %s" % tbl_name)
 
  col_str = '"' + '","'.join(dataframe.columns) + '"'
  cur.execute("create table %s (%s)" % (tbl_name, col_str))
 
  cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), data)
 
  conn.commit()
  conn.close()
df2sqlite(tweet_data)


    
   
    
#conn.commit()
#conn.close()
#conn.commit()
