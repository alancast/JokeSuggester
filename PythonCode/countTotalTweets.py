import csv
import sys
import os

# Counts the number of tweets (csv rows) in the passed in file
# INPUTS: string of directory name (with /) and string of file name
# RETURNS: Int number of data rows in that file
def CountTweetsFromFile(directory_name, file_name):
    file_loc = directory_name + file_name
    with open(file_loc,"r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)
    # To Remove header row
    row_count -= 1
    print file_loc + " has " + str(row_count) + " tweets."
    return row_count

# Counts the number of data rows (tweets) in an entire directory
# COMMAND LINE ARGS: [directory name (with the /)]
def main(argv):
    directory_name = argv[0]
    total_tweets = 0
    for file in os.listdir(directory_name):
        if not file.startswith('.'):
            total_tweets += CountTweetsFromFile(directory_name, file)
    print "We currently have " + str(total_tweets) + " tweets."

if __name__ == "__main__":
    main(sys.argv[1:])



