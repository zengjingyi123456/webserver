import logdata as log
import pandas as pd
import server.logic.Team1903.JMH as J
import os
import matplotlib.pyplot as plt
res=["apache/cassandra","apache/camel","apache/hive","apache/commons-lang"]
def gitframe(name):
    projectPath = os.path.abspath('data/gitRepo/%s'%(name))
    resd=J.getJMH(name)
    mid=resd[name]
    pathd=mid['path']
    toco=mid['toco']
    not os.path.isdir(projectPath) and os.makedirs(projectPath)
    cwd = os.getcwd()
    os.chdir(projectPath)
    f=log.gitdata(name)
    time=log.gittime(name)
    #ct=changetimes ac=athuer_count
    frame={'file':pathd,'changetimes':f[ptfl],'athuer_count':f[ptsl]}
    Frame=DataFrame(c)
    print(Frame)
    return 0
gitframe('apache/cassandra')
