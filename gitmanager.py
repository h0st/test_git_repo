#!/usr/bin/env python
#coding: utf-8

import os
import os.path


class GitManager():

    def __init__(self, repo_url, repo_dir):
        self.repo_url = repo_url
        self.repo_dir = repo_dir

    
    def exec_cmd(self, cmd):
        if cmd is not None:
            os.system(cmd)
        else:
            print("Command is not defined!")
        
        
    def check_git(self):
        if os.path.exists(".git"):
            return True
        else:
            return False


    # clone repo
    def clone(self, repo_url, repo_dir):
        if repo_url is not None and repo_dir is not None:
            cmd = "git clone {} {}".format(repo_url, repo_dir)
            self.exec_cmd(cmd)
        else:
            print("Repo URL or directory is not defined!")
    
    
    def create_branch(self, branch_name):
        if self.check_git():
            if branch_name is not None:
                cmd = "git branch {}".format(branch_name)
                self.exec_cmd(cmd)
            else:
                print("Branch name is not defined!")
        else:
            print("You are not in a Git repo directory, please open it first!")
    
    
    def switch_to_branch(self, branch_name):
        if self.check_git():
            if branch_name is not None:
                cmd = "git checkout {}".format(branch_name)
                self.exec_cmd(cmd)
            else:
                print("Branch name is not defined!")
        else:
            print("You are not in a Git repo directory, please open it first!")
    

    # add all file and commit with message
    def commit(self, commit_msg):
        if self.check_git():
            if commit_msg is not None:
                cmd = "git add . && git commit -am \"{}\"".format(commit_msg)
                self.exec_cmd(cmd)
            else:
                print("Commit message is not defined, please, write comment using --commitmsg!")
        else:
            print("You are not in a Git repo directory, please open it first!")
        
        
    def push(self, branch_name):
        if self.check_git():
            if branch_name is not None:
                cmd = "git push origin {}".format(branch_name)
                self.exec_cmd(cmd)
            else:
                print("Branch name is not defined!")
        else: 
            print("You are not in a Git repo directory, please open it first!")
    
    
    def status(self):
        if self.check_git():
            cmd = "git status"
            self.exec_cmd(cmd)
        else:
            print("You are not in a Git repo directory, please open it first!")
