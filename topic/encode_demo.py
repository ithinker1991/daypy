# coding: utf-8


# # case1
# s = '中文'
# print s
# print '中文'
#
# # 中文
# try:
#     print s.decode('utf-8')
#     print s.decode('gb2312')
# except UnicodeDecodeError, e:
#     print str(e)
#
# # s1 = s.decode('utf-8')
# # print s1.encode('gb2312')
# #
# #
# # print (u'中文', u'123')
# # print str((u'中文', u'123'))
#
s0 = u'中文'
s = (u'中文', u'123')

s1 = str((u'中文', u'123'))
s2 = '中文'
s3 = ('中文', '123')
s4 = str(s3).encode('utf-8')
s5 = str(s3).decode('utf-8')
s6 = str(s3)


print 's0', s0
print 's', s
print 's1', s1
print 's2', s2
print 's3', str(s3).decode('utf-8')
print 's3 1', str(s3).encode('utf-8')
print 's3 2', s3
# print 's3 3', u'%s' % s3


for item in s:
    print item


for item in s3:
    print item