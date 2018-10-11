#!/usr/bin/python3

'''
Purpose: To follow the users who have followed experiences1o1 and also has certain keyword(s).
Author: Rohit Farmer
'''

# Standard library
import logging
import datetime

# External library.
import tweepy

# Create a log file.
logging.basicConfig(filename='.log/follow.log',level=logging.INFO)

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

logging.info("Extracting following ids")
following = api.friends_ids('experiences1o1')

logging.info("Extracting follower ids")
followers = api.followers_ids('experiences1o1')

acceptedTags =['travel','explore','nomad','writer','blog','wander','photo','lifestyle','food','adventure','hike','skydiv','scuba','outdoor','chef']

logging.info("Searching")
count = 0
for f in followers:
    count += 1
    if count >=50:
        break
    found = False
    if f in following:
        continue
    else:
        logging.info("Getting user info at:" + str(count))
        userinfo = api.get_user(f)
        desc = userinfo.description
        for ht in acceptedTags:
            if found:
                continue
            elif ht in desc.lower():
                logging.info(userinfo.name)
                logging.info(userinfo.description)
                try:
                    api.create_friendship(f)
                    found = True
                except Exception as ex:
                    logging.info(ex.message)
