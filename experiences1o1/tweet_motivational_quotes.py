#!/usr/bin/python3

'''
Purpose: To tweet a motivational quote from a file periodically.
Author: Rohit Farmer
'''

# Standard library
import logging
import datetime
import os

# External library.
import tweepy

# Create a log file.
logging.basicConfig(filename='.log/tweet_motivation.log',level=logging.INFO)

# OAuth authentication.
with open('../../cred/exp.txt', 'r') as f: # Reading the credentials from a text file.
    creds = f.readlines()
    consumer_key = creds[0].rstrip()
    consumer_secret = creds[1].rstrip()
    access_token = creds[2].rstrip()
    access_token_secret = creds[3].rstrip()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

# Create tweepy object.
api = tweepy.API(auth)

try :
    f = open('motivationQuotes.txt', 'r')
    ft = open('temp.txt','w')
    quote = f.readline().rstrip()
    logging.info(quote)
except Exception as ex:
    logging.info(ex.message)

for i in f :
    ft.write(i)

os.remove('motivationQuotes.txt')
os.rename('temp.txt', 'motivationQuotes.txt')

# Update status.
try:
    api.update_status(quote)
except Exception as ex:
    logging.info(ex.message)

