#-*- coding: utf-8 -*-

import os
import server.logic.Team1903.JMH as J

repos = ["apache/cassandra","apache/camel","apache/hive","apache/commons-lang","ReactiveX/RxJava","apache/logging-log4j2"]
def gitlog(name):
    projectPath = os.path.abspath('data/gitRepo/%s'%(name))
    resd=J.getJMH(name)
    mid=resd[name]
    pathd=mid['path']
    not os.path.isdir(projectPath) and os.makedirs(projectPath)
    cwd = os.getcwd()
    os.chdir(projectPath)
    pathcount=1
    print('atnco')
    for pi in pathd:
        print(pi)
        cmd = 'git shortlog -s -n head %s >atnco%s.txt' %(pi, str(pathcount))
        result = os.system(cmd)
        pathcount=pathcount+1
    os.chdir(projectPath)
    pathcount=1
    print('times')
    for pit in pathd:
        print(pit)
        cmd = 'git log --pretty=format:"%%h|%%ce|%%cd" %s >times%s.txt' %(pit,str(pathcount))
        result = os.system(cmd)
        pathcount=pathcount+1
    os.chdir(cwd)
    

for i in repos:
    gitlog(i)
    print('done')



