#!/usr/local/bin/python3
import issue
import options
import getopt
import sys

if __name__ == '__main__':
    reset = False
    try:
      opts, args = getopt.getopt(sys.argv[1:],"",["reset"])
    except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
    if 'reset' in args:
        reset = True
    issueUrl, mrUrl = options.options(reset)
    issue.get_issue(issueUrl)
