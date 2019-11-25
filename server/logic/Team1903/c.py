import os
def getinfoc():

    c=[]
    repos = [

         "apache/cassandra",
         "apache/camel",
         "apache/hive",
         "apache/commons-lang"
         ]
    for name in repos:
#def gitClone(name):


        a=open('data/gitRepo/%s/log.txt' % (name),encoding='utf-8')

        for line in a.readlines():
           c.append(line)
        a.close()


    return c

