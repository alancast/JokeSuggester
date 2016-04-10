import sys
import csv
import operator
import codecs
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.externals import joblib

# Takes in input of training or dev file and parses it
# RETURNS: target (nparray of floats) and data (list of strings)
def parse_training_file(file):
    target = []
    data = []
    with codecs.open(file) as f:
        # Skip header
        f.next()
        reader = csv.reader(f)
        for row in reader:
            target.append(int(row[0]))
            data.append(row[1].decode('iso-8859-1').encode('utf8'))
        f.close()
    target = np.array(target)
    return target, data

# PURPOSE: Creates a rankings model for how funny our jokes are
#           Saves the model file in a specified location
# COMMAND LINE ARGS: <training_file>,
#                    <outfile_name>
def main(argv):
    if len(argv) < 2:
        print "ABORTING: Requires 2 command line arguments:"
        print "<training_path_file> <output_path_file>"
        exit(1)
    training_path = argv[0]
    training_target, training_data = parse_training_file(training_path)
    # Pipeline to make testing combinations of parameters for models easier
    text_clf_svm = Pipeline([('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('clf', LinearSVC())])
    # Grid search to find best combination of parameters for each
    parameters = {'vect__ngram_range': [(1, 1), (1, 2), (1,3)],
                    'tfidf__use_idf': (True, False),
                    # 'clf__n_iter': (10, 50, 80),
                    'vect__max_df': (0.5, 0.75, 1.0),
                    'vect__max_features': (None, 5000, 10000, 50000)}
    # Train SVM grid serach
    print "Starting grid search SVM"
    gs_clf_svm = GridSearchCV(text_clf_svm, parameters, n_jobs=-1)
    print "Starting grid search fit SVM"
    # Will currently break because trying to classify into float (not really bins)
    gs_clf_svm = gs_clf_svm.fit(training_data[:400], training_target[:400])
    # Save model to disk
    print "Saving output path"
    output_path = argv[1]
    joblib.dump(gs_clf_svm, output_path) 
    
if __name__ == "__main__":
   main(sys.argv[1:])