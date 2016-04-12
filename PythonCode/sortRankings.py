import sys
import csv
import operator
import codecs

# Creates a list of lists from ranking
# INPUTS: 
#       file - rankings list csv
# RETURNS: 
#       ranking_info - list of lists of ranking info
def read_in_rankings(file):
    ranking_info = []
    with codecs.open(file) as f:
        # Skip header
        f.next()
        reader = csv.reader(f)
        for row in reader:
            ranking_info.append(row)
        f.close()
    return ranking_info

# Prints the output needed for sorted rankings
# Takes in output filename and list of scores
def print_output(file, ranking_info):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        header = ("id","ranking_score","text","author")
        writer.writerow(header)
        for joke in ranking_info:
            writer.writerow(joke)
        f.close()

def rankings_comparator(a, b):
    if float(a[1]) > float(b[1]):
        return -1
    else:
        return 1

# PURPOSE: Read in rankings and sort them
#           output them as a CSV
# COMMAND LINE ARGS: <rankings_file>,
#                    <outfile_name>
def main(argv):
    if len(argv) < 2:
        print "ABORTING: requires 2 command line arguments :"
        print "<master_list_file> <output_file>"
        exit(1)
    # Parse input file
    rankings_file = argv[0]
    print "Reading in rankings"
    ranking_info = read_in_rankings(rankings_file)
    # Sort all jokes/scores
    print "Sorting all scores"
    ranking_info.sort(rankings_comparator)
    # Write output to file
    print "Writing output"
    output_path = argv[1]
    print_output(output_path, ranking_info)
    
if __name__ == "__main__":
   main(sys.argv[1:])






