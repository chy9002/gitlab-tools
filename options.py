import json
import requests
import os
import setup

def options(reset = False):
    option_json = {"GroupID":0,"ProjectID":0}
    confPath = './data/config.json'
    opt_file = './data/options.json'

    if not os.path.exists(confPath):
        setup.setup()

    with open(confPath, 'r') as confstr:
        config = json.load(confstr)

    if not os.path.exists(opt_file):
        reset = True

    if reset:
        groupUrl = '%s/groups/?private_token=%s' % (
            config['url'], config['private_token'])
        with requests.get(groupUrl) as groups:
            # groupJson = groups.json()
            i = 0
            for group in groups.json():
                print('[%d] - %s(%s)' % (i, group['name'], group['web_url']))
                i += 1
            group_in = input('Please input your group: ')
            group_id = groups.json()[int(group_in)]['id']
            option_json["GroupID"] = group_id

        projectUrl = '%s/groups/%s/projects?private_token=%s' % (
            config['url'], group_id, config['private_token'])
        # print(projectUrl)
        with requests.get(projectUrl) as projects:
            i = 0
            for project in projects.json():
                print('[%d] - %s(%s)' % (i, project['name'], project['web_url']))
                i += 1
            project_in = int(input('Please input your project: '))
            project_id = projects.json()[int(project_in)]['id']
            option_json["ProjectID"] = project_id

            issueUrl = '%s/projects/%d/issues?private_token=%s' % (config['url'], project_id, config['private_token'])
            mrUrl = '%s/projects/%d/merge_requests?private_token=%s' % (config['url'], project_id, config['private_token'])
            with open('./data/options.json','w+') as opt:
                opt.write(json.dumps(option_json))
    else:
        with open(opt_file, 'r') as optf:
            opt = json.load(optf)
            print('load last time options GroupID:%d, ProjectID:%d'%(opt["GroupID"],opt["ProjectID"]))
            issueUrl = '%s/projects/%d/issues?private_token=%s' % (config['url'], opt["ProjectID"], config['private_token'])
            mrUrl = '%s/projects/%d/merge_requests?private_token=%s' % (config['url'], opt["ProjectID"], config['private_token'])
    return issueUrl, mrUrl


if __name__ == '__main__':
    options()