#-*- coding: utf-8 -*-

import os
import server.logic.Team1903.JMH as J

res=["apache/cassandra","apache/camel","apache/hive","apache/commons-lang"]
def gitlog(name):
    projectPath = os.path.abspath('data/gitRepo/%s'%(name))
    resd=J.getJMH(name)
    mid=resd[name]
    pathd=mid['path']
    print(pathd)
    not os.path.isdir(projectPath) and os.makedirs(projectPath)
    cwd = os.getcwd()
    print('1')
    print('1')
    os.chdir(projectPath)
    print('1')
    pathcount=1
    for pi in pathd:
        print(pi)
        cmd = 'git shortlog -s -n head %s > atnco%s.txt' %(pi, str(pathcount))
        result = os.system(cmd)
        pathcount=pathcount+1
    os.chdir(projectPath)
    pathcount=1
    for pit in pathd:
        print(pit)
        cmd = 'git log --pretty=format:"%%h|%%ce|%%cd" %s > times%s.txt' %(pit,str(pathcount))
        result = os.system(cmd)
        pathcount=pathcount+1
    os.chdir(cwd)

gitlog("apache/cassandra")
#gitlog("apache/camel")
gitlog("apache/hive")
gitlog("apache/commons-lang")
    #if result != 0:
    #    return False
    #return True
    #if result1 != 0:
    #    return False
    #return True


