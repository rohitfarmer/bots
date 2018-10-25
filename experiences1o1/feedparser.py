#!/usr/bin/python3

# External library.
import feedparser

d = feedparser.parse('https://feeds.feedburner.com/zenhabits')
print(d['feed']['title'])