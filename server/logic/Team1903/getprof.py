import profile
import pprint
import pstats
import os
import numpy as np
def getprofW():
 p = pstats.Stats("data/WALinuxAgent/profile/WALinuxAgent_0a849e4311_0.prof")
 stats = p.stats
 #pprint.pprint(stats)
 tt=[]
 n=0
 ncall=0
 ncall1=0
 tttime=0
 for key in stats.keys():
    tu=stats[key]
    tt.append(tu[2])
    ncall=ncall+tu[0]
    n=n+1
    ncall1=ncall1+tu[1]
    tttime=tttime+tu[2]
 L=[]
 L.append(n)
 L.append(ncall)
 L.append(ncall1)
 L.append(tttime/n)
 L.append(float(np.var(tt)))
 L.append(float(np.percentile(tt,25)))
 return L


def getprofT():
 p = pstats.Stats("data/TriFusion/profile/TriFusion_00e5c44d5a_0.prof")
 stats = p.stats
 #pprint.pprint(stats)
 tt=[]
 n=0
 ncall=0
 ncall1=0
 tttime=0
 for key in stats.keys():
    tu=stats[key]
    tt.append(tu[2])
    ncall=ncall+tu[0]
    n=n+1
    ncall1=ncall1+tu[1]
    tttime=tttime+tu[2]
 L=[]
 L.append(n)
 L.append(ncall)
 L.append(ncall1)
 L.append(tttime/n)
 L.append(float(np.var(tt)))
 L.append(float(np.percentile(tt,25)))
 return L
