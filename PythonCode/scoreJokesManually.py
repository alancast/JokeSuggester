import csv
import sys

# PURPOSE: Prints jokes and allows patrick and I to manually rank them
# COMMAND LINE ARGS: <AMT_csv_file>,
def main(argv):
    if len(argv) < 1:
        print "ABORTING: Need command line argument: <AMT_csv_file>"
        exit(1)
    person = raw_input('Enter a \'p\' if you\'re patrick: ')
    # Alex's score row
    row_to_update = 19
    # Pat's score row
    if person == 'p':
        row_to_update = 20
    AMT_csv_file = argv[0]
    # List of all jokes
    all_results = []
    # Read in all rows into list
    with open(AMT_csv_file, 'rb') as csv_infile:
        # Skip header
        csv_infile.next()
        csvreader = csv.reader(csv_infile)
        # Read every row and add data as needed
        for row in csvreader:
            # Add this result to the list of all results
            all_results.append(row)
        csv_infile.close()
    print "There are: " + str(len(all_results)) + " results (should be 250)"
    # Write header
    file_to_open = open(AMT_csv_file,'w')
    writer = csv.writer(file_to_open)
    header = ("id","text","author","creation_date", "favorites", \
        "retweets", "upvotes", "average_favorites", "max_favorites", \
        "average_retweets", "max_retweets", "average_upvotes", "max_upvotes",\
        "follower_count", "account_creation_date", "type", "answer1",\
        "answer2", "answer3", "alex_score", "pat_score", "average")
    writer.writerow(header)
    file_to_open.close()
    # Write randomly selected jokes to output CSV
    file_to_open = open(AMT_csv_file,'a')
    writer = csv.writer(file_to_open)
    input_char = 'p'
    for result in all_results:
        print result[1]
        if input_char != 'q':
            input_char = raw_input('Enter your score (-2,-1,0,1,2) or s to skip (if already rated) or q to quit: ')
        if input_char == 's' or input_char == 'q':
            writer.writerow(result)
        elif input_char == '-2':
            result[row_to_update] = -2
            average = float(result[16]) + float(result[17]) + float(result[18])
            average += float(result[19]) + float(result[20])
            average /= 5.0
            result[21] = average
            writer.writerow(result)
        elif input_char == '-1':
            result[row_to_update] = -1
            average = float(result[16]) + float(result[17]) + float(result[18])
            average += float(result[19]) + float(result[20])
            average /= 5.0
            result[21] = average
            writer.writerow(result)
        elif input_char == '0':
            result[row_to_update] = 0
            average = float(result[16]) + float(result[17]) + float(result[18])
            average += float(result[19]) + float(result[20])
            average /= 5.0
            result[21] = average
            writer.writerow(result)
        elif input_char == '1':
            result[row_to_update] = 1
            average = float(result[16]) + float(result[17]) + float(result[18])
            average += float(result[19]) + float(result[20])
            average /= 5.0
            result[21] = average
            writer.writerow(result)
        elif input_char == '2':
            result[row_to_update] = 2
            average = float(result[16]) + float(result[17]) + float(result[18])
            average += float(result[19]) + float(result[20])
            average /= 5.0
            result[21] = average
            writer.writerow(result)
    file_to_open.close()

if __name__ == "__main__":
    main(sys.argv[1:])



