# -*- coding:utf-8 -*-
'''
Created on  
2017年6月27日   下午9:52:43
@author: yzw
'''
import json
import docx
from LeetCode_test2 import reconfigurl
from LeetCode_test2 import reconfig_solution
from LeetCode_test2 import reconfig_pythonsulu
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
with open('leetcodeans.txt','w') as f:
    for i,l in enumerate(name_list[::-1]):
        ls =l.replace(' ','-')
        ls =ls.replace('(','')
        ls =ls.replace(')','')
        ls =ls.replace(',','')
        ls =ls.replace(' ','')
        ls = ls.replace("'",'')
        try:       
            url = reconfig_solution(ls)
            tem_con =reconfig_pythonsulu(url)
            cont = tem_con[0]        
            best_solu = tem_con[1]
            if cont[0]!=0 :
                con = str(i+1)+','+l+':\n'+'Python_solution:'+'\n'+cont[1].decode('UTF-8')+'\n'+cont[2].decode('UTF-8')+'\n'
                f.write(con)
            if cont[0]==0 and best_solu[0]!=0:
                con = str(i+1)+','+l+':\n'+'Best_solution:'+'\n'+best_solu[0].decode('UTF-8')+'\n'+best_solu[1].decode('UTF-8')+'\n'
                f.write(con)
        except IndexError:
            pass
        print(i+1)
f.close()

 
#doc.save('demo.docx')  