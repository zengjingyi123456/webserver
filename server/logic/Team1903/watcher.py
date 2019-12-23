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


