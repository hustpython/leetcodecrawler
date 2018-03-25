# -*- coding:utf-8 -*-
from pymongo import MongoClient

def insertData2Table(collectname,num,test_name,content):
        '''insert one data to collection'''
        
        connect=MongoClient()
        db = connect['LeetCode']
        data = db[collectname]
        
        
        try:    
            datum = {           
                'num' : num,
                'test_name':test_name,
                'content' :content
            }
            data.insert_one(datum)
        except:
            print u'数据存储失败，请检查数据格式'
def queryMatrix(collectname,value):
        '''根据变量矩阵查询表'''
        try:
            connect=MongoClient()
            db = connect['LeetCode']
            data = db[collectname]           
            query_result = data.find_one({'test_name':value})
            
        except:
            return 
        return query_result