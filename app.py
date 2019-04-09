#!/usr/local/bin/python3
import issue
import options
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
      opts, args = getopt.getopt(sys.argv[1:],"h",["reset","setup"])
    except getopt.GetoptError:
      print(help_str)
      sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(help_str)
            sys.exit()
        if opt == '--reset':
            reset = True
        if opt == '--setup':
            setup.setup()
    # print(opts,args)

    issue_url, mrUrl, isOpened = options.options(reset)
    issue.get_issue(issue_url,isOpened=isOpened)
