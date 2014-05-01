Yelp
====

Yelp graph characterization project for CS 246 Web Info Management with Junghoo Cho, at UCLA


Pickle Contents after running mappings.py

business_to_review_ids.p = dictionary
business id -> [review id] list

user_to_review_ids.p = dictionary
user id -> [review_id] list

businesses.p = dictionary
business id ->
  {
    'type': 'business',
    'business_id': (a unique identifier for this business),
    'name': (the full business name),
    'neighborhoods': (a list of neighborhood names, might be empty),
    'full_address': (localized address),
    'city': (city),
    'state': (state),
    'latitude': (latitude),
    'longitude': (longitude),
    'stars': (star rating, rounded to half-stars),
    'review_count': (review count),
    'photo_url': (photo url),
    'categories': [(localized category names)]
    'open': (is the business still open for business?),
    'schools': (nearby universities),
    'url': (yelp url)
  }

reviews.p = list
review id is the list index
  {
    'type': 'review',
    'business_id': (the identifier of the reviewed business),
    'user_id': (the identifier of the authoring user),
    'stars': (star rating, integer 1-5),
    'text': (review text),
    'date': (date, formatted like '2011-04-19'),
    'votes': {
      'useful': (count of useful votes),
      'funny': (count of funny votes),
      'cool': (count of cool votes)
    }
  }

users.p = dictionary
user id ->
  {
    'type': 'user',
    'user_id': (unique user identifier),
    'name': (first name, last initial, like 'Matt J.'),
    'review_count': (review count),
    'average_stars': (floating point average, like 4.31),
    'votes': {
      'useful': (count of useful votes across all reviews),
      'funny': (count of funny votes across all reviews),
      'cool': (count of cool votes across all reviews)
    }
  }