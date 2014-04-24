# This file is meant to learn the basics of json parsing with python.

import json;

num_lines = 0;
with open('../yelp_academic_dataset.json') as yelp_file:
    for line in yelp_file:
        num_lines += 1;
        #print line;
    print 'Number of lines: '+str(num_lines);
    #yelp_data = json.load(yelp_file);
    
