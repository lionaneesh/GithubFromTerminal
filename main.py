from pygithub3 import Github
import subprocess 
import time
import sys

username = raw_input("Username: ")
password = raw_input("Password: ")
gh = Github(login=username, password=password)

repo = gh.repos.create({"name":raw_input("RepoName: "), "description":raw_input("Description: "), "homepage":""})
subprocess.call(["git", "init"])
subprocess.call(["git", "remote", "add", "origin", repo.clone_url])
