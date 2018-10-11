#!/home/rohitfar/public_html/cgi-bin/anaconda3/bin/python3

import tweepy, os

#OAuth authentication

#creating an object
api = tweepy.API(auth)

following = api.friends_ids('experiences1o1')

followers = api.followers_ids('experiences1o1')

for f in following:
	if f in followers:
		continue
	else:
		print("Not following: ",f)
		print("Unfollowing: ",f)
		api.destroy_friendship(f)
