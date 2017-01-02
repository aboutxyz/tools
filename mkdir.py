#coding:utf-8
'''
20170901-20171231
'''
import os
import datetime
import time
def dateRange(start, end): 
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1 
    return [datetime.datetime.strftime(datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(i), "%Y%m%d") for i in xrange(days)]
if __name__ == '__main__':
    for i in dateRange("2017-01-01", "2017-12-31"):
        os.mkdir(i)
    


