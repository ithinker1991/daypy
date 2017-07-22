# coding: utf-8

import time
from datetime import datetime

# datetime -> str
sdatetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print 'datetime -> str:', datetime.now(), '->', sdatetime

# str 转 时间
s = '2017-07-03 16:00:29'
d = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
print d

# 将时间戳转时间
tp = 1493049615012 / 1000
tp = 1493049446273 / 1000
tp = 1493049615096 / 1000
time_local = time.localtime(tp)
print time_local


# 转换时间格式 -> str
day = time.strftime('%Y%m%d', time_local)
hour = time.strftime('%H', time_local)
print day
print hour

localtime = time.localtime(time.time())
print u"本地时间为 :", localtime

s1 = '24/Apr/2017:23:55:57'
# s2 = '24/Apr/2017:23:55'
# print len(s1)
print len(s1)
# a = time.strptime(s1, '%d/%b/%Y:%H:%i:%s')
a = time.strptime(s1, '%d/%b/%Y:%H:%M:%S')

day = time.strftime('%Y%m%d', a)
hour = time.strftime('%H', a)
print day
print hour
