#-*- coding: utf-8 -*-
from app import route, response, redirect, config
import ssl
import requests
import os
import json
import logic.Team1903.branches as Branch
import logic.Team1903.infomation as Info
repos = ['cxsjclassroom/webserver',"octocat/Hello-World"]

@route('/hello.py.html')
def projectInfo(cookies):
	info = Info.getInfo()
	#将info返回给页面
	return response(projectInfo=info)

@route('/hellobran.py.html')
def projectBranches(cookies):
	bran = Branch.getBranches()
	#将info返回给页面
	return response(projectBran=bran)



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
