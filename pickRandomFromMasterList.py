import csv
import sys
import random

# PURPOSE: Randomly select x amount of jokes from MasterList and
#           output them as a CSV
# COMMAND LINE ARGS: <master_list_file>,
#                    <outfile_name>,
def main(argv):
    if len(argv) < 2:
        print "ABORTING: Need 2 command line arguments: <master_list_file> <outfile_name>"
        exit(1)
    master_list_file = argv[0]
    outfile_name = argv[1]
    # Write header
    file_to_open = open(outfile_name,'w')
    writer = csv.writer(file_to_open)
    header = ("id","text","author","creation_date", "favorites", \
        "retweets", "upvotes", "average_favorites", "max_favorites", \
        "average_retweets", "max_retweets", "average_upvotes", "max_upvotes",\
        "follower_count", "account_creation_date", "type")
    writer.writerow(header)
    file_to_open.close()
    how_many_jokes = 5
    # List of all jokes
    all_jokes = []
    # Read in all rows into list
    with open(master_list_file, 'rb') as csv_infile:
        # Skip header
        csv_infile.next()
        csvreader = csv.reader(csv_infile)
        # Read every row and add data as needed
        for row in csvreader:
            # Add this joke to the list of all jokes
            all_jokes.append(row)
        csv_infile.close()
    # Create random joke list
    random_jokes = random.sample(all_jokes, how_many_jokes)
    # Write randomly selected jokes to output CSV
    file_to_open = open(outfile_name,'a')
    writer = csv.writer(file_to_open)
    for joke in random_jokes:
        writer.writerow(joke)
    file_to_open.close()

if __name__ == "__main__":
    main(sys.argv[1:])



