"Compute and pickle the user scores based on number of reviews."

import cPickle as pickle


def get_count_scores():
  '''Get normalized scores for each user in regards review count.

  global:
    user_to_review_ids: {user_id: [review_ids]} - mapping user id to review ids.

  Returns:
    ({user_id: float}) - mapping of a user to the score based on number of
      reviews.
  '''
  count_scores = {}
  for user, review_ids in user_to_review_ids.iteritems():
    count_scores[user] = len(review_ids)

  count_max = float(max(count_scores.itervalues()))
  for user in count_scores:
    count_scores[user] /= count_max

  return count_scores


if __name__ == '__main__':
  user_to_review_ids = pickle.load(open('user_to_review_ids.p', 'rb'))
  count_scores = get_count_scores()
  pickle.dump(count_scores, open('count_scores.p', 'wb'))