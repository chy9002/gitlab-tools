import json
import requests

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