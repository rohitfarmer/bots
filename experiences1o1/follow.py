#!/home/rohitfar/public_html/cgi-bin/anaconda3/bin/python3

import tweepy, os

#OAuth authentication
i

#creating an object
print("api object created")
api = tweepy.API(auth)

print("Extracting following ids")
following = api.friends_ids('experiences1o1')

print("Extracting follower ids")
followers = api.followers_ids('experiences1o1')

acceptedTags =['travel','explore','nomad','writer','blog','wander','photo','lifestyle','food','adventure','hike','skydiv','scuba','outdoor','chef']

print("Searching")
count = 0
for f in followers:
	count += 1
	if count >=50:
		break
	found = False
	if f in following:
		continue
	else:
		print("Getting user info at:",count)
		userinfo = api.get_user(f)
		desc = userinfo.description
		for ht in acceptedTags:
			if found:
				continue
			elif ht in desc.lower():
				print(userinfo.name)
				print(userinfo.description)
				api.create_friendship(f)
				found = True
