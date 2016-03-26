import tweepy
import csv
import sys
import os
from sets import Set
import time

# These keys and secrets are for the "Joke Suggester" app 
# on Shlancaster39's account
consumer_key = 'L9jRZtrpgbJNu6Z9fPMfxPiZq'
consumer_secret = '5AkgpcNeRAc4IIB6kolZIjJ9DWH6g31ndx5LeLTZZtQqfbllGP'
access_token = '599251230-V3Tl1N3qnlgpd0PViBFB0aclXiVuEaaKMd3KQBUA'
access_token_secret = 'MY8DqQ3sbECkXU0iUr6MfRdasWIaDW8MKc5DuH2G8VBfG'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Gets all the tweets from the passed in user name
# INPUTS: twitter handle (username for the noobs out there)
# RETURNS: List of all tweets for that user
# Got this from https://gist.github.com/yanofsky/5436496
def get_all_tweets_for_user(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method
    # Initialize a list to hold all the tweepy Tweets
    all_tweets = []
    try:
        # Make initial request for most recent tweets (200 is the maximum allowed count)(?)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200, 
                                        exclude_replies=True, include_rts=False)
    except tweepy.TweepError, e:
        print "Caught some tweepy exception:", e
        if type(e) == tweepy.error.RateLimitError:
            sys.exit()
        return
    # Make sure no tweets are quote tweets
    no_quoted_new_tweets = []
    for tweet in new_tweets:
        # Make sure tweet isn't a quote tweet
        if hasattr(tweet, 'quoted_status'):
            continue
        no_quoted_new_tweets.append(tweet)
    all_tweets.extend(no_quoted_new_tweets)
    oldest = all_tweets[-1].id - 1
    # Keep grabbing tweets until there are no tweets left to grab
    while len(no_quoted_new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        try:
            # All subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,
                                            exclude_replies=True, include_rts=False)
        except tweepy.TweepError, e:
            print "Caught some tweepy exception:", e
            sys.exit()
        # Make sure no tweets are quote tweets
        no_quoted_new_tweets = []
        for tweet in new_tweets:
            # Make sure tweet isn't a quote tweet
            if hasattr(tweet, 'quoted_status'):
                continue
            no_quoted_new_tweets.append(tweet)
        all_tweets.extend(no_quoted_new_tweets)
        oldest = all_tweets[-1].id - 1
        print "...%s tweets downloaded so far" % (len(all_tweets))
    return all_tweets

# Outputs all the tweets in the passed in list
# INPUTS: list of tweepy tweets, twitter handle of user who tweets belong to
# RETURNS: nothing
def output_tweets(tweets, screen_name):
    if tweets == None:
        return
    # Transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.text.encode("utf-8"), tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.lang] for tweet in tweets]
    # Write the csv  
    with open('Datasets/%s_tweets.csv' % screen_name.lower(), 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["text","created_at","favorite_count","retweet_count","lang"])
        writer.writerows(outtweets)

# Creates a set of all usernames we have already grabbed tweets from
# INPUTS: string of directory name
# RETURNS: Set of usernames already gotten
def GetUsersFromDirectory(directory):
    gotten_set = Set()
    for file in os.listdir(directory):
        gotten_set.add(file[:-11].lower())
    return gotten_set

# Counts the number of data rows (tweets) in an entire directory
# COMMAND LINE ARGS: [filename and location of list of twitter accounts,
#                       directory name (with the /) of dataset of tweets]
def main(argv):
    infile_name = argv[0]
    directory_name = argv[1]
    # Populate set of usernames we have already finished
    done_set = GetUsersFromDirectory(directory_name)
    # Read in file with list of users we are going to search
    with open(infile_name) as f:
        for line in f:
            name = line.strip().lower()
            # Already have tweets from that user so continue to next user
            if name in done_set:
                continue
            print "------------------------NEW USER------------------------"
            print name
            tweets = get_all_tweets_for_user(name)
            output_tweets(tweets, name)
            print "Sleeping for .75 minutes starting from:", time.strftime("%H:%M:%S")
            time.sleep(45)
            print "Done sleeping at:", time.strftime("%H:%M:%S")

if __name__ == "__main__":
    main(sys.argv[1:])



