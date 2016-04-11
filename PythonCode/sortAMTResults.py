import sys
import csv
import operator
import codecs

# Creates a list of lists of the AMT results
# INPUTS: 
#       file - AMTResults list csv
# RETURNS: 
#       results_info - list of lists of the AMT results
def read_in_rankings(file):
    results_info = []
    with codecs.open(file) as f:
        # Skip header
        f.next()
        reader = csv.reader(f)
        for row in reader:
            results_info.append(row)
        f.close()
    return results_info

# Prints the output needed for sorted AMT results
# Takes in output filename and list of scores
def print_output(file, results_info):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        header = ("id","text","author","creation_date", "favorites", \
        "retweets", "upvotes", "average_favorites", "max_favorites", \
        "average_retweets", "max_retweets", "average_upvotes", "max_upvotes",\
        "follower_count", "account_creation_date", "type", "answer1",\
        "answer2", "answer3", "alex_score", "pat_score", "average")
        writer.writerow(header)
        for result in results_info:
            writer.writerow(result)
        f.close()

def rankings_comparator(a, b):
    if float(a[-1]) > float(b[-1]):
        return -1
    else:
        return 1

# PURPOSE: Read in AMT results and sort them by highest average score
#           output them as a CSV
# COMMAND LINE ARGS: <amt_results_file>,
#                    <outfile_name>
def main(argv):
    if len(argv) < 2:
        print "ABORTING: requires 2 command line arguments :"
        print "<amt_results_file> <output_file>"
        exit(1)
    # Parse input file
    amt_results_file = argv[0]
    print "Reading in AMT results"
    results_info = read_in_rankings(amt_results_file)
    # Sort all jokes/scores
    print "Sorting all results"
    results_info.sort(rankings_comparator)
    # Write output to file
    print "Writing output"
    output_path = argv[1]
    print_output(output_path, results_info)
    
if __name__ == "__main__":
   main(sys.argv[1:])






