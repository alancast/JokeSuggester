import tweepy

# These keys and secrets are for the "Joke Suggester" app 
# on Shlancaster39's account
consumer_key = 'L9jRZtrpgbJNu6Z9fPMfxPiZq'
consumer_secret = '5AkgpcNeRAc4IIB6kolZIjJ9DWH6g31ndx5LeLTZZtQqfbllGP'
access_token = '599251230-V3Tl1N3qnlgpd0PViBFB0aclXiVuEaaKMd3KQBUA'
access_token_secret = 'MY8DqQ3sbECkXU0iUr6MfRdasWIaDW8MKc5DuH2G8VBfG'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# List of users we are going to search
usernames = ['twitter', 'shlancaster39']
for name in usernames:
    # Get the User object for the user we are currently searching
    user = api.get_user(name)
    print user.screen_name
    print user.followers_count
    # Iterates through tweets from the given user
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=user.screen_name).items(3):
        print(tweet.created_at)
        print(tweet.favorite_count)
        print(tweet.retweet_count)
        print(tweet.lang)
        print(tweet.text)