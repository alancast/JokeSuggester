import csv
import sys
import random

# PURPOSE: Reads in AMT results and writes them in a format we can use
# COMMAND LINE ARGS: <AMT_input_file>,
#                    <outfile_name>
def main(argv):
    if len(argv) < 2:
        print "ABORTING: Need 2 command line arguments: <AMT_input_file> <outfile_name>"
        exit(1)
    AMT_file = argv[0]
    outfile_name = argv[1]
    # Write header
    file_to_open = open(outfile_name,'w')
    writer = csv.writer(file_to_open)
    header = ("id","text","author","creation_date", "favorites", \
        "retweets", "upvotes", "average_favorites", "max_favorites", \
        "average_retweets", "max_retweets", "average_upvotes", "max_upvotes",\
        "follower_count", "account_creation_date", "type", "answer1",\
        "answer2", "answer3", "alex_score", "pat_score", "average")
    writer.writerow(header)
    file_to_open.close()
    # List of AMT results
    AMT_results = []
    # Read in all rows into list
    with open(AMT_file, 'rb') as csv_infile:
        # Skip header
        csv_infile.next()
        csvreader = csv.reader(csv_infile)
        # Read every row and add data as needed
        for row in csvreader:
            # Add only the columns we are interested in
            data_needed = row[1:17]
            data_needed.append(row[18])            
            data_needed.append(row[20])
            data_needed.append(row[22])
            # Alex Score
            data_needed.append(0)
            # Pat Score
            data_needed.append(0)
            # Average
            data_needed.append(0.0)
            AMT_results.append(data_needed)
        csv_infile.close()
    # Write restuls to output file
    file_to_open = open(outfile_name,'a')
    writer = csv.writer(file_to_open)
    for result in AMT_results:
        writer.writerow(result)
    file_to_open.close()

if __name__ == "__main__":
    main(sys.argv[1:])



