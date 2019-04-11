#!/usr/bin/python3
import gitlabtool
import getopt
import sys
import setup

if __name__ == '__main__':
    reset = False
    help_str = '''
      app.py reset|setup
      reset -- reset group and project
      setup -- setup api url and token
      '''
    try:
      opts, args = getopt.getopt(sys.argv[1:],"him",["reset","setup"])
    except getopt.GetoptError:
      print(help_str)
      sys.exit(2)

    if len(opts) == 0:
      opts=[('-i','')]

    issue_url, mrUrl, isOpened = gitlabtool.options(reset)
    
    for opt, arg in opts:
      if opt == '-h':
          print(help_str)
          sys.exit()
      if opt == '--reset':
          reset = True
      if opt == '--setup':
          setup.setup()
      if opt == '-m':
        gitlabtool.get_mr(mrUrl)
      if opt == '-i':
        gitlabtool.get_issue(issue_url,isOpened=isOpened)

