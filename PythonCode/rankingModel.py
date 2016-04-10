import sys
import csv
import operator
import codecs

# Creates a list of info needed for all the jokes in the master list
# INPUTS: 
#       file - master list csv
# RETURNS: 
#       master_info - list of lists of info on that joke
#                       format = [[joke],[joke2],...]
def create_master_info(file):
    master_info = []
    with codecs.open(file) as f:
        # Skip header
        f.next()
        reader = csv.reader(f)
        for row in reader:
            master_info.append(row)
        f.close()
    return master_info

# Creates a list of tuples of all jokes. Format = (id,score)
# INPUTS: 
#       master_info - list of lists of all jokes and info
# RETURNS: 
#       scores_list - list of tuples of (joke, score)
def score_all(master_info):
    scores_list = []
    for joke in master_info:
        twitter_score = 0.0
        reddit_score = 0.0
        # Twitter joke
        if int(joke[-1]) == 0:
            twitter_score = compute_twitter_score(joke)
        # Reddit joke
        elif int(joke[-1]) == 1:
            reddit_score = compute_reddit_score(joke)
        joke_score = (.6*reddit_score) + (.4*twitter_score)
        scores_list.append((joke[0], joke_score))
    return scores_list

# Computes the twitter score of the passed in joke
# INPUTS: 
#       joke - list of info needed for the joke
# RETURNS: 
#       score - float with the twitter score of the joke
def compute_twitter_score(joke):
    score = 0.0
    favorites = int(joke[4])
    retweets = int(joke[5])
    average_favorites = float(joke[7])
    max_favorites = int(joke[8])
    average_retweets = float(joke[9])
    max_retweets = int(joke[10])
    follower_count = int(joke[13])
    score += (float(favorites)/average_favorites) + (float(retweets)/average_retweets)
    if favorites == max_favorites:
        score += 1.0
    if retweets == max_retweets:
        score += 1.0
    return score

# Computes the reddit score of the passed in joke
# INPUTS: 
#       joke - list of info needed for the joke
# RETURNS: 
#       score - float with the reddit score of the joke
def compute_reddit_score(joke):
    score = 0.0
    score = 0.0
    upvotes = int(joke[6])
    average_upvotes = float(joke[11])
    max_upvotes = int(joke[12])
    score += (float(upvotes)/average_upvotes)
    if upvotes == max_upvotes:
        score += 1.0
    return score

# Prints the output needed for rankings
# Takes in output filename and list of scores
def print_output(file, scores_list):
    with open(file, 'w') as f:
        fieldnames = ['id', 'ranking_score']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for joke in scores_list:
            writer.writerow({'id': joke[0], 'ranking_score': joke[1]})
        f.close()

# PURPOSE: Load in saved rankings model, and rank all jokes from it
#           output them as a CSV
# COMMAND LINE ARGS: <test_path_file> (master csv list),
#                    <outfile_name>
def main(argv):
    if len(argv) < 2:
        print "ABORTING: requires 2 command line arguments :"
        print "<master_list_file> <output_file>"
        exit(1)
    # Parse input file
    master_file = argv[0]
    print "Creating master dictionary"
    master_info = create_master_info(master_file)
    # Score all jokes
    print "Scoring all items"
    scores_list = score_all(master_info)
    # Write output to file
    print "Writing output"
    output_path = argv[1]
    print_output(output_path, scores_list)
    
if __name__ == "__main__":
   main(sys.argv[1:])






