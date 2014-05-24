"Compute and pickle the final user scores based on multiple factors."

import cPickle as pickle
import operator

SCORE_WEIGHTS = {
  'latest_scores': 0.2,
  'age_scores': 0.2,
  'count_scores' : 0.2,
  'correlation_scores': 0.2,
  'upvote_scores': 0.2
}


def get_user_scores():
  '''Combines user score factors with weights to compute final user score.

  Returns:
    ({user_id: float}, [(user_id, float)]) - a mapping of users to their score
      and a list of users and score pairs sorted by their score in descending
      order.
  '''
  user_scores = {}

  for user in count_scores:
    user_scores[user] = (
      (SCORE_WEIGHTS['latest_scores'] * latest_scores[user]) +
      (SCORE_WEIGHTS['age_scores'] * age_scores[user]) +
      (SCORE_WEIGHTS['count_scores'] * count_scores[user]) +
      (SCORE_WEIGHTS['correlation_scores'] * correlation_scores[user]) +
      (SCORE_WEIGHTS['upvote_scores'] * upvote_scores[user]))

  user_scores_sorted = sorted(user_scores.iteritems(),
                              key=operator.itemgetter(1),
                              reverse=True)

  return (user_scores, user_scores_sorted)


if __name__ == '__main__':
  count_scores = pickle.load(open('count_scores.p', 'rb'))
  latest_scores = pickle.load(open('latest_scores.p', 'rb'))
  age_scores = pickle.load(open('age_scores.p', 'rb'))
  correlation_scores = pickle.load(open('users_score_correlation.p', 'rb'))
  upvote_scores = pickle.load(open('users_score_upvotes.p', 'rb'))

  (user_scores, user_scores_sorted) = get_user_scores()
  print "Top 10 users:"
  print str(user_scores_sorted[:10])

  pickle.dump(user_scores, open('user_scores.p', 'wb'))
  pickle.dump(user_scores_sorted, open('user_scores_sorted.p', 'wb'))