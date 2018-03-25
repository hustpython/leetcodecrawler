# -*- coding:utf-8 -*-
'''
Created on  
2017年6月28日   下午11:40:37
@author: yzw
'''
from pymongo import MongoClient
connect=MongoClient()
collectname = 'LeetCode_solu1'
db = connect['LeetCode']
data = db[collectname]
import sys
reload(sys) 
sys.setdefaultencoding('utf8')
i = 0
with open('leetcode_solu1111.txt','w') as f:
    for x in data.find().sort("num"):
        if x['content'] !=0:
            con = '***'+str(x['num'])+','+x['test_name']+':\n'+x['content'].decode('utf-8')+'\n'
            f.write(con)
            i+=1
            print(i)
f.close()