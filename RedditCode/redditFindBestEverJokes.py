import praw
from pprint import pprint
import datetime
import csv
import sys
import os

r = praw.Reddit('Comment parser example by u/_Daimon_')
subreddit = r.get_subreddit("jokes")
posts = subreddit.get_top_from_all(limit=None)
#posts = subreddit.get_top_from_day(limit=None)
count = 1

f = open('RedditJokes/bestEver.csv', 'wb')	
writer = csv.writer(f)
writer.writerow(["account","text","score","date"])
for x in posts:
	writer.writerow([str(x.author),str(x.title.encode('utf-8')) + " ||| "+ str(x.selftext.encode('utf-8')),str(x.score),(datetime.datetime.fromtimestamp(int(x.created)).strftime('%Y-%m-%d'))])
	# print str(x.author.name)
	# print str(x.author)
	# pprint(vars(x))
	# print str(x.score)
	# print(datetime.datetime.fromtimestamp(int(x.created)).strftime('%Y-%m-%d'))
	# print str(x.title.encode('utf-8'))
	# print str(x.selftext.encode('utf-8'))
	# print '---------------------------'
	# break
	print count
	count += 1


	