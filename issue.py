import json
import requests

def get_issue(issueUrl, nextpage = 1):
    print(nextpage)
    issuePath = './data/issues.json'
    if nextpage == 1:
        with open(issuePath,'w+') as issuefs:
            issuefs.write(r'[]')
    with requests.get(issueUrl+'&page=%d'%(nextpage)) as issues:
        with open(issuePath,'r') as issuefs:
            issuejson = json.load(issuefs)
            for issue in issues.json():
                issuejson.append(issue)
        with open(issuePath,'w+') as issuefs:
            issuefs.write(json.dumps(issuejson))
        next_page = issues.headers['X-Next-Page']
        if next_page.isnumeric():
            get_issue(issueUrl,int(next_page))
        else:
            print('Done!')