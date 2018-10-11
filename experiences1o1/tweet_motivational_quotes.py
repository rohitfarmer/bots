#!/home/rohitfar/public_html/cgi-bin/anaconda3/bin/python3

import tweepy, os

#OAuth authentication

#creating an object
api = tweepy.API(auth)

f = open('motivationQuotes.txt', 'r')
ft = open('temp.txt','w')
quote = f.readline().rstrip()
print(quote)

for i in f :
	ft.write(i)

os.remove('motivationQuotes.txt')
os.rename('temp.txt', 'motivationQuotes.txt')

#Update status
api.update_status(quote)

