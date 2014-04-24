import cPickle as pickle
import json

def pickle_mappings(data_filename):
  businesses = {}
  users = {}
  reviews = []
  review_id = 0
  user_to_review_ids = {}
  business_to_review_ids ={}


  with open(data_filename, 'r') as yelp_file:
    for line in yelp_file:
      data = json.loads(line)

      if data['type'] == 'business':
        businesses[data['business_id']] = data
      elif data['type'] == 'user':
        users[data['user_id']] = data
      elif data['type'] == 'review':
        reviews.append(data)
        user_to_review_ids.setdefault(data['user_id'], []).append(review_id)
        business_to_review_ids.setdefault(data['business_id'],
                                          []).append(review_id)
        review_id += 1

  print "Num of Businesses: %d" % len(businesses)
  print "Num of Users: %d" % len(users)
  print "Num of Reviews: %d" % len(reviews)

  pickle.dump(businesses, open('businesses.p', 'wb'))
  pickle.dump(users, open('users.p', 'wb'))
  pickle.dump(reviews, open('reviews.p', 'wb'))
  pickle.dump(user_to_review_ids, open('user_to_review_ids.p', 'wb'))
  pickle.dump(business_to_review_ids, open('business_to_review_ids.p', 'wb'))

if __name__ == '__main__':
  data_filename = '../yelp_academic_dataset.json'
  pickle_mappings(data_filename)