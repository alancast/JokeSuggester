# -*- coding: utf-8 -*-
import time
import datetime
import praw
import os
import traceback
import requests
import csv
import sys
import os
import datetime


b = "timestamp:"
d = ".."


#Config Details-
r = praw.Reddit('searchandarchive by ')
def resume():
    if os.path.exists('config.txt'):
        line = file('config.txt').read()
        startStamp,endStamp,step,subName=line.split(',')
        startStamp,endStamp,step=int(startStamp),int(endStamp),int(step)
        return startStamp,endStamp,step,subName
    else:
        return 0

subName="jokes"
sdate="01/25/2012"
edate="01/30/2012"
step=3600

# subName=raw_input('Input the subreddit to archive: ')
# sdate=raw_input('Input start date in the format mm/dd/yyyy: ')
# edate=raw_input('Input end date in the format mm/dd/yyyy: ')
# step=input('Input seconds between each search, 30 recommended: ')

startStamp= int(time.mktime(datetime.datetime.strptime(sdate, "%m/%d/%Y").timetuple()))
endStamp= int(time.mktime(datetime.datetime.strptime(edate, "%m/%d/%Y").timetuple()))

obj=file('config.txt','w')
obj.write(str(startStamp)+','+str(endStamp)+','+str(step)+','+str(subName))
obj.close()

sdate=datetime.datetime.fromtimestamp(int(startStamp)).strftime('%m-%d-%Y')
edate=datetime.datetime.fromtimestamp(int(endStamp)).strftime('%m-%d-%Y')
folderName=str(subName+' '+str(sdate)+' '+str(edate))
if not os.path.exists(folderName):
    os.makedirs(folderName)


    
def main(startStamp,endStamp,step,folderName,subName,progress):
    totalTweets = 0

    startSpecialString = (datetime.datetime.fromtimestamp(int(startStamp)).strftime("%m-%d-%Y"))
    endSpecialString = (datetime.datetime.fromtimestamp(int(endStamp)).strftime("%m-%d-%Y"))
    fileNameString = 'RedditJokes/redditJokesFrom%s-To-%s.csv' % (str(startSpecialString),str(endSpecialString))
    ftwt = open(fileNameString, 'wb')   
    
    writer = csv.writer(ftwt)
    writer.writerow(["account","text","score","date"])

    count=step
    try:
        startStamp =open(folderName+"/lastTimestamp.txt").read()
        print("Resuming from timestamp: " + startStamp)
        time.sleep(2)
        startStamp=int(startStamp)
        progress=startStamp
    except: 
        pass
    c=1
    for currentStamp in range(startStamp,endStamp,step):
        e=' --'
        if(c%2==0):
            e=' |'
        f = str(currentStamp)
        g = str(currentStamp+step)
        search_results = r.search(b+f+d+g, subreddit=subName, syntax='cloudsearch')
        end=str((int((float(count)/float(progress)*20.0))*10)/2)+'%'
        count+=step
        for post in search_results:
            totalTweets += 1

            writer.writerow([str(post.author),str(post.title.encode('utf-8')) + "  "+ str(post.selftext.encode('utf-8')),str(post.score),(datetime.datetime.fromtimestamp(int(post.created)).strftime('%Y-%m-%d'))])
            # print '-------------------------------------------'
            # print str(post.title.encode('utf-8'))
            # print str(post.selftext.encode('utf-8'))
            # print '-------------------------------------------'
            print totalTweets
            # time.sleep(1)
        obj=open(folderName+"/lastTimestamp.txt", 'w')
        obj.write(str(currentStamp))
        obj.close()
        c+=1
    print('Welp, all done here! Stopped at timestamp '+ str(currentStamp))
progress = endStamp-startStamp
while True:
    try:
        main(startStamp,endStamp,step,folderName,subName,progress)
        exit()
    except KeyboardInterrupt:
        exit()
    except SystemExit:
        exit()
    except:
        print("Error in the program! The error was as follows: ")
        error = traceback.format_exc()
        time.sleep(5)
        print(error)
        time.sleep(5)
        print("Resuming in 5 seconds...")
        time.sleep(5)
