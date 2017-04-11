# coding:utf-8
'''
Created on 2017-04-04

@author: shawn
'''

from SpiderThread import SpiderThread
from utils import configureRead
import time



def execute(model_name=''):

    thread = SpiderThread(model_name)
    thread.setDaemon(True)
    thread.start()


if __name__ == "__main__":

    while(True):

        #execute('guanxi11_5')
        for job in  configureRead.get_section():
            execute(job)
        time.sleep(int(configureRead.getCommonValue('concurrent', 'sleepTimeInMainThread')))
