# coding:utf-8
'''
Created on 2017-10-13

@author: shawn
'''


import requests
import re
from lxml import etree
from utils import configureRead
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36'}


class prizeNotice():
   
    

    def __init__(self,url):
        self.url=configureRead.getCommonValue('concurrent',url)
        
        

    def notice_to_draw_server(self,items):
        for item in items:
            self._notice_to_draw_server(item)
            
    def _notice_to_draw_server(self,item):
        server_url=self.url+"?code="+item.code+"&&issueAlias="+item.issue
        res=requests.post(url=server_url,headers=headers,timeout=300)
        print(res.text)
        
        
