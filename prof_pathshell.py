#-*- coding: utf-8 -*-

import profile
import os
import pstats
import pprint
import server.logic.Team1903.JMH as J

res=["apache/cassandra","apache/camel","apache/hive","apache/commons-lang"]

ct=[]
tt=[]
nc=[]



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


gitlog("apache/hive")


if __name__ == "__main__":
    profile.run("gitlog('apache/hive')")
    p = pstats.Stats("test.prof")
    stats = p.stats
    pprint(stats)
    for key in stats.keys():
        tu=stats[key]
        tt.append(tu[2])
        ct.append(tu[3])
        nc.append(tu[1])
    print(nc)
    print(tt)
    print(ct)

#gitlog("apache/cassandra")
#gitlog("apache/camel")
#gitlog("apache/commons-lang")
