import os

def git_pull():
    return os.popen('git pull origin master').read()