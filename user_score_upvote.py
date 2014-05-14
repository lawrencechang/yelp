# 2. User's average upvotes
# Get list of users
#   For each, get all reviews
#   For each review
#     Add up the upvotes
#   save total

import cPickle as pickle;
import time;

start = time.clock();
print 'Loading users list from users.p file.';
users = pickle.load(open('users.p', 'rb'));

print 'Loading user_to_review_ids list from user_to_review_ids.p file.';
user_to_review_ids = pickle.load(open('user_to_review_ids.p', 'rb'));

print 'Loading reviews list from reviews.p file.';
reviews = pickle.load(open('reviews.p', 'rb'));

elapsed = (time.clock() - start);
print 'All the loading took '+str(elapsed)+' seconds.';

users_score_upvotes = {};
count = 0;
most_upvotes = 0;
for user in users:
	users_reviews = user_to_review_ids[user];
	
	upvotes = 0;
	for review_id in users_reviews:
		upvotes = (reviews[review_id]['votes']['useful']
			     + reviews[review_id]['votes']['funny']
			     + reviews[review_id]['votes']['cool']);
	
	if upvotes > most_upvotes:
		most_upvotes = upvotes;
	
	users_score_upvotes[user] = upvotes;

	count += 1;
	
	# Debug
	# print 'user: '+user+' upvotes: '+str(upvotes);
	#if count > 10:
	#	break;
	
# Normalize values to most_upvotes, all values will go from 0 to 1
most_upvotes *= 1.0;
users_score_upvotes_normalized = {}
for user in users_score_upvotes:
	users_score_upvotes_normalized[user] = users_score_upvotes[user] / most_upvotes;

print 'Done calculating all upvotes scores.';
pickle.dump(users_score_upvotes_normalized, open('users_score_upvotes.p', 'wb'));


	