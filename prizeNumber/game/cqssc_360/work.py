# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

from  game.common import *
from model.Item import *




def handler(job_name='',prizeItem=[]):
    items=[]
    current_issue=0
    #current_date=yesterday
    
    if len(prizeItem)>0:
        current_date=prizeItem[0][1]
        current_issue=prizeItem[0][2]



    try:
        res=requests.get(url=configureRead.getJobValue(job_name,'site_url'),headers=headers,timeout=300)
        

        page_element=etree.HTML(res.text)

        body_node=page_element.xpath('//tbody[@id="data-tab"]/tr')
        
        for node in body_node:
            a=node.xpath('./td/text()')

            numbers=''
            if len(a)>2 and  int(a[0][-3:])>current_issue:

                span=node.xpath('./td/span/text()')
                
                number_tmp=span[0]
                for t in number_tmp:
                    numbers=numbers+','+t
                strong=node.xpath('./td/span/strong/text()')
                stringNumber=strong[0]

                numbers=numbers[1:]+','+stringNumber

                item =PrizeNumberItem()
                item.issue=a[0].replace('-','')
                item.numbers=numbers
                item.ptime=a[1][:-3]
                item.pdate=datetime.datetime.utcnow().strftime(date_format)
                item.source=configureRead.getJobValue(job_name,'site_url')
                item.code=configureRead.getJobValue(job_name,'code')
                item.update_time=datetime.datetime.utcnow().strftime(UTC_FORMAT)
                item.name=configureRead.getJobValue(job_name,'name')
                item.priority=configureRead.getJobValue(job_name,'priority')
                item.job_name=job_name
                item.status=1
                item.printContent()
                items.append(item)

        items.sort(key=lambda item:item.issue, reverse=False)
        return items
    except Exception as e:
        print(str(e))
        return items