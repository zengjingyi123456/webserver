import pandas as pd
#import path_shell as ps
import server.logic.Team1903.JMH as J
import os
import time
import server.logic.Team1903.infomation as Info
import datetime
from collections import Counter
import matplotlib.pyplot as plt
res=["apache/cassandra","apache/camel","apache/hive","apache/commons-lang"]


def gitdata(name):
    pathcount=1
    ptfl=[]
    ptsl=[]
    pttl=[]
    ptfd={}
    ptsd={}
    pttd={}
    pttdmid={}
    projectPath = os.path.abspath('data/gitRepo/%s'%(name))
    resd=J.getJMH(name)
    mid=resd[name]
    pathd=mid['path']
    toco=mid['toco']
    not os.path.isdir(projectPath) and os.makedirs(projectPath)
    cwd = os.getcwd()
    os.chdir(projectPath)
    for pi in pathd:
        ptpd=pd.read_csv('atnco'+str(pathcount)+'.txt',sep="\t",names=["times","name"])
        ptlist=ptpd.values.tolist()
        ptfv=0
        sign=0
        for i in ptlist:
            ptfv=ptfv+i[0]
            pttdmid[i[1]]=i[0]
        X,Y=Counter(pttd),Counter(pttdmid)
        pttd=dict(X+Y)
        pttdmid.clear()
        ptfd[pi]=ptfv
        ptfl.append(ptfv)
        ptsd[pi]=len(ptlist)
        ptsl.append(len(ptlist))
        pathcount=pathcount+1
    for key in pttd.keys():
        pttl.append(pttd[key])
    logt={'name':name,'path':pathd,'ptfd':ptfd,'ptsd':ptsd,'pttd':pttd,'ptfl':ptfl,'ptsl':ptsl,'pttl':pttl,}
    return logt


def gittime(name):
    pathcount=1
    projectPath = os.path.abspath('data/gitRepo/%s'%(name))
    resd=J.getJMH(name)
    mid=resd[name]
    pathd=mid['path']
    toco=mid['toco']
    not os.path.isdir(projectPath) and os.makedirs(projectPath)
    cwd = os.getcwd()
    os.chdir(projectPath)
    ctime=Info.gettime(name)
    ctime=ctime[:-10]
    ctime=time.strptime(ctime,"%Y-%m-%d")
    ctime=datetime.datetime(ctime[0],ctime[1],ctime[2])
    print(ctime)
    timem=[]
    for pi in pathd:
        ptpd=pd.read_csv('times'+str(pathcount)+'.txt',sep="|")
        ptlist=ptpd.values.tolist()
        for pi in ptlist:
            pi[1]=(pi[1])[:-6]
            pitimef=time.strptime(pi[1], "%a %b %d %H:%M:%S %Y")
            pitimef=datetime.datetime(pitimef[0],pitimef[1],pitimef[2])
            times=pitimef-ctime
            times=times.days
            timem.append(times)
    return timem



def gitframe(f):
    #ct=changetimes ac=athuer_count
    fframe={'file':f['path'],'ct':f['ptfl'],'ac':f['ptsl']}
    sframe={'file':f['pttd'].keys(),'act':f['pttl']}
    #tframe={'time':tf}
    dff=pd.DataFrame(fframe)
    sdf=pd.DataFrame(sframe)
    #tdf=pd.DataFrame(tframe)
    mean=[]
    mid=[]
    sv=[]
    cta=dff['ct'].mean()
    aca=dff['ac'].mean()
    acta=sdf['act'].mean()

    mean.append(cta)
    mean.append(aca)
    mean.append(acta)
    
    ctm=dff['ct'].median()
    acm=dff['ac'].median()
    actm=sdf['act'].median()
    
    mid.append(ctm)
    mid.append(acm)
    mid.append(actm)

    ctv=dff['ct'].var()
    acv=dff['ac'].var()
    actv=sdf['act'].var()

    sv.append(ctv)
    sv.append(acv)
    sv.append(actv)
    #ta=tdf['time'].maen()
    #print(ta)

    plotdata={'name':f['name'],'avr':mean,'mid':mid,'var':sv}
    print(plotdata)
    return plotdata


#res=["apache/cassandra","apache/camel","apache/hive","apache/commons-lang"]

#gitdata(name)
#gittime(name)
#gitframe(f)
fr=gitdata('apache/commons-lang')
dfra=gitframe(fr)
pframe=pd.DataFrame(dfra)
print(pframe)
pframe.plot.bar()
plt.show()

'''
projectPath = os.path.abspath('data/gitRepo/apache/camel')
not os.path.isdir(projectPath) and os.makedirs(projectPath)
cwd = os.getcwd()
os.chdir(projectPath)
pathcount=3
test=pd.read_csv('atnco'+str(pathcount)+'.txt',sep="\t",names=["times","name"])
tlist=test.values.tolist()
print(test)
print(tlist)
'''
