#!/usr/bin/python3

'''
Purpose: To unfollow users who are not following experiences1o1 anymore.
Author: Rohit Farmer
'''

# Standard library
import logging
import datetime

# External library.
import tweepy

# Create a log file.
logging.basicConfig(filename='.log/unfollow.log',level=logging.INFO)

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

# Print a timestamp in the log file.
timestamp = datetime.datetime.now()
logging.info(timestamp)

following = api.friends_ids('experiences1o1')

followers = api.followers_ids('experiences1o1')

for f in following:
    if f in followers:
        continue
    else:
        logging.info("Not following: " + str(f))
        logging.info("Unfollowing: " + str(f))
        try:
            api.destroy_friendship(f)
        except Exception as ex:
            logging.info(ex.message)
