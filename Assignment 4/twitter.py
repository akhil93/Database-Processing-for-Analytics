# -*- coding: utf-8 -*-
"""
Created on Sat Nov 01 23:53:58 2014

@author: Akhilkumar
"""
import sqlite3
import json
import urllib2
webFD = urllib2.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Assignment4.txt")
tweet = webFD.readline()
tweet = tweet.split("         EndOfTweet          ")
tweet_records = [json.loads(line) for line in tweet]
attributes = ["created_at", "id_str", "text", "source", "in_reply_to_user_id", 
              "in_reply_to_screen_name", "in_reply_to_status_id", "retweet_count",
              "contributors"]
conn = sqlite3.connect("Assignment4.db")
cursor = conn.cursor()
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