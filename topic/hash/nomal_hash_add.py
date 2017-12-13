# coding: utf-8

'''正常 hash 算法的实现'''




from hashlib import md5
from struct import unpack_from
from bisect import bisect_left


ITEMS = 10000000
NODES = 100
NEW_NODES = 101


def _hash(value):
    k = md5(str(value)).digest()
    ha = unpack_from(">I", k)[0]
    return ha

ring = []
new_ring = []
change = 0

for item in range(ITEMS):
    h = _hash(item)
    n = h % NODES
    new_n = h % NEW_NODES

    if n != new_n:
        change += 1

print change

print "Change: %d\t(%0.2f%%)" % (change, change * 100.0 / ITEMS)