

from hashlib import md5
from struct import unpack_from, pack


value = '1'

h = md5(value)

print h
print h.digest()
print h.hexdigest()
k = h.hexdigest()

print k, type(k)
print unpack_from('>Ii', k)

print len(k)


print unpack_from('>Iiiiiiihh', k)

print 128 / 8


a = 1
b = 8
c = 16
str1 = pack('>iii', a, b, c)
str2 = pack('iii', a, b, c)

print str1
print str2
print repr(str1)
print repr(str2)