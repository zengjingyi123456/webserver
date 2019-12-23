import profile
import pprint
import pstats
import os
import numpy as np
print(os.getcwd())
p = pstats.Stats("../../../data/TriFusion/profile/TriFusion_00e5c44d5a_0.prof")
stats = p.stats
#pprint.pprint(stats)
tt=[]
ct=[]
nc=[]
zb=[]
n=0
ncall=0
ncall1=0
tttime=0
for key in stats.keys():
    tu=stats[key]
    tt.append(tu[2])
    ct.append(tu[3])
    nc.append(tu[4])
    ncall=ncall+tu[0]
    n=n+1
    ncall1=ncall1+tu[1]
    tttime=tttime+tu[2]
# print(ct)
# print(tt)
# print(nc)
print("函数个数")
print(n)
print("基本调用次数")
print(ncall)
print("函数调用次数：")
print(ncall1)
print("总运行时间平均值：")
print(tttime/n)
print("总运行时间方差：")
print(float(np.var(tt)))
print("总运行时间四分位数：")
print(float(np.percentile(tt,25)))

#p.strip_dirs().sort_stats("name").print_stats()
