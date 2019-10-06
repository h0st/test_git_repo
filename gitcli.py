#!/usr/bin/env python
#coding: utf-8

import os
import sys
import argparse
from gitmanager import *


def createParser ():
    parser = argparse.ArgumentParser(description="Manager for your Git repo ...")
    parser.add_argument('--repourl', type=str, help='Git repository URL')
    parser.add_argument('--repodir', type=str, help='Git repo local directory')
    parser.add_argument('--branchname', type=str, help='Git repo branch name')
    parser.add_argument('--commitmsg', type=str, help='Git commit message')
    parser.add_argument('--cmd', type=str, help='Command string')
    parser.add_argument('-clone', nargs='?', const='clone', default='uncloned', help='Clone Git repo')
    parser.add_argument('-createbranch', nargs='?', const='createbranch', default='uncreate', help='Create new repo branch')
    parser.add_argument('-switchbranch', nargs='?', const='switchbranch', default='unswitch', help='Switch to repo branch')
    parser.add_argument('-commit', nargs='?', const='commit', default='uncommit', help='Commit repo changes with message')
    parser.add_argument('-push', nargs='?', const='push', default='unpush', help='Push repo changes to the branch')
    parser.add_argument('-status', nargs='?', const='status', default='unstatus', help='Git repo status')
    parser.add_argument('-exec', nargs='?', const='exec', default='unexec', help='Execute some command')
    return parser


if __name__ == '__main__':
    parser = createParser()
    args = vars(parser.parse_args())
    #print(args)

    repourl = args['repourl']
    repodir = args['repodir']
    branchname = args['branchname']
    commitmsg = args['commitmsg']
    cmd = args['cmd']
    
    git = GitManager(repourl, repodir)

    # SWITCH FOR EACH COMMAND
    if args['clone'] == 'clone':
        git.clone(repourl, repodir)
    elif args['createbranch'] == 'createbranch':
        git.create_branch(branchname)
    elif args['switchbranch'] == 'switchbranch':
        git.switch_to_branch(branchname)
    elif args['commit'] == 'commit':
        git.commit(commitmsg)
    elif args['push'] == 'push':
        git.push(branchname)
    elif args['status'] == 'status':
        git.status()
    elif args['exec'] == 'exec':
        git.exec_cmd(cmd)
    else:
        print("Welcome to the Git Manager ... Enter gitcli.py -h for a help.")
        
        