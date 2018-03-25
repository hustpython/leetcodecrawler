# -*- coding:utf-8 -*-
'''
Created on  
2017年6月27日   下午9:52:43
@author: yzw
'''
import json
import docx
from LeetCode_test2 import reconfigurl
# encoding=utf8 
import sys
reload(sys) 
sys.setdefaultencoding('utf8')
from database_leetcode import insertData2Table,queryMatrix
with open('name_all.json','r') as f:
     data = json.load(f)
f.close()
name_list = []
doc = docx.Document()
for x in data['stat_status_pairs']:
    s = x['stat']['question__title']
    name_list.append(s)

for i,l in enumerate(name_list[::-1]):
    ls =l.replace(' ','-')
    ls =ls.replace('(','')
    ls =ls.replace(')','')
    ls =ls.replace(',','')
    ls =ls.replace(' ','')
    ls = ls.replace("'",'')
    ls = ls.replace("`",'')     
    judge = queryMatrix('LeetCode_exe',l)
    if  not judge:
        con = reconfigurl(ls).decode('UTF_8')
        if not con.startswith('Level up your'):
           insertData2Table('LeetCode_exe',i+1,l,con)
        else:
            print(i+1,l)
    print(i+1)
 
 