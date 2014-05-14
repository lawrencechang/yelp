"Compute and pickle the user scores based on temporal review factors."

import cPickle as pickle
import datetime


def get_days_since_review(review_id):
  '''Returns the number of days elapsed since review with given id.

  global:
    current_date: datetime object - the date to subtract from.
    reviews: [review data] - list of reviews.

  Args:
    review_id: str - the index id of a review in the reviews list.

  Returns:
    int - days from the review date to the current date.
  '''
  review_date = datetime.datetime.strptime(reviews[review_id]['date'],
                                           '%Y-%m-%d')
  return (current_date - review_date).days


def get_oldest_and_youngest_elapsed():
  '''Number of days since oldest and most recent reviews from all users.

  global:
    current_date: datetime object - the date to subtract from.
    reviews: [review data] - list of reviews.
    user_to_review_ids: {user_id: [review_ids]} - mapping user id to review ids.

  Returns:
    ({user_id: int}, {user_id: int}) - mapping of a user to the number of days
      since their oldest review and their most recent review.
  '''
  oldest_per_user = {}
  youngest_per_user = {}

  for user in user_to_review_ids:
    # Could implement max and min together to avoid two iterations.
    max_days_review_id = max(user_to_review_ids[user],
                             key=get_days_since_review)
    min_days_review_id = min(user_to_review_ids[user],
                             key=get_days_since_review)
    oldest_per_user[user] = get_days_since_review(max_days_review_id)
    youngest_per_user[user] = get_days_since_review(min_days_review_id)

  return (oldest_per_user, youngest_per_user)


def get_latest_and_age_scores(oldest_per_user, youngest_per_user):
  '''Get normalized scores for each user in regards of latest review and oldest.

  global:
    current_date: datetime object - the date to subtract from.
    reviews: [review data] - list of reviews.
    user_to_review_ids: {user_id: [review_ids]} - mapping user id to review ids.

  Args:
    oldest_per_user: {user_id: int} - user id to days since latest review.
    youngest_per_user: {user_id: int} - user id to days since oldest review.

  Returns:
    ({user_id: float}, {user_id: float}) - mappings of users to the scores based
      on temporal data.
  '''
  num_users = len(oldest_per_user)
  latest_average = sum(youngest_per_user.itervalues()) / float(num_users)
  age_average = sum(oldest_per_user.itervalues()) / float(num_users)
  latest_min = min(youngest_per_user.itervalues())
  age_max = max(oldest_per_user.itervalues())

  latest_scores = {}
  age_scores = {}

  for user in oldest_per_user:
    latest_score = max(latest_average - youngest_per_user[user], 0)
    latest_scores[user] = latest_score / float(latest_average - latest_min)

    age_score = max(oldest_per_user[user] - age_average, 0)
    age_scores[user] = age_score / float(age_max - age_average)

  return (latest_scores, age_scores)


if __name__ == '__main__':
  current_date = datetime.datetime.today()

  reviews = pickle.load(open('reviews.p', 'rb'))
  user_to_review_ids = pickle.load(open('user_to_review_ids.p', 'rb'))

  oldest_per_user, youngest_per_user = get_oldest_and_youngest_elapsed()
  latest_scores, age_scores = (
    get_latest_and_age_scores(oldest_per_user, youngest_per_user))

  pickle.dump(latest_scores, open('latest_scores.p', 'wb'))
  pickle.dump(age_scores, open('age_scores.p', 'wb'))