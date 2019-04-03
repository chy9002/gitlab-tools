import os
import json

def configJson(url, pt):
    conf = {
        'url':url,
        'private_token':pt
    }
    return json.dumps(conf)

def setup():
    dataDir = './data'
    configPath = dataDir+'/config.json'
    if not os.path.exists(dataDir):
        os.makedirs(dataDir)
    url = input("Please input gitlab api url: ").rstrip('/')
    pt = input("Please input your gitlab private token: ")
    with open(configPath,"w+") as confile:
        confile.write(configJson(url,pt))

if __name__ == "__main__":
    setup()