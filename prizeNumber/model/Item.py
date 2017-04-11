'''
Created on 2017年4月6日

@author: shawn
'''


class PrizeNumberItem():
    def __init__(self, pdate='', issue='', numbers='', name='', ptime='', _code='', source='', update_time='',job_name='',status=''):
        self.pdate = pdate
        self.issue = issue
        self.numbers = numbers
        self.ptime = ptime
        self.source = source
        self.update_time = update_time
        self.code = _code
        self.name = name
        self.job_name=job_name
        self.status=status

    def printContent(self):
        print(self.pdate )
        print(self.issue )
        print(self.numbers )
        print(self.ptime )
        print(self.source )
        print(self.update_time )
        print(self.code )
        print(self.name )


class job_detail():
    def __init__(self, url='', _type='', message='', desc=''):
        self.url = url


class ItemSpiderExcept():
    def __init__(self, url='', _type='', message='', desc=''):
        self.URL = url
        self.Type = _type
        self.Message = message
        self.Desc = desc
