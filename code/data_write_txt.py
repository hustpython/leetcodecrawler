# -*- coding:utf-8 -*-
'''
Created on  
2017年6月28日   下午11:40:37
@author: yzw
'''
from pymongo import MongoClient
connect=MongoClient()
collectname = 'LeetCode_exe'
db = connect['LeetCode']
data = db[collectname]
import sys
reload(sys) 
sys.setdefaultencoding('utf8')
with open('leetcode_database.txt','w') as f:
    for x in data.find().sort("num"):
        con = str(x['num'])+','+x['test_name']+'***'+':\n\n'+x['content'].decode('utf-8')+'\n'
        f.write(con)
f.close()