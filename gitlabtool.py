import json
import requests
import os
import setup


def opened(isOpened):
    return '&state=opened' if isOpened else ''

def get_issue(issue_url, next_page = 1, isOpened = True):
    issuePath = './data/issues.json'
    if next_page == 1:
        with open(issuePath,'w+') as issuefs:
            issuefs.write(r'[]')
    with requests.get(issue_url+opened(isOpened)+'&page=%d'%(next_page)) as issues:
        with open(issuePath,'r') as issuefs:
            issuejson = json.load(issuefs)
            for issue in issues.json():
                issuejson.append(issue)
        with open(issuePath,'w+') as issuefs:
            issuefs.write(json.dumps(issuejson))
        next_page = issues.headers['X-Next-Page']
        if next_page.isnumeric():
            get_issue(issue_url,int(next_page),isOpened)
        else:
            print('Done!')

def get_mr(mr_url, next_page = 1):
    mrPath = './data/mr.json'
    if next_page == 1:
        with open(mrPath,'w+') as mrfs:
            mrfs.write(r'[]')
    with requests.get(mr_url+'&page=%d'%(next_page)) as mrs:
        with open(mrPath,'r') as mrfs:
            mrjson = json.load(mrfs)
            for mr in mrs.json():
                mrjson.append(mr)
        with open(mrPath,'w+') as mrfs:
            mrfs.write(json.dumps(mrjson))
        next_page = mrs.headers['X-Next-Page']
        if next_page.isnumeric():
            get_mr(mr_url,int(next_page))
        else:
            print('Done!')

def options(reset = False):
    option_json = {"GroupID":0,"ProjectID":0,"isOpened":True}
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

            issue_url = '%s/projects/%d/issues?private_token=%s' % (config['url'], project_id, config['private_token'])
            mrUrl = '%s/projects/%d/merge_requests?private_token=%s' % (config['url'], project_id, config['private_token'])
        isOpened_in = input("Only query for open issue?(y)es/(n)o(default:yes): ")
        if isOpened_in in ['n','N','no','No']:
            isOpened=False
        else:
            isOpened=True
        option_json["isOpened"]=isOpened
        with open('./data/options.json','w+') as opt:
            opt.write(json.dumps(option_json))
    else:
        with open(opt_file, 'r') as optf:
            opt = json.load(optf)
            print('load last time options GroupID:%d, ProjectID:%d %s'% (
                opt["GroupID"]
                ,opt["ProjectID"]
                ,', Only Open issue' if opt["isOpened"] else ''
            ))
            issue_url = '%s/projects/%d/issues?private_token=%s' % (config['url'], opt["ProjectID"], config['private_token'])
            mrUrl = '%s/projects/%d/merge_requests?private_token=%s' % (config['url'], opt["ProjectID"], config['private_token'])
            isOpened = opt["isOpened"]
    return issue_url, mrUrl, isOpened