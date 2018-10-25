#!/usr/bin/env python3

'''
Purpose: To fetch tweets from the home time line using since id.
'''

# Standard library
import logging
import datetime, time
import sqlite3
import os
from datetime import datetime

# External library
import tweepy

# Logging configuration
logging.basicConfig(filename='../.log/tweets_capture_hometimeline.log',level=logging.INFO)

# Twitter OAuth authentication
with open('../../../cred/country.txt', 'r') as f: # Reading the credentials from a text file.
    creds = f.readlines()
    consumer_key = creds[0].rstrip()
    consumer_secret = creds[1].rstrip()
    access_token = creds[2].rstrip()
    access_token_secret = creds[3].rstrip()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

# Creating a tweepy object
api = tweepy.API(auth)

# Fetch current UTC time.
date = datetime.utcnow().strftime("%Y%b")
year = date[:4]
month = date[4:]

# Check if the year folders exists.
data_dir = '../data/'
path_year =  data_dir + year
if os.path.isdir(path_year):
    pass
else:
    os.mkdir(path_year)
    logging.info("Creating directory for this year.")

file_month = path_year + "/" + month + ".tsv"
if os.path.exists(file_month):
    pass
else:
    with open(file_month, 'w') as f:
        logging.info("Creating a new monthly file.")

# Open since_id file.
with open('since_id.txt', 'r') as sf:
    tweet_id = sf.readline().rstrip()

# Fetch recent tweets and append in the tsv file.
with open(file_month, 'a') as t:
    language = ""
    stat = ""
    user_id = ""
    stat_id = ""
    create = ""
    name = ""

    for status in api.home_timeline(since_id=tweet_id, tweet_mode='extended'):
        language = status.lang
        stat = status.full_text
        stat = stat.replace('\n','')
        stat = stat.replace('\t','')
        user_id = status.user.id_str
        stat_id = status.id_str
        create = str(status.created_at)
        name = status.user.screen_name
        try:
            data = language + "\t" + create + "\t" + user_id + "\t" + name + "\t" + stat_id + "\t" + stat + "\n"
            t.write(data)
        except Exception as ex:
            logging.info(ex)

# Write the updated since_id.
if stat_id != "" :
    with open('since_id.txt', 'w') as sf:
        try:
            sf.write(stat_id)
        except Exception as ex:
            logging.info(ex)