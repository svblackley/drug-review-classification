#!usr/bin/python

import sys, os, csv, re

def featurize(instance):
    features = []
    

def get_n_grams(instance, n=1):
    

def get_clusters(instance):
    pass

def get_side_effects(instance):
    pass

def get_sentiment(instance):
    pass

def get_metadata(instance):
    pass
    # word count
    # age
    # gender
    # treatment length

def get_ease_prediction(instance):
    pass

def get_effectiveness_prediction(instance):
    pass

def get_satisfiaction_prediction(instance):
    pass





if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if os.path.isfile(input_file):
            with open(input_file, 'rU') as csvfile:
                reader = csv.DictReader(csvfile)
                for instance in reader:
                    featurize(instance)
        else:
            print "Input file does not exist."
    else:
        print "Usage:\nfeaturize.py <input file>"