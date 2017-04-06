from githublib import *

 # Get the Profile data of user "defunkt" using github api
def test_get_profile():
	profile = get_profile('defunkt')
	assert profile['login'] == 'defunkt' # Profile login id
	assert profile['public_repos'] == 107 # profile's total public repositories

	profile = get_profile('defunkthidhhdih') # A wrong username that does not exist
	assert profile == 0

# Get the repository data of user "defunkt" using github api
def test_get_repositories(): 
	repos = get_repositories('defunkt')
	repo_count = len(repos)
	assert repo_count == 107 # Total no of public repositories of defunkt

# Test the Profile object having name, location, email, followers attributes
def test_create_profile():
	user = create_profile('defunkt')
	assert user.name == 'Chris Wanstrath' # Name of the user "defunkt"
	assert user.location == 'San Francisco' # Location of defunkt
	assert user.email == 'chris@github.com' # Email id of defunkt
	assert user.followers == 16011 # Total Followers of defunkt

# Test the list of public repository objects having name, html_url, stargazers_count, description, homepage attributes
def test_public_repositories():
	repo_list = public_repositories('defunkt')
	assert len(repo_list) == 107 # Total no of public repositories of defunkt
	assert repo_list[0].name == 'ace' # Repo name of the first repo in list
	assert repo_list[0].html_url == 'https://github.com/defunkt/ace' # Repo html url of the first repo in list
	assert repo_list[0].stargazers_count == 11 # Stargazers count of first repository in the list
	assert repo_list[0].description == 'Ajax.org Cloud9 Editor' # Description of first repository in the list	
	assert repo_list[0].home_page == 'http://ace.ajax.org' # Repo homepage of the first repo in list
