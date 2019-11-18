#-*- coding: utf-8 -*-

import os
def gitClone(name):
    projectPath = os.path.abspath('data/gitRepo/%s'%(name))
    print('1')
    not os.path.isdir(projectPath) and os.makedirs(projectPath)
    print('2')
    cmd = 'git clone https://github.com/%s.git %s' %(name, projectPath)
    #print('2.5')
    #cmd1 = 'git shortlog -s -n head itests/hive-jmh/src/main/java/org/apache/hive/benchmark/hash/Murmur3Bench.java > athercount.txt'
    #cmd2 = 'git log --pretty=format:"%h|%ce|%cd" itests/hive-jmh/src/main/java/org/apache/hive/benchmark/hash/Murmur3Bench.java > chtime.txt'
    cwd = os.getcwd()
    print('3')
    os.chdir(projectPath)
    result = os.system(cmd)
    print('4')
    #result1 = os.system(cmd1)
    #result1 = os.system(cmd2)
    os.chdir(cwd)
    print('5')
    if result != 0:
        return False
    return True
    if result1 != 0:
        return False
    return True

gitClone('apache/hive')
