import sys
import csv
import codecs
import pprint
import scipy.stats as st

# Creates a list of lists from ranking
# INPUTS: 
#       file - rankings list csv
# RETURNS: 
#       ranking_info - list of id's in rank order
#       rankings_dict - dictionary with all id's in ranking_info
def read_in_amt_rankings(file):
    ranking_info = []
    rankings_dict = {}
    with codecs.open(file) as f:
        # Skip header
        f.next()
        reader = csv.reader(f)
        for row in reader:
            ranking_info.append(row[0])
            rankings_dict[row[0]] = 1
        f.close()
    return ranking_info, rankings_dict

# Creates a list of lists from ranking
# INPUTS: 
#       file - rankings list csv
#       rankings_dict - dictionary with all id's in ranking_info
# RETURNS: 
#       ranking_info - list of id's in rank order
def read_in_our_rankings(file, rankings_dict):
    ranking_info = []
    with codecs.open(file) as f:
        # Skip header
        f.next()
        reader = csv.reader(f)
        for row in reader:
            if row[0] in rankings_dict:
                ranking_info.append(row[0])
        f.close()
    return ranking_info

# PURPOSE: Compute Kendall Tau agreement score between AMT and our ranking model
# COMMAND LINE ARGS: <amt_file>,
#                    <rankings_file>
def main(argv):
    if len(argv) < 2:
        print "ABORTING: requires 2 command line arguments :"
        print "<amt_file> <rankings_file>"
        exit(1)
    # Parse rankings files
    amt_file = argv[0]
    amt_ranking_info, rankings_dict = read_in_amt_rankings(amt_file)
    rankings_file = argv[1]
    our_ranking_info = read_in_our_rankings(rankings_file, rankings_dict)
    # pprint.pprint(amt_ranking_info)
    # pprint.pprint(our_ranking_info)
    # Compute Kendall Tau
    print "Computing Kendall Tau"
    print "------------------------------------------------------\n\n"
    tau, p_value = st.kendalltau(amt_ranking_info, our_ranking_info)
    # tau, p_value = st.kendalltau(amt_ranking_info, amt_ranking_info)
    print "\n\n------------------------------------------------------"
    print "Kendall Tau score is:", tau
    
if __name__ == "__main__":
   main(sys.argv[1:])






