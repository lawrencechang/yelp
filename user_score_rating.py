# Read in the user dataset
# 1. User rating correlation
# Get the reviews of this user
# For each review, compare actual rating with user's rating
# Total up the differences squared
# Average for all reviews
# Normalize by 16 to get a value between 0 and 1
# (This is so because the greatest difference between star ratings is 4,
# squared is 16, and average across all reviews, max is 16).

import cPickle as pickle;
import time;

start = time.clock();
print 'Loading users list from users.p file.';
users = pickle.load(open('users.p', 'rb'));

print 'Loading user_to_review_ids list from user_to_review_ids.p file.';
user_to_review_ids = pickle.load(open('user_to_review_ids.p', 'rb'));

print 'Loading reviews list from reviews.p file.';
reviews = pickle.load(open('reviews.p', 'rb'));

print 'Loading businesses list from businesses.p file.';
businesses = pickle.load(open('businesses.p', 'rb'));

elapsed = (time.clock() - start);
print 'All the loading took '+str(elapsed)+' seconds.';

count = 0;
users_score_correlation = {};
for user in users:
	users_reviews = user_to_review_ids[user];
	
	num_reviews = 0;
	total_diff = 0;
	for review_id in users_reviews:
		stars_given = reviews[review_id]['stars'];
		business_id = reviews[review_id]['business_id'];
		stars_business = businesses[business_id]['stars']
		diff_squared = stars_given - stars_business;
		diff_squared *= diff_squared;
		num_reviews += 1;
		total_diff += diff_squared
		
	# Score of 0 is the worst, 1 is the best
	if num_reviews == 0:
		# How are there no reviews for this user? Something went wrong.
		correlation_score = 0;
	else:
		correlation_score = 1.0 - ((total_diff / num_reviews)/16);
	
	users_score_correlation[user] = correlation_score;
	
	count += 1;
	
print 'Done calculating all correlation scores.';
pickle.dump(users_score_correlation, open('users_score_correlation.p', 'wb'));
	
# Some statistics
from collections import Counter;
cnt = Counter(users_score_correlation.values());

# Test output file
scores_loaded = pickle.load(open('users_score_correlation.p', 'rb'));
cnt2 = Counter(scores_loaded.values());

if all(cnt[i] == cnt2[i] for i,x in enumerate(cnt)):
	print 'Test succeeded.';
else:
	print 'Test failed.';
	
# To get a good histogram view...
# sorted(cnt.items(),key=lambda x: x[0])

	
