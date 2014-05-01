# Read in the user dataset
# 1. User rating correlation
# Get the reviews of this user

import cPickle as pickle;
import time;

start = time.clock();
print 'Loading user list from users.p file.';
users = pickle.load(open('users.p', 'rb'));
print 'Finished loading user list.';

print 'Loading user_to_review_ids list from user_to_review_ids.p file.';
user_to_review_ids = pickle.load(open('user_to_review_ids.p', 'rb'));
print 'Finished loading user_to_review_ids list.';

print 'Loading review list from reviews.p file.';
reviews = pickle.load(open('reviews.p', 'rb'));
print 'Finished loading reviews list.';

elapsed = (time.clock() - start);
print 'All the loading took '+str(elapsed)+' seconds.';

count = 0;
for user in users:
	print users[user];
	users_reviews = user_to_review_ids[user]; # This is a list
	for review_id in users_reviews:
		print review_id;
		print reviews[review_id];
	if count > 5:
		break;
	count += 1;
	
	

