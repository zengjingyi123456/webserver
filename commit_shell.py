#-*- coding: utf-8 -*-

import os
repos = ["apache/cassandra","apache/camel","apache/hive","apache/commons-lang"]
def gitClone(name):
    projectPath = os.path.abspath('data/gitRepo/%s'%(name))
    not os.path.isdir(projectPath) and os.makedirs(projectPath)
    cmd = 'git clone https://github.com/%s.git %s' %(name, projectPath)
    cmd1 = 'git log --pretty=format:“%h - %an, %ar : %s” > log.txt'
    cmd2 = 'git log --pretty=format:“%h - %an, %ar : %s” > log.txt'
    cmd3 = 'git log --pretty=format:“%h - %an, %ar : %s” > log.txt'
    cmd4 = 'git log --pretty=format:“%h - %an, %ar : %s” > log.txt'
    cwd = os.getcwd()
    os.chdir(projectPath)
    result = os.system(cmd)
    result1 = os.system(cmd1)
    result1 = os.system(cmd1)
    result1 = os.system(cmd1)
    result1 = os.system(cmd1)
    os.chdir(cwd)
    if result != 0:
        return False
    return True
    if result1 != 0:
        return False
    return True

gitClone('cxsjclassroom/webserver')
