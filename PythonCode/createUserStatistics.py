import tweepy
import csv
import sys
import os
from sets import Set

# These keys and secrets are for the "Joke Suggester" app 
# on Shlancaster39's account
consumer_key = 'regenerated-and-never-checked-in-again'
consumer_secret = 'regenerated-and-never-checked-in-again'
access_token = 'regenerated-and-never-checked-in-again'
access_token_secret = 'regenerated-and-never-checked-in-again'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# PURPOSE: Creates a set of all usernames we have already analyzed
# INPUTS: string of file name
# RETURNS: Set of usernames already gotten
def GetUsersFromFile(file):
    analyzed_set = Set()
    with open(file, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            analyzed_set.add(row[0].lower())
    return analyzed_set

# PURPOSE: Analyzes everything we need about the passed in use. Utilizes tweepy API
# INPUTS: username of uswer we want to analyze
# RETURNS: list of all the stats needed to write to csv
def AnalyzeUser(username):
    stats = [username]
    user = api.get_user(username)
    stats.append(user.followers_count)
    stats.append(user.created_at)
    return stats

# PURPOSE: Writes one row to CSV file with all the user stats gathered
# INPUTS: list of user stats, outfile name
# RETURNS: nothing
def WriteRow(user_stats, outfile):
    writer = csv.writer(open(outfile,'a'))
    writer.writerow(user_stats)

# PURPOSE: update csv for twitter user info
#           CSV file format: username, follower_count, creation date
# COMMAND LINE ARGS: [directory name (with the /),
#                       filename and location we are writing to]
def main(argv):
    directory_name = argv[0]
    outfile_name = argv[1]
    analyzed_set = GetUsersFromFile(outfile_name)
    for file in os.listdir(directory_name):
        if not file.startswith('.'):
            username = file[:-11].lower()
            if username not in analyzed_set:
                print "Adding new user:", username
                user_stats = AnalyzeUser(username)
                WriteRow(user_stats, outfile_name)

if __name__ == "__main__":
    main(sys.argv[1:])



