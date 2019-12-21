#-*- coding: utf-8 -*-
import ssl
import requests
import os
import json
import numpy as np

repos = ["apache/logging-log4j2",
         'ReactiveX/RxJava',
         "apache/cassandra",
         "apache/camel",
         "apache/hive",
         "apache/commons-lang"
         ]

repo2= ['ReactiveX/RxJava']
repo3= ["apache/cassandra"]
repo4= ["apache/camel"]
repo5= ["apache/hive"]
repo6= ["apache/commons-lang"]

def getstars():
    i=0
    stars=['','','','','','']
    for repo in repos:
        repo_url = 'https://api.github.com/repos/%s' % (repo)  # 确定url
        repoInfo = readURL('Repositories/reposInfo/%s' % (repo), repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        stars[i]=int(repoInfo['stargazers_count'])
        i=i+1
        # 提取想要的信息保存在info中
    #stars.append(int(np.meam(stars))) #均值
    #stars.append(int(np.var(stars))) #方差
    #stars.append(int(np.percentile(stars,50))) #中位数
    #stars.append(int(np.percentile(stars,25))) #四分位数
    return stars

def getsubscribers():
    i=0
    sub=['','','','','','']
    for repo in repos:
        repo_url = 'https://api.github.com/repos/%s' % (repo)  # 确定url
        repoInfo = readURL('Repositories/reposInfo/%s' % (repo), repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        sub[i]=int(repoInfo['subscribers_count'])
        i=i+1
        # 提取想要的信息保存在info中
    #stars.append(int(np.meam(stars))) #均值
    #stars.append(int(np.var(stars))) #方差
    #stars.append(int(np.percentile(stars,50))) #中位数
    #stars.append(int(np.percentile(stars,25))) #四分位数
    return sub


def gettime2():
    time2 = {}
    for repo in repo2:
        repo_url = 'https://api.github.com/repos/%s' % repo  # 确定url
        repoInfo = readURL('Repositories/reposInfo/%s' % (repo), repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        # 提取想要的信息保存在info中
        time2[repo] = {

            'stargazers_count': repoInfo['stargazers_count'],
            'subscribers_count': repoInfo['subscribers_count'],
            'created_at': repoInfo['created_at']

        }
        return time2

def gettime():
    time = {}
    for repo in repos:
        repo_url = 'https://api.github.com/repos/%s' % repo  # 确定url
        repoInfo = readURL('Repositories/reposInfo/%s' % (repo), repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        # 提取想要的信息保存在info中
        time[repo] = {

            'stargazers_count': repoInfo['stargazers_count'],
            'subscribers_count': repoInfo['subscribers_count'],
            'created_at': repoInfo['created_at']

        }
        return time

def gettime3():
    time3 = {}
    for repo in repo3:
        repo_url = 'https://api.github.com/repos/%s' % repo  # 确定url
        repoInfo = readURL('Repositories/reposInfo/%s' % (repo), repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        # 提取想要的信息保存在info中
        time3[repo] = {

            'stargazers_count': repoInfo['stargazers_count'],
            'subscribers_count': repoInfo['subscribers_count'],
            'created_at': repoInfo['created_at']

        }
        return time3

def gettime4():
    time4 = {}
    for repo in repo4:
        repo_url = 'https://api.github.com/repos/%s' % repo  # 确定url
        repoInfo = readURL('Repositories/reposInfo/%s' % (repo), repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        # 提取想要的信息保存在info中
        time4[repo] = {

            'stargazers_count': repoInfo['stargazers_count'],
            'subscribers_count': repoInfo['subscribers_count'],
            'created_at': repoInfo['created_at']

        }
        return time4

def gettime5():
    time5 = {}
    for repo in repo5:
        repo_url = 'https://api.github.com/repos/%s' % repo  # 确定url
        repoInfo = readURL('Repositories/reposInfo/%s' % (repo), repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        # 提取想要的信息保存在info中
        time5[repo] = {

            'stargazers_count': repoInfo['stargazers_count'],
            'subscribers_count': repoInfo['subscribers_count'],
            'created_at': repoInfo['created_at']

        }
        return time5

def gettime6():
    time6 = {}
    for repo in repo6:
        repo_url = 'https://api.github.com/repos/%s' % repo  # 确定url
        repoInfo = readURL('Repositories/reposInfo/%s' % (repo), repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        # 提取想要的信息保存在info中
        time6[repo] = {

            'stargazers_count': repoInfo['stargazers_count'],
            'subscribers_count': repoInfo['subscribers_count'],
            'created_at': repoInfo['created_at']

        }
        return time6

def getInfomation():
    info = {}
    for repo in repos:
        repo_url = 'https://api.github.com/repos/%s' % repo  # 确定url
        repoInfo = readURL('Repositories/reposInfo/%s' % (repo), repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        # 提取想要的信息保存在info中
        info[repo] = {
            "stargazers_count": repoInfo['stargazers_count'],
            'watchers_count': repoInfo['watchers_count'],
            'created_at': repoInfo['created_at'],
            'size': repoInfo['size'],
            'forks_count': repoInfo['forks_count'],
            'open_issues': repoInfo['open_issues']
        }
        return info
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
def getstime(repo):
    info = {}
    repo_url = 'https://api.github.com/repos/%s' % repo  # 确定url
    repoInfo = readURL('Repositories/reposInfo/%s' % (repo), repo_url)  # 访问url得到数据
    repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换
        # 提取想要的信息保存在info中
    info[repo] = {
        "stargazers_count": repoInfo['stargazers_count'],
        'watchers_count': repoInfo['watchers_count'],
        'ctime': repoInfo['created_at'],
        'size': repoInfo['size'],
        'forks_count': repoInfo['forks_count'],
        'open_issues': repoInfo['open_issues']
    }
    ctime=info[repo]
    ctime=ctime['ctime']
    return ctime

