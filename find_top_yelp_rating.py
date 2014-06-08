# Simply sorts all businesses by their rating.
# Flaw is that there are many businesses with the same rating.

import cPickle as pickle;

business_review_ids_filename = "business_to_review_ids.p";
print "Reading "+business_review_ids_filename;
business_to_review_ids = pickle.load(open(business_review_ids_filename, 'rb'));
print "Done.";

businesses = pickle.load(open('businesses.p', 'rb'));

businesses_sorted = sorted(businesses.iteritems(),key=lambda x: x[1]['stars'],reverse=True )

k_counter = 0
total = 10;
print "Straight up rating, top "+str(total);
print "Name\tID\tCity\tCount Score\tStars"
for business_tuple in businesses_sorted:

	business = business_tuple[1];
	if (('Restaurants' not in business['categories']) and
      ('Food' not in business['categories'])):
		continue
    
	print "%s\t%s\t%s\t%s" % (business['name'], business['business_id'],
                                  business['city'], 
                                  business['stars'])

	k_counter += 1
	if (k_counter > total):
  		break;
  		
print
print "Let's put a threshold of review counts, just to help trim the list."
threshold = 500;
print "Threshold of "+str(threshold)+" reviews.";
print "Name\tID\tCity\tCount Score\tStars"
total_count = 0;
counter = 0;
while total_count < total and counter < len(businesses_sorted):
	business_tuple = businesses_sorted[counter];
	business_id = business_tuple[0];
	business = business_tuple[1];
	if (business_to_review_ids.get(business_id) != None
			and
			len(business_to_review_ids[business_id]) >= threshold
			and
			('Restaurants' in business['categories']) 
			and
      		('Food' in business['categories'])
		):
		total_count += 1;
		print "%s\t%s\t%s\t%s" % (business['name'], business['business_id'],
                                  business['city'], 
                                  business['stars'])
	counter += 1;
	