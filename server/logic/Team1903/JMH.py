#-*- coding: utf-8 -*-
import ssl
import requests
import os
import json

repos = ["apache/cassandra","apache/camel","apache/hive","apache/commons-lang"]

def getJMH(repo):
    jmh = {}
    repo_url = 'https://api.github.com/search/code?q=org.openjdk.jmh+in:file+language:java+repo:%s' % repo  # 确定url
    repoJMH = readURL('Repositories/Path/%s' % (repo), repo_url)  # 访问url得到数据
    repoJMH = repoJMH and json.loads(repoJMH)  # 将数据类型转换
    # 提取想要的信息保存在info中
    items = []
    JMHC=[]
    PA=[]
    JMHC.append(repoJMH['total_count'])
    items.append(repoJMH['items'])
    for i in items:
        for th in i:
            PA.append(th['path'])
            #print(PA)
    jmh[repo] = {
        "path": PA,
        'toco':JMHC
        }
    return jmh

#读取url的信息，并建立缓存PA.append(i['path'])
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
