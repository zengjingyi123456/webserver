#-*- coding: utf-8 -*-
from app import route, response, redirect, config
import ssl
import requests
import os
import json
import logic.Team1903.branches as Branch
import logic.Team1903.infomation as Info
import logic.Team1903.commits as Co
import logic.Team1903.JMH as P
import logic.Team1903.c as c
import numpy as np



repos = ["apache/logging-log4j2",
         "ReactiveX/RxJava",
         "apache/cassandra",
         "apache/camel",
         "apache/hive",
         "apache/commons-lang"
         ]




@route('/hello.py.html')
def projectInfo():

    #将info返回给页面
    infoShow = [
    { 'genre': 'apache/logging-log4j2', 'sold': Info.getstars()[0] },
    { 'genre': 'ReactiveX/RxJava', 'sold': Info.getstars()[1] },
    { 'genre': 'apache/cassandra', 'sold': Info.getstars()[2] },
    { 'genre': 'apache/camel', 'sold': Info.getstars()[3] },
    { 'genre': 'apache/hive', 'sold': Info.getstars()[4] },
    { 'genre': 'apache/commons-lang', 'sold': Info.getstars()[5] },
    #{ 'genre': '均值', 'sold': Info.getstars()[6] },
    #{ 'genre': '方差', 'sold': Info.getstars()[7] },
    #{ 'genre': '中位数', 'sold': Info.getstars()[8] },
    #{ 'genre': '四分位数', 'sold': Info.getstars()[9] }
    ]



    subShow = [
    { 'genre': 'apache/logging-log4j2', 'sold': Info.getsubscribers()[0] },
    { 'genre': 'ReactiveX/RxJava', 'sold': Info.getsubscribers()[1] },
    { 'genre': 'apache/cassandra', 'sold': Info.getsubscribers()[2] },
    { 'genre': 'apache/camel', 'sold': Info.getsubscribers()[3] },
    { 'genre': 'apache/hive', 'sold': Info.getsubscribers()[4] },
    { 'genre': 'apache/commons-lang', 'sold': Info.getsubscribers()[5] }
    ]

    releasesShow = [
    { 'genre': 'apache/logging-log4j2', 'sold': 67 },
    { 'genre': 'ReactiveX/RxJava', 'sold': 224 },
    { 'genre': 'apache/cassandra', 'sold': 243 },
    { 'genre': 'apache/camel', 'sold': 150 },
    { 'genre': 'apache/hive', 'sold': 54 },
    { 'genre': 'apache/commons-lang', 'sold': 87 }
    ]

    commitShow = [
    { 'genre': 'apache/logging-log4j2', 'sold': 69 },
    { 'genre': 'ReactiveX/RxJava', 'sold': 5600 },
    { 'genre': 'apache/cassandra', 'sold': 24879 },
    { 'genre': 'apache/camel', 'sold': 40588 },
    { 'genre': 'apache/hive', 'sold': 13882 },
    { 'genre': 'apache/commons-lang', 'sold': 5592 }
    ]
    contributorShow = [
    { 'genre': 'apache/logging-log4j2', 'sold': 69 },
    { 'genre': 'ReactiveX/RxJava', 'sold': 239 },
    { 'genre': 'apache/cassandra', 'sold': 279 },
    { 'genre': 'apache/camel', 'sold': 544 },
    { 'genre': 'apache/hive', 'sold': 194 },
    { 'genre': 'apache/commons-lang', 'sold': 127 }
    ]


    times=Info.gettime()
    times2=Info.gettime2()
    times3=Info.gettime3()
    times4=Info.gettime4()
    times5=Info.gettime5()
    times6=Info.gettime6()

    s=c.getinfoc()

    return response(cShow=s,timeShow6=times6,timeShow5=times5,timeShow4=times4,timeShow3=times3,timeShow2=times2,timeShow=times,infoShow=infoShow,subShow=subShow,releasesShow=releasesShow,commitShow=commitShow,contributorShow=contributorShow)

@route('/hellobran.py.html')
def projectBranches():
    bran = Branch.getBranches()
    #将info返回给页面
    return response(projectBran=bran)
@route('/helloCo.py.html')
def projectCommits(cookies):
    commits = Co.getCommits()
    #将info返回给页面
    return response(projectCo=commits)
@route('/path.py.html')
def projectPath(cookies):
    JMH = P.getJMH()
    #将info返回给页面
    return response(projectPa=JMH)




#读取url的信息，并建立缓存
def readURL(cache,url):
    #看看该url是否访问过
    cache = 'data/cache/%s' % cache
    if os.path.isfile(cache):
        with open(cache, 'r') as f:
            content = f.read()
        return content

    content = requests.get(url).content.decode()

    #吧文件内容保存下来，以免多次重复访问url，类似于缓存
    folder = cache.rpartition('/')[0]
    not os.path.isdir(folder) and os.makedirs(folder)
    with open(cache, 'w') as f:
        f.write(content)
    return content


import os
repos = [

         "apache/cassandra",
         "apache/camel",
         "apache/hive",
         "apache/commons-lang"
         ]
for name in repos:
#def gitClone(name):
    projectPath=os.path.abspath('data/gitRepo/%s' % (name))
    not os.path.isdir(projectPath) and os.makedirs(projectPath)

    cwd = os.getcwd()
    os.chdir(projectPath)
    os.system('git shortlog -s -n>log.txt')
    os.chdir(cwd)



