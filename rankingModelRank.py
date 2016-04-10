import sys
import csv
import operator

from sklearn.externals import joblib

# Takes in input of training or dev file and parses it
# RETURNS list of ID's and the data of the test instances
def parse_test_file(file):
    # List of ID's for every joke
    ids = []
    data = []
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            ids.append(int(row[0]))
            data.append(row[1].decode('iso-8859-1').encode('utf8'))
        f.close()
    return ids, data

# Prints the output needed for rankings
# Takes in output filename, id's, and predicted rankings
def print_output(file, ids, rankings):
    with open(file, 'w') as f:
        fieldnames = ['ID', 'RankingScore']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(ids)):
            writer.writerow({'ID': ids[i], 'RankingScore': rankings[i]})
        f.close()

# PURPOSE: Load in saved rankings model, and rank all jokes from it
#           output them as a CSV
# COMMAND LINE ARGS: <model_file>,
#                    <test_path_file> (master csv list),
#                    <outfile_name>
def main(argv):
    if len(argv) < 3:
        print "ABORTING: requires 3 command line arguments :"
        print "<model_file> <test_path_file> <output_file>"
        exit(1)
    # Load in model
    model_file = argv[0]
    clf = joblib.load(model_file)
    # Parse then predict test data
    test_path = argv[1]
    ids, test_data = parse_test_file(test_path)
    predicted_rankings = clf.predict(test_data)
    # Write output to file
    output_path = argv[2]
    print_output(output_path, ids, predicted_rankings)
    
if __name__ == "__main__":
   main(sys.argv[1:])






