import profile
import pprint
import pstats
import os


def getzb():

 p = pstats.Stats("data/TriFusion/profile/TriFusion_00e5c44d5a_0.prof")
 stats = p.stats
 zb=[]
 n=0
 ncall=0
 ncall1=0
 tttime=0

 for key in stats.keys():
    tu=stats[key]

    ncall=ncall+tu[0]
    n=n+1
    ncall1=ncall1+tu[1]
    tttime=tttime+tu[2]
    zb.append(tu[4])
    zb.append(tu[2]/2.0961880000000006)

 return zb


 time=[]
 p = pstats.Stats("data/TriFusion/profile/TriFusion_00e5c44d5a_0.prof")
 stats = p.stats
 for key in stats.keys():
    tu=stats[key]
    time.append(tu[0])

