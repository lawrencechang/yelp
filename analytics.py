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

k = 10

star_total = 0.0
count_total = 0.0


print
print "User Score Weights: %s" % user_score.SCORE_WEIGHTS
print
print "Authorities derived from Top %d Hub Users" % find_authorities.k

print
print "Name\tID\tCount Score\tStars"
k_counter = 0
for auth, count in authorities_sorted:
  if (('Restaurants' not in businesses[auth]['categories']) and
      ('Food' not in businesses[auth]['categories'])):
    continue
  count_total += count
  star_total += float(businesses[auth]['stars'])
  print "%s\t%s\t%s\t%s" % (businesses[auth]['name'], auth,
                            count, businesses[auth]['stars'])
  k_counter += 1;
  if k_counter > k:
    break;

print
print "Average Stars of Top %d: %g" % (k, star_total / k)
print "Average Count Score of Top %d: %g" % (k, count_total / k)
print
