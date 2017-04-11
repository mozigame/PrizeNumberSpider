# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''
from threading import Thread
from time import sleep
from random import randint
import imp
import time

from store import spiderRecord4DB
from utils import configureRead
import sys

class SpiderThread(Thread):
    """docstring for MyThread"""
    def __init__(self, name):
        super(SpiderThread, self).__init__()
        self.name = name       
    def run(self):
            while(True):
                
                current_prize_number=spiderRecord4DB.getCurrentPrizeNumberFromDB(self.name)
                fp, pathname, description = imp.find_module('work',['./game/'+self.name])
                try:
                    m = imp.load_module(self.name+"_work", fp, pathname, description)
                    items=m.handler(self.name,current_prize_number)
                    if(len(items)>0):
                        spiderRecord4DB.batchInsert(items)
                finally:
                    if fp:
                        fp.close()
                time.sleep(int(configureRead.getJobValue(self.name, 'sleepTimeInThread')))



    
       