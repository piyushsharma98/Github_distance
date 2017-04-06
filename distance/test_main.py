from main import get_friends, distance

# Test the reading of the file
def test_get_friends():
	friends = get_friends()
	friends_count = len(friends)
	assert friends[0]['name'] == 'Chris'
	assert friends_count == 32
	assert friends[friends_count-1]['name'] == 'David'

# Test the distance between to point of given latitude and longitude
def test_distance():
	
	dist = distance(12.9611159,77.6362214,12.986375,77.043701) # Taking the first friend's location from json file
	assert dist == 64.26480291997056

	friends = get_friends()
	friends_count = len(friends)
	# Taking the last friend's location from json file
	dist = distance(12.9611159,77.6362214,float(friends[friends_count-1]['latitude']),float(friends[friends_count-1]['longitude']))
	assert dist == 54.57024856881087	