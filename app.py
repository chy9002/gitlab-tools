import json
import requests
import os
import setup
import issue

confPath = './data/config.json'

if not os.path.exists(confPath):
    setup.setup()

with open(confPath, 'r') as confstr:
    config = json.load(confstr)


groupUrl = '%s/groups/?private_token=%s' % (
    config['url'], config['private_token'])
with requests.get(groupUrl) as groups:
    # groupJson = groups.json()
    i = 0
    for group in groups.json():
        print('[%d] - %s(%s)' % (i, group['name'], group['web_url']))
        i += 1
    groupin = input('Please input your group: ')
    groupid = groups.json()[int(groupin)]['id']

projectUrl = '%s/groups/%s/projects?private_token=%s' % (
    config['url'], groupid, config['private_token'])
# print(projectUrl)
with requests.get(projectUrl) as projects:
    i = 0
    for project in projects.json():
        print('[%d] - %s(%s)' % (i, project['name'], project['web_url']))
        i += 1
    projectin = input('Please input your project: ')
    # projectid = projects.json()[int(projectin)]['id']

    issueUrl = projects.json()[int(projectin)]['_links']['issues']+'?private_token=%s'%(config['private_token'])
    mrurl = projects.json()[int(projectin)]['_links']['merge_requests']+'?private_token=%s'%(config['private_token'])

if __name__ == '__main__':
    issue.get_issue(issueUrl)
