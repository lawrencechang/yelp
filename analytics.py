import cPickle as pickle
import os
import find_authorities
import user_score

# Update hubs and authorities
print "Updating user scores..."
os.system("python ./user_score.py")
print "Updating authorities..."
os.system("python ./find_authorities.py")

print "Getting analytics..."
authorities_sorted = pickle.load(open('authorities_sorted.p', 'rb'))
businesses = pickle.load(open('businesses.p', 'rb'))
business_to_review_ids = pickle.load(open('business_to_review_ids.p', 'rb'))

# k authorities
top_auth_k = 10
# k used to find hidden gems
top_k_for_hidden = 50
# k hidden gems
hidden_k = 10
top_k_auth = []




print
print ("User Score Weights: Latest = %g, Age = %g, Count = %g, "
       "Correlation = %g, Upvote = %g" % (
        user_score.SCORE_WEIGHTS['latest_scores'],
        user_score.SCORE_WEIGHTS['age_scores'],
        user_score.SCORE_WEIGHTS['count_scores'],
        user_score.SCORE_WEIGHTS['correlation_scores'],
        user_score.SCORE_WEIGHTS['upvote_scores']))

print
print "Authorities derived from Top %d Hub Users" % find_authorities.k

print
print "Name\tID\tCount Score\tStars"
star_total = 0.0
count_total = 0.0
k_counter = 0
for auth, count in authorities_sorted:
  if k_counter > max(top_auth_k, top_k_for_hidden):
    break

  if (('Restaurants' not in businesses[auth]['categories']) and
      ('Food' not in businesses[auth]['categories'])):
    continue

  if k_counter < top_k_for_hidden:
    top_k_auth.append((auth, count))

  if k_counter < top_auth_k:
    count_total += count
    star_total += float(businesses[auth]['stars'])
    print "%s\t%s\t%s\t%s" % (businesses[auth]['name'], auth,
                              count, businesses[auth]['stars'])

  k_counter += 1


print
print "Average Stars of Top %d Auth: %g" % (top_auth_k,
                                            star_total / top_auth_k)
print "Average Count Score of Top %d Auth: %g" % (top_auth_k,
                                                  count_total / top_auth_k)
print

hidden_sorted = sorted(top_k_auth,
                       key=lambda (auth, _): len(business_to_review_ids[auth]))

print
print "Hidden Gems based on Top %d Auth" % top_k_for_hidden
print
print "Name\tID\tCount Score\tStars\tReview Count"
star_total = 0.0
count_total = 0.0
k_counter = 0
for auth, count in hidden_sorted:
  count_total += count
  star_total += float(businesses[auth]['stars'])
  print "%s\t%s\t%s\t%s\t%s" % (businesses[auth]['name'], auth,
                            count, businesses[auth]['stars'],
                            len(business_to_review_ids[auth]))

  k_counter += 1
  if k_counter >= hidden_k:
    break

print
print "Average Stars of Top %d Hidden Gems: %g" % (hidden_k,
                                                   star_total / hidden_k)
print "Average Count Score of Top %d Hidden Gems: %g" % (hidden_k,
                                                         count_total / hidden_k)
print