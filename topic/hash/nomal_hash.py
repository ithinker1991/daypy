# coding: utf-8

'''正常 hash 算法的实现'''




from hashlib import md5
from struct import unpack_from
from bisect import bisect_left


ITEMS = 10000000
NODES = 100
NEW_NODES = 101


def hash(value):
    k = md5(str(value)).digest()
    ha = unpack_from(">I", k)[0]
    print '-' * 100
    for i in unpack_from(">I", k):
        print i
    # print ha
    return ha

ring = []
new_ring = []

for n in range(NODES):
    ring.append(hash(n))


ring.sort()

for n in range(NEW_NODES):
    new_ring.append(hash(n))

new_ring.sort()
change = 0

for item in range(ITEMS):
    h = hash(item)
    n = bisect_left(ring, h) % NODES
    new_n = bisect_left(new_ring, h) % NEW_NODES
    if n != new_n:
        change += 1

print change