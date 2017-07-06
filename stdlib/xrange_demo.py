# coding: utf-8


# 正常使用
for i in xrange(10):
    print i


# 倒叙
# 参数, [40, 0) -1步长
print 'case 2'
for i in xrange(40, 0, -1):
    print i

print 'case 3'
for i in xrange(10, 0, 1):
    print i


print 'case 4'
for i in xrange(1, 10):
    print i,