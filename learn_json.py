# This file is meant to learn the basics of json parsing with python.

import json;

num_lines = 0;
yelp_data = [];
filename = '../yelp_academic_dataset.json'

print 'Loading '+filename+' ...';

with open(filename) as yelp_file:
    for line in yelp_file:
        num_lines += 1;
        #print line;
        yelp_data.append(json.loads(line));
    print 'Number of lines: '+str(num_lines);
    
    
    
