# This script will find the authority restaurants
# The authority restaurant is defined as restaurants who most "hub" users
# have gone to.
# We define "hubs" as the top k users, ranked by our scoring algorithm.

import cPickle as pickle;
import operator;

k = 100;

user_scores_filename = "user_scores_sorted.p";
print "Reading "+user_scores_filename;
users_ranked = pickle.load(open(user_scores_filename, 'rb'));
print "Done.";

user_review_ids_filename = "user_to_review_ids.p";
print "Reading "+user_review_ids_filename;
user_to_review_ids = pickle.load(open(user_review_ids_filename, 'rb'));
print "Done.";

#business_review_ids_filename = "business_to_review_ids.p";
#print "Reading "+business_review_ids_filename;
#business_to_review_ids = pickle.load(open(business_review_ids_filename, 'rb'));
#print "Done.";

reviews_filename = "reviews.p";
print "Reading "+reviews_filename;
reviews = pickle.load(open(reviews_filename, 'rb'));
print "Done.";


# For each user, add to dictionary of <business_id,matches>
authorities = {};
count = 0;
for user in users_ranked:
	user_id = user[0];
	for review_id in user_to_review_ids[user_id]:
		business_id = reviews[review_id]['business_id'];
		if authorities.get(business_id) == None:
			authorities[business_id] = 1;
		else:
			authorities[business_id] += 1;
			#print "Got a multiple!";
			
	count += 1;
	if count > k:
		break;
		
sorted_tuple = sorted(authorities.iteritems(),key=operator.itemgetter(1),reverse=True);

print "Top 10 restaurants, with highest correlation among users:";
print str(sorted_tuple[0:10]);

