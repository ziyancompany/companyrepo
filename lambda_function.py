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

# function for grant team member read permission on all repos when Org base permission is set to No Permission
# used for dedicated read permission team like auditing team or security team
            
# def lambda_handler(event, context):
#     org = g.get_organization("your_org_name")
#     team = org.get_team_by_slug(team_slug)
#     git_event = event['headers']['x-github-event']
#     if git_event == "repository":
#         for repo in org.get_repos():
#             for member in team.get_members():
#                 repo.add_to_collaborators(member, permission="pull")
