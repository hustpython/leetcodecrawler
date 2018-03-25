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
from LeetCode_test2 import get_content
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
    ls = ls.replace('`','')
    ls = ls.replace('---','-')
    judge = queryMatrix('LeetCode_solu1',l)
    if  not judge :
        try:       
            url = reconfig_solution(ls)
            tem_con =reconfig_pythonsulu(url)
            cont = tem_con[0]      
            best_solu = tem_con[1]
            if cont!=0 :
                python_solution =get_content(cont)
                best_solution = get_content(best_solu)
                title = python_solution[0]
                code = python_solution[1]
                best_title = best_solution[0]
                best_code = best_solution[1]
                con1 ='Python_solution:'+'\n'+title.decode('UTF-8')+'\n'+code.decode('UTF-8')+'\n'+'Best_solution:'+'\n'+best_title.decode('UTF-8')+'\n'+ best_code.decode('UTF-8')+'\n'
                insertData2Table('LeetCode_solu1',i+1,l,con1)
            else:
                print('is 0')
                best_solution = get_content(best_solu)
                best_title = best_solution[0]
                best_code = best_solution[1]
                con2 = 'Best_solution:'+'\n'+best_title.decode('UTF-8')+'\n'+ best_code.decode('UTF-8')+'\n'
                insertData2Table('LeetCode_solu1',i+1,l,con2)
        except IndexError:
            print(ls,l)
            insertData2Table('LeetCode_solu1',i+1,l,0)
    print(i+1)
 