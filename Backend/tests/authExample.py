# Authenticating API's using Python Automation auth method (access token in header)- Example
import requests
from Backend.config.configurations import *
from Backend.config.resources import *

gitAccessUrl = get_config()['api']['gitHubUrl']
print(gitAccessUrl)
# userName = get_config()['gitHubCredentials']['userName']
# get password by user, not required as basic auth deprecated on github since 5may 2021
# session manager
with requests.Session() as sessionManager:
    HeadAccept = ApiResources.HeadAccept
    sessionManager.headers.update(HeadAccept)
    token = input('Please enter GitHub access token:\n')
    resourceObj = ApiResources(token)
    head_authorize = resourceObj.get_auth_token()
    sessionManager.headers.update(head_authorize)
    # requesting git hub with authorization header
    responseGitAuth = sessionManager.get(gitAccessUrl+'/user')
    print(responseGitAuth.status_code)
    print(responseGitAuth.json())

    # accessing octokit org's repo
    pathOrgRepos = ApiResources.gitHubRepo  # preparing base url using configurations.py
    repoUrl = gitAccessUrl+pathOrgRepos  # making final url by adding base url and resource path from resources.py
    print(repoUrl)
    responseUserRepos = sessionManager.get(repoUrl)
    print(responseUserRepos.status_code)
    # print(responseUserRepos.json())
