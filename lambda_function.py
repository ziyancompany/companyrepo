import json
import uuid
from github import Github

# using an access token
g = Github("access_token")

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

def lambda_handler(event, context):
    # print(git_event)
    git_event = event['headers']['x-github-event']
    if git_event == "repository":
        for repo in g.get_organization("ziyancompany").get_repos():
            #print(repo.name)
            branch = repo.get_branch("master")
            branch.edit_protection(required_approving_review_count=2, enforce_admins=True)
            print("Edited the branch protection rules for: " + repo.name)
