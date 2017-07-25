# coding: utf-8

from hashlib import md5
from struct import unpack_from

ITEMS = 100000
NODES = 100
VIRTUAL_NODES = 1000
node_stat = [0 for i in range(NODES)]

def _hash(value):
    k = md5(str(value)).hexdigest()
    ha = unpack_from('>I', k)[0]
    return ha

ring = []
hash2node = {}

for n in range(NODES):
    for v in range(VIRTUAL_NODES):
        h = _hash(str(n) + str(v))
        ring.append(h)
        # hash 值实际落在的 node
        hash2node[h] = n
ring.sort()

for item in range(ITEMS):
    h = _hash(str(item))
    from bisect import bisect_left
    # item 在虚节点的位置
    n = bisect_left(ring, h) % (NODES * VIRTUAL_NODES)
    node_stat[hash2node[ring[n]]] += 1

# 数据分布情况
print sum(node_stat), node_stat

_ave = ITEMS / NODES
_min = min(node_stat)
_max = max(node_stat)

print 'AVG %s' % _ave
print("Max: %d\t(%0.2f%%)" % (_max, (_max - _ave) * 100.0 / _ave))
print("Min: %d\t(%0.2f%%)" % (_min, (_ave - _min) * 100.0 / _ave))