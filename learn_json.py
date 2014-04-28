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
    
# Find how many users there are
num_users = 0;
for line in yelp_data:
    if line['type'] == 'user':
        num_users += 1;
print 'Number of users: '+str(num_users);

# Num businesses
num_businesses = 0;
for line in yelp_data:
    if line['type'] == 'business':
        num_businesses += 1;
print 'Number of businesses: '+str(num_businesses);

# Num reviews
num_reviews = 0;
for line in yelp_data:
    if line['type'] == 'review':
        num_reviews += 1;
print 'Number of reviews: '+str(num_reviews);

# Checking to see how the user data is formed
# Is the funny, useful, and cool counts already incorporated? Each user seems to have fields for them...
# yelp_data[100000] is a user with 6 reviews, some counts for funny useful and cool
my_user = yelp_data[100000]['user_id'];
for line in yelp_data:
    if line['type'] == 'review' and line['user_id'] == my_user:
        print line;
        
        
