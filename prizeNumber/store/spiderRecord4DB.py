# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

from utils.mysql import *


def getCurrentPrizeNumberFromDB(jobName):
    db = MySQLDB('job')
    sql = "select * from PrizeNumberItem where id in(SELECT max(id) from PrizeNumberItem where job_name='"+jobName+"');"
    db.query(sql);
    result = db.fetchAllRows();
    db.close()
    return result



def batchInsert(items):
    
    db = MySQLDB('job')
    sql='insert into PrizeNumberItem(pdate,issue,numbers,ptime,source,update_time,code,name,job_name,status,priority) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    tmpItem=[]
    for e in items:
        tmpItem.append((e.pdate,e.issue,e.numbers,e.ptime,e.source,e.update_time,e.code,e.name,e.job_name,e.status,e.priority))
    db.batchInsert(sql,tmpItem)
    db.close()
    
def batchUpdate(items):
    
    db = MySQLDB('lottery')
    sql='update lp_prize_number_item set numbers=%s where code=%s and issue_alias=%s'
    tmpItem=[]
    for e in items:
        tmpItem.append((e.numbers,e.code,e.issue))
    db.batchInsert(sql,tmpItem)
    db.close()    
    
    



