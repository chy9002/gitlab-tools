#!/usr/local/bin/python3
import issue
import options

if __name__ == '__main__':

    issueUrl, mrUrl = options.options()
    issue.get_issue(issueUrl)
