import tweepy
import csv

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
    # Make initial request for most recent tweets (200 is the maximum allowed count)(?)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200, 
                                    exclude_replies=True, include_rts=False)
    # Make sure no tweets are quote tweets
    no_quoted_new_tweets = []
    for tweet in new_tweets:
        # Make sure tweet isn't a quote tweet
        if hasattr(tweet, 'quoted_status'):
            # print "Found quote tweet, don't include it"
            continue
        no_quoted_new_tweets.append(tweet)
    all_tweets.extend(no_quoted_new_tweets)
    oldest = all_tweets[-1].id - 1
    # Keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        # All subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,
                                        exclude_replies=True, include_rts=False)
        # Make sure no tweets are quote tweets
        no_quoted_new_tweets = []
        for tweet in new_tweets:
            # Make sure tweet isn't a quote tweet
            if hasattr(tweet, 'quoted_status'):
                # print "Found quote tweet, don't include it"
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
    # Transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.text.encode("utf-8"), tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.lang] for tweet in tweets]
    # Write the csv  
    with open('Datasets/%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["text","created_at","favorite_count","retweet_count","lang"])
        writer.writerows(outtweets)

def main():
    # List of users we are going to search
    usernames = ['jess_hold', 'shlancaster39']
    # usernames = ['quotetweetonly']
    for name in usernames:
        print "------------------------NEW USER------------------------"
        print name
        tweets = get_all_tweets_for_user(name)
        output_tweets(tweets, name)

if __name__ == "__main__":
    main()



