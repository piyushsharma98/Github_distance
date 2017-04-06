# Github Profile and Repositories#
1. githublib.py is a library contains functions to get the public profile of a github user , it taker username as input . It also provide list of public repositories of the provided username.
2. githublib.py uses requests python library 
3. main.py is a programme that print the list of public repositories of entered username.
4. **Pytest test framework** is used to test the library.
5. test_githublib.py test all the functions of library.

### Installation of Pytest test framework ###
  1. Command to install pytest framework : pip install pytest
  2. To test the code run : py.test -v ( Make sure u are in respective folder containing test file)
## Note : As github provide max 60 requests in 1 hr so if there is any error it can be due to exceeding of API rate limit.##

# Distance between two coordinates#
1. main.py reads the friends.json file and print the lists of friends with user id sorted by user_id within the 100km of GPS coordinates 12.9611159,77.6362214 .
2. haversine formula is used to calculate distance between two given coordinates.
3. test_main.py test get_friends() and distance() functions.
3. test_main.py test get_friends() and distance() functions.

