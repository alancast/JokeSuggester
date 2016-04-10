import csv
import sys
import os
import pprint

id_count = 1

# PURPOSE: Creates a dictionary of username to (follower_count, creation_date)
# INPUTS: string of file name
# RETURNS: dictionary of username to (follower_count, creation_date)
def GetStatsFromFile(file):
    statistics = {}
    with open(file, 'rb') as csvfile:
        # Skip header
        csvfile.next()
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            statistics[row[0].lower()] = (row[1], row[2])
        csvfile.close()
    return statistics

# PURPOSE: Reads in a users tweets and writes them to the master list
#           Also gets all the stats needed from that user (averages and maxes)
# INPUTS: infile = Name of CSV file we need to read, 
#         user_info = (username, follower_count, account_creation_date), 
#         outfile = Name of CSV file we are writing to
# RETURNS: nothing
def ReadAndWriteTweets(infile, user_info, outfile):
    global id_count
    # Stats that will be needed for every tweet
    average_favorites = 0
    average_retweets = 0
    max_favorites = 0
    max_retweets = 0
    username = user_info[0]
    upvotes = 0
    average_upvotes = 0
    max_upvotes = 0
    follower_count = user_info[1]
    account_creation_date = user_info[2]
    # List of lists with all the stuff we need for master list
    tweet_data = []
    # Read this persons twitter csv
    with open(infile, 'rb') as csv_infile:
        # Skip header
        csv_infile.next()
        csvreader = csv.reader(csv_infile)
        # Read every row and add data as needed
        for row in csvreader:
            master_id = 1
            text = row[0]
            creation_date = row[1]
            favorites = int(row[2])
            retweets = int(row[3])
            tweet = [master_id, text, username, creation_date, favorites,\
                    retweets, upvotes, average_favorites, max_favorites,\
                    average_retweets, max_retweets, average_upvotes,\
                    max_upvotes, follower_count, account_creation_date, 0]
            # Update stats
            average_retweets += retweets
            average_favorites += favorites
            if favorites > max_favorites:
                max_favorites = favorites
            if retweets > max_retweets:
                max_retweets = retweets
            # Add this tweet to the list we need
            tweet_data.append(tweet)
        csv_infile.close()
    # Make averages acutal averages
    average_favorites = float(average_favorites)/float(len(tweet_data))
    average_retweets = float(average_retweets)/float(len(tweet_data))
    file_to_open = open(outfile,'a')
    writer = csv.writer(file_to_open)
    # Write all rows to outfile
    for tweet in tweet_data:
        tweet_with_stats = tweet
        # Update tweet to have real stats
        tweet_with_stats[0] = id_count
        id_count += 1
        tweet_with_stats[7] = average_favorites
        tweet_with_stats[8] = max_favorites
        tweet_with_stats[9] = average_retweets
        tweet_with_stats[10] = max_retweets
        # Write row to CSV
        writer.writerow(tweet_with_stats)
    file_to_open.close()

# PURPOSE: Reads in a reddit joke file and appends it to a list
#           Also updates all the stats needed from that file (averages and maxes)
# INPUTS: infile = Name of CSV file we need to read
#           total_upvotes = current total upvotes from all reddit jokes
#           max_upvotes = current max upvotes from all reddit jokes
# RETURNS: List of rows to write from that Reddit file,
#           Updated Reddit joke count
#           Updated Reddit upvote count 
#           Updated Reddit max upvote
def ReadRedditJokes(infile, total_upvotes, max_upvotes):
    # Stats that will be needed for every joke
    average_favorites = 0
    average_retweets = 0
    max_favorites = 0
    max_retweets = 0
    favorites = 0
    retweets = 0
    average_upvotes = 0
    follower_count = 0
    account_creation_date = 0
    tweet_count = 0
    # List of lists with all the stuff we need for master list
    file_jokes = []
    # Read this persons twitter csv
    with open(infile, 'rb') as csv_infile:
        # Skip header
        csv_infile.next()
        csvreader = csv.reader(csv_infile)
        # Read every row and add data as needed
        for row in csvreader:
            master_id = 1
            username = row[0]
            text = row[1]
            upvotes = int(row[2])
            creation_date = row[3]
            joke = [master_id, text, username, creation_date, favorites,\
                    retweets, upvotes, average_favorites, max_favorites,\
                    average_retweets, max_retweets, average_upvotes,\
                    max_upvotes, follower_count, account_creation_date, 1]
            # Update stats
            total_upvotes += upvotes
            if upvotes > max_upvotes:
                max_upvotes = upvotes
            # Add this joke to the list we need
            file_jokes.append(joke)
        csv_infile.close()
    return file_jokes, total_upvotes, max_upvotes

# PURPOSE: Create one master CSV with all the jokes from all 
#           twitter accounts and all reddit jokes
# COMMAND LINE ARGS: <tweets_directory_name> (with the /),
#                    <reddit_directory_name> (with the /),
#                    <user_statistics_filename>,
#                    <outfile_name> 
def main(argv):
    if len(argv) < 4:
        print "ABORTING: Need 4 command line arguments: "
        print "<tweets_directory> <reddit_directory> <user_statistics_file> <outfile_name>"
        exit(1)
    tweets_directory = argv[0]
    reddit_directory = argv[1]
    user_statistics_file = argv[2]
    outfile_name = argv[3]
    statistics = GetStatsFromFile(user_statistics_file)
    # Write header
    file_to_open = open(outfile_name,'w')
    writer = csv.writer(file_to_open)
    header = ("id","text","author","creation_date", "favorites", \
        "retweets", "upvotes", "average_favorites", "max_favorites", \
        "average_retweets", "max_retweets", "average_upvotes", "max_upvotes",\
        "follower_count", "account_creation_date", "type")
    writer.writerow(header)
    file_to_open.close()
    # Put all tweets in outfile
    for file in os.listdir(tweets_directory):
        # Ignore hidden files or git stuff
        if not file.startswith('.'):
            username = file[:-11].lower()
            user_stats = statistics[username]
            user_info = [username, user_stats[0], user_stats[1]]
            print "Adding new user:", username, "with stats:", user_stats
            infile_name = tweets_directory+file
            ReadAndWriteTweets(infile_name, user_info, outfile_name)
    reddit_jokes = []
    reddit_upvotes = 0
    reddit_max_upvotes = 0
    # Put all reddit jokes in outfile
    for file in os.listdir(reddit_directory):
        # Ignore hidden files or git stuff
        if not file.startswith('.'):
            infile_name = reddit_directory+file
            print "Reading Reddit jokes from:", infile_name
            temp_jokes_list, reddit_upvotes, reddit_max_upvotes \
            = ReadRedditJokes(infile_name, reddit_upvotes, reddit_max_upvotes)
            reddit_jokes += temp_jokes_list
    # Write Reddit jokes to CSV
    # Make averages acutal averages
    average_upvotes = float(reddit_upvotes)/float(len(reddit_jokes))
    file_to_open = open(outfile_name,'a')
    writer = csv.writer(file_to_open)
    # Write all Reddit jokes to outfile
    global id_count
    for joke in reddit_jokes:
        joke_with_stats = joke
        # Update joke to have real stats
        joke_with_stats[0] = id_count
        id_count += 1
        joke_with_stats[11] = average_upvotes
        joke_with_stats[12] = reddit_max_upvotes
        # Write row to CSV
        writer.writerow(joke_with_stats)
    file_to_open.close()

if __name__ == "__main__":
    main(sys.argv[1:])



