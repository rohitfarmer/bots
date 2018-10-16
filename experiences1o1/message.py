#!/usr/bin/python3

'''
Purpose: To send a message to the followers, telling them about our instagram page.
Note: Using twurl to send the message. Tweepy send message is not working due to the update in the twitter api.
Author: Rohit Farmer
'''

# Standard library
import logging
import datetime
import os
import pickle

# External library.
import tweepy

# Create a log file.
logging.basicConfig(filename='.log/message.log',level=logging.INFO)

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
api = tweepy.API(auth, wait_on_rate_limit=True)


# Print a timestamp in the log file.
timestamp = datetime.datetime.now()
logging.info(timestamp)

# Read/create sent message users list.
if os.path.isfile('sent_user_list.pickle'):
    try:
        with open('sent_user_list.pickle', 'rb') as s:
            sent_user_list = pickle.load(s)
    except:
        logging.info("Exception occurred in reading pickle!!")
else:
    try:
        sent_user_list = [851383179407532032]
        with open('sent_user_list.pickle', 'wb') as s:
            pickle.dump(sent_user_list, s, pickle.HIGHEST_PROTOCOL)
    except:
        logging.info("Exception occurred while creating pickle!!")

logging.info("Extracting follower ids")
followers = api.followers_ids('experiences1o1')

for follower in followers:
    if follower in sent_user_list:
        continue
    else:
        user_info = api.get_user(follower)
        name = user_info.name
        msg = "Hi " + name + ", thank you for following us on Twitter. We also have an Instagram account where we post pictures from our lifestyle, travel, adventure and food experiences. We are sure that you would like them as well. Please visit: https://www.instagram.com/experiences1o1/"
        
        try:
            data = '\'{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "' + str(follower) + '"}, "message_data": {"text":' + '"' + msg + '"' + ' }}}}\''
            command = 'twurl -c ' + str(consumer_key) + ' -s ' + str(consumer_secret) + ' -a ' + str(access_token) + ' -S ' + str(access_token_secret) + ' -A ' + '"Content-type: application/json"' + ' -X  POST /1.1/direct_messages/events/new.json' + ' -d ' + data
            os.system(command)
            sent_user_list.append(follower)
        except Exception as ex:
            logging.info(ex)

# Write the updated sent message user list.
try:
    with open('sent_user_list.pickle', 'wb') as s:
        pickle.dump(sent_user_list, s, pickle.HIGHEST_PROTOCOL)
except:
    logging.info("Exception occurred while writing pickle!!")