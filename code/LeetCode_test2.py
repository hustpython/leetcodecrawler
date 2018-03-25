# -*- coding:utf-8 -*-
'''
Created on  
2016年10月9日   下午9:15:00
@author: yzw
'''

from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
  
def reconfigurl(name):
    url = 'https://leetcode.com/problems/{}/#/description'.format(name) 
    response = requests.get(url)
    html = BeautifulSoup(response.text)
    
    c = html.find('meta',attrs={'name':'description'}) 
    c =str(c)
    d = replace_html(c)
    return d
def reconfig_solution(name):
    url1 = 'https://leetcode.com/problems/{}/#/solutions'.format(name)
    response = requests.get(url1)
    html = BeautifulSoup(response.text)
    html = str(html)
    c1 = html.rfind('data-forumurl')
    c2 = html.rfind('data-notebbcid')
    d= html[c1:c2]
    d =d.split('=')
    d = d[1][1:-2]
    d2 ='{}/{}'.format(d,name)
    return d2
def reconfig_pythonsulu(url1):
    response = requests.get(url1)
    html = BeautifulSoup(response.text,"html.parser")
    d_temp = html.find_all('a', class_="permalink")
    python_url = []
    total_url =[]
    for i,x in enumerate(d_temp):
        temp_url =d_temp[i]['href']
        index_url = temp_url.rfind('/')
        temp_url = temp_url[:index_url]
        total_url.append(temp_url)
        if 'python' in temp_url:
            python_url.append(temp_url)
    try:
       url_python = 'https://discuss.leetcode.com{}'.format(python_url[0])
    except:
       url_python = 0
    best_url = 'https://discuss.leetcode.com{}'.format(total_url[0])
    return url_python,best_url
def get_content(part_url):
    response = requests.get(part_url)
    html = BeautifulSoup(response.text)
    title = html.title.string
    title = title.split('|')[0]
    try:
        code = html.code.string
    except AttributeError:
        code = 'None'
    return title,code
def replace_html(s):
    s = s.replace('&quot;','"')
    s = s.replace('&amp;','&')
    s = s.replace('&lt;','<')
    s = s.replace('&gt;','>')
    s = s.replace('&nbsp;',' ')
    s = s.replace('&#8594;','→')
    s = s.replace(' - 361way.com','')
    s = s.replace('<meta content="','')
    s = s.replace("<meta content='" ,'')
    s = s.replace('" name="description"/>','')
    s = s.replace('  name="description"/>','')
    s = s.replace(' name="description"/>','')
    return s
'''a =reconfig_solution('two-sum')
parturl= reconfig_pythonsulu(a)[0]
c =get_content(parturl)
print(c)'''
