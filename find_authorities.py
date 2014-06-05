# This script will find the authority restaurants
# The authority restaurant is defined as restaurants who most "hub" users
# have gone to.
# We define "hubs" as the top k users, ranked by our scoring algorithm.

import cPickle as pickle;
import operator;
import os.path

k = 300;

if __name__ == '__main__':
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


  if not os.path.isfile('review_ids_to_businesses.p'):
    reviews_filename = "reviews.p";
    print "Reading "+reviews_filename;
    reviews = pickle.load(open(reviews_filename, 'rb'));
    print "Done.";
    review_ids_to_businesses = []

    for review in reviews:
      review_ids_to_businesses.append((review['business_id'],
                                       float(review['stars'])))
    pickle.dump(review_ids_to_businesses,
                open('review_ids_to_businesses.p', 'wb'))

  # [(business_id, star_rating)]
  review_ids_to_businesses = pickle.load(open('review_ids_to_businesses.p', 'rb'))


  # For each user, add to dictionary of <business_id,matches>
  authorities = {};
  count = 0;
  for user in users_ranked:
    user_id = user[0];
    for review_id in user_to_review_ids[user_id]:
      business_id = review_ids_to_businesses[review_id][0]
      star_rating = review_ids_to_businesses[review_id][1]

      if authorities.get(business_id) == None:
        authorities[business_id] = (star_rating - 1) / 4.0;
      else:
        authorities[business_id] += (star_rating - 1) / 4.0;
        #print "Got a multiple!";

    count += 1;
    if count >= k:
      break;

  sorted_tuple = sorted(authorities.iteritems(),key=operator.itemgetter(1),reverse=True);

  print "Using top %d hub users:" % k
  print "Top 10 restaurants, with highest correlation among users:";
  print str(sorted_tuple[0:10]);

  pickle.dump(sorted_tuple, open('authorities_sorted.p', 'wb'))