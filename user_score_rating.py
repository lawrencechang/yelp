# Read in the user dataset
# 1. User rating correlation
# Get the reviews of this user

import cPickle as pickle

print 'Loading user list from users.p file.';
users = pickle.load(open('users.p', 'rb'));
print 'Finished loading user list.';

print 'Loading user list from users.p file.';
users = pickle.load(open('users.p', 'rb'));
print 'Finished loading user list.';

for user in users:
	print users[user];
	break;
	
	

