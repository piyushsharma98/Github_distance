#! /usr/bin/python3

from githublib import public_repositories, create_profile, get_profile
from pprint import pprint
	
if __name__ == '__main__':
	
	username = input("Enter a Github Username : ")
	repolist = []
	repos = public_repositories(username)
	if not repos:
		print("404 not Found")
	else:
		repos = sorted(repos,key = lambda x:x.stargazers_count,reverse=True) # Sorting the list of repo objects
		print('list of the repository name and stargazers count .. ')
		for repo in repos:
			repolist.append((repo.name,repo.stargazers_count))
		pprint(repolist)	 #list of the repository name and stargazers count

