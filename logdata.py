

#import path_shell as ps


import server.logic.Team1903.JMH as J
import os
import time
import server.logic.Team1903.infomation as Info
import datetime
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd



repos = ["apache/cassandra","apache/camel","apache/hive","apache/commons-lang","ReactiveX/RxJava","apache/logging-log4j2"]

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
    os.chdir(cwd)
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
    ctime=Info.getstime(name)
    ctime=ctime[:-10]
    ctime=time.strptime(ctime,"%Y-%m-%d")
    ctime=datetime.datetime(ctime[0],ctime[1],ctime[2])
    print(ctime)
    timem=[]
    for pi in pathd:
        try:
            ptpd=pd.read_csv('times'+str(pathcount)+'.txt',sep="|")
            ptlist=ptpd.values.tolist()
            for pi in ptlist:
                pi[2]=(pi[2])[:-6]
                pitimef=time.strptime(pi[2], "%a %b %d %H:%M:%S %Y")
                pitimef=datetime.datetime(pitimef[0],pitimef[1],pitimef[2])
                times=pitimef-ctime
                times=times.days
                timem.append(times)
        except BaseException:
            print("wrong")
            timem.append(0)
            pathcount=pathcount+1
        else:
            print("find")
            pathcount=pathcount+1
    os.chdir(cwd)
    print(timem)
    return timem


def gitCID(name):
    pathcount=1
    projectPath = os.path.abspath('data/gitRepo/%s'%(name))
    resd=J.getJMH(name)
    mid=resd[name]
    pathd=mid['path']
    toco=mid['toco']
    cid=[]
    not os.path.isdir(projectPath) and os.makedirs(projectPath)
    cwd = os.getcwd()
    os.chdir(projectPath)
    emptlist=['em','em','em']
    for pi in pathd:
        try:
            ptpd=pd.read_csv('times'+str(pathcount)+'.txt',sep="|",header=None)
            print(ptpd)
            ptlist=ptpd.values.tolist()
            for pl in ptlist:
                cid.append(pl[0])
                print(pl[0])
        except BaseException:
            print("wrong")
            cid.append(0)
            pathcount=pathcount+1
        else:
            print("find")
            pathcount=pathcount+1
    os.chdir(cwd)
    os.chdir(cwd)
    return cid


def gitframe(f,tf):
    #ct=changetimes ac=athuer_count
    fframe={'file':f['path'],'ct':f['ptfl'],'ac':f['ptsl']}
    sframe={'file':f['pttd'].keys(),'act':f['pttl']}
    tframe={'time':tf}
    dff=pd.DataFrame(fframe)
    sdf=pd.DataFrame(sframe)
    tdf=pd.DataFrame(tframe)

    cta=dff['ct'].describe()
    aca=dff['ac'].describe()
    acta=sdf['act'].describe()
    ta=tdf['time'].describe()
    
    #plotdata={'name':f['name'],'des':mean,'mid':mid,'var':sv}
    #print(plotdata)
    ctal=cta.values.tolist()
    acal=aca.values.tolist()
    actl=acta.values.tolist()
    tal=ta.values.tolist()
    result=[[ctal,acal,actl],[tal]]
    
    pframe=pd.DataFrame(result[0])
    pframe.rename(index={0:'changestime',1:'athuercount',2:'athuerchangestime'}, columns={0:'count',1:'mean',2:'std',3:'min',4:'25%',5:'50%',6:'75%',7:'max'}, inplace=True)
    tframe=pd.DataFrame(result[1])
    tframe.rename(index={0:'commitdaysconut'}, columns={0:'count',1:'mean',2:'std',3:'min',4:'25%',5:'50%',6:'75%',7:'max'}, inplace=True)
    print(pframe)
    print(tframe)
    pframe.plot.bar()
    plt.show()
    tframe.plot.bar()
    plt.show()
    return result

def gitplot(name):
    f=gitdata(name)
    t=gittime(name)
    dfra=gitframe(f,t)


#repos = ["apache/cassandra","apache/camel","apache/hive","apache/commons-lang","ReactiveX/RxJava","apache/logging-log4j2"]





for i in repos:
    gitplot(i)
    print('done')
'''
c=gitCID("apache/cassandra")
print(c)
pathcount=1
for ci in c:
    try:
        cmd = 'git log --name-only %s >comid%s.txt' %(ci, str(pathcount))
        result = os.system(cmd)
    except BaseException:
        print("wrong")
        pathcount=pathcount+1
    else:
        print("find")
        pathcount=pathcount+1
'''
'''
pframe=pd.DataFrame(dfra[0])
pframe.rename(index={0:'changestime',1:'athuercount',2:'athuerchangestime'}, columns={0:'count',1:'mean',2:'std',3:'min',4:'25%',5:'50%',6:'75%',7:'max'}, inplace=True)
print(pframe)
pframe.plot.bar()
plt.show()
'''


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
