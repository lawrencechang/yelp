# Generate a histogram of users, based on scores

import cPickle as pickle;
#import operator;
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

user_scores_filename = "user_scores_sorted.p";
print "Reading "+user_scores_filename;
users_ranked = pickle.load(open(user_scores_filename, 'rb'));
print "Done.";

# Lets say we to get 10 groups
groups = 10;
max_score = users_ranked[0][1];
min_score = users_ranked[len(users_ranked)-1][1];
range = (max_score-min_score) / float(groups);

# Make a histogram of the ranges
dec = [int(x[1]/range) for x in users_ranked];
cnt = Counter(dec);

labels, values = zip(*cnt.items())
indexes = np.arange(len(labels))
width = 1

# Logarithmic scale, remove log to do normal
plt.bar(indexes, values, width);
#plt.bar(indexes, values, width,log=1);
plt.xticks(indexes + width * 0.5, labels);
plt.show();

