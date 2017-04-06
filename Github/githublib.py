#! /usr/bin/python3
import requests

class Profile(object):
	def __init__(self, username, name, location, email, followers):
		self.username = username
		self.name = name
		self.location = location
		self.email = email
		self.followers = followers
		self.public_repo = []

	def load_repo(self):
		repo_list = public_repositories(self.username)
		self.public_repo = repo_list

class Repository(object):
	def __init__(self, name, html_url, stargazers_count, description, home_page):
		self.name = name
		self.html_url = html_url
		self.stargazers_count = stargazers_count
		self.description = description
		self.home_page = home_page

 # Get the Profile data using github api
def get_profile(username):
	profile_url = 'https://api.github.com/users/'+username
	profile = requests.get(profile_url)
	if profile.headers['status'] == "200 OK":
		return profile.json()
	else:
		print(profile.json()['message'])
		return 0

# Get the repository data using github api
def get_repositories(username):
	profile = get_profile(username)
	if not profile:
		return 0
	repos_list = []
	if profile['public_repos']%30 != 0:
		page_count = int(profile['public_repos']/30) + 1
	else:
		page_count = int(profile['public_repos']/30)

	print(page_count,'Pages to be requested of max 30 repositories each')

	for i in range(1,page_count+1):
		repo_url = 'https://api.github.com/users/'+username+'/repos?page='+str(i)
		print('Requesting page ... ',i)
		repos = requests.get(repo_url)
		if repos.headers['status'] != "200 OK":
			print(repos.json().headers['message'])
			return 0
		repos = repos.json()
		for repo in repos:
			repos_list.append(repo)
	return repos_list

# Create the Profile object having name, location, email, followers, list of public_repo objects
def create_profile(username):
	profile = get_profile(username) # get profile from github api
	if not profile:
		return 0
	# repos = get_repositories(username) # get public repositories from github api
	user = Profile(username, profile['name'], profile['location'], profile['email'], profile['followers']) # creating a user object of profile class	
	user.load_repo() # loading of repositories in a list attribute of user object
	return user

# Create the list of public repository objects having name, html_url, stargazers_count, description, homepage attributes
def public_repositories(username):
	repo_list = []
	repos = get_repositories(username)
	if not repos:
		return 0
	for repo in repos:
		repository = Repository(repo['name'], repo['html_url'], repo['stargazers_count'], repo['description'], repo['homepage'])
		repo_list.append(repository)
	print('Total No of public repositories = ',len(repo_list))
	return repo_list
