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
with open('name_all.json','r') as f:
     data = json.load(f)
f.close()
name_list = []
doc = docx.Document()
for x in data['stat_status_pairs']:
    s = x['stat']['question__title']
    name_list.append(s)
with open('leetcode1.txt','w') as f:
    for i,l in enumerate(name_list[::-1]):
        ls =l.replace(' ','-')
        ls =ls.replace('(','')
        ls =ls.replace(')','')
        ls =ls.replace(',','')
        ls =ls.replace(' ','')
        ls = ls.replace("'",'')    
        temp_con = reconfigurl(ls)
        if  not temp_con.startwith('Level up your'):
            con = str(i+1)+','+l+':\n\n'+temp_con.decode('UTF-8')+'\n'
            f.write(con)
            print(i+1)
f.close()

 
#doc.save('demo.docx') 
 