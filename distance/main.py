#! /usr/bin/python3
from math import radians, sin, cos, asin, sqrt
import json
from pprint import pprint

def get_friends():
    friends_list = []
    with open('friends.json') as friends:
        for friend in friends:
            friend = json.loads(friend)
            friends_list.append(friend)            
    return friends_list

def distance(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    # haversine formula
    lat_diff = lat2 - lat1 
    lon_diff = lon2 - lon1 

    a = sin(lat_diff/2)**2 + cos(lat1) * cos(lat2) * sin(lon_diff/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers is 6371
    return c * r

if __name__ == '__main__':

    invite_list = []
    friends = get_friends()
    for friend in friends:
        dist = distance(12.9611159,77.6362214,float(friend["latitude"]),float(friend["longitude"]))
        if dist <= 100:
            invite_list.append((int(friend['user_id']), friend['name']))
    print("List of the user_id and Friends name within 100Km...")
    # Sort the invite list
    sorted_invite_list = sorted(invite_list,key=lambda id: id[0]) 
    pprint(sorted_invite_list)
        
        