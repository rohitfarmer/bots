#!/usr/bin/python3

'''
Purpose: To re-tweet a tweet from the home timeline that has been re-tweeted atleast 15 times.
Author: Rohit Farmer
'''

# Standard library
import logging
import datetime

# External library.
import tweepy

# Create a log file.
logging.basicConfig(filename='.log/retweet.log',level=logging.INFO)

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

# Timeline methods.
acceptedTags =['travel','photography','lifestyle','traveller','nomad','food','foodporn','adventure','hike','skydiving','scuba','hiking','nikon','canon','outdoor','motivation','inspiration', 'recipe']

for tweet in tweepy.Cursor(api.home_timeline).items(250): # Iterate over the maximum allowed api calls.
    if tweet.retweet_count >= 15 : # Check if the tweet has been tweeted atleast 15 times.
        if tweet.retweeted :
            continue
        else :
            tweethashtags = tweet.entities['hashtags']
            for i in range(len(tweethashtags)):
                if tweethashtags[i]['text'].lower() in acceptedTags:
                    logging.info("\nRetweeting")
                    logging.info(tweet.text)
                    logging.info("ID string: " + str(tweet.id_str))
                    logging.info("Retweet count: " + str(tweet.retweet_count))
                    logging.info("Hashtags: " + str(tweethashtags))
                    # Re-tweet the tweet.
                    try:
                        api.retweet(tweet.id_str)
                    except Exception as ex:
                        logging.info(ex)
