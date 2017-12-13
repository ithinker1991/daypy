# coding: utf-8

ITEMS = 1000000
NODES = 100

node_stat = [0 for i in range(NODES)]
ring = []

def _hash(value ):
    from hashlib import md5
    k = md5(str(value)).hexdigest()
    from struct import unpack_from
    ha = unpack_from('>I', k)
    return ha

# 每个节点指定一个 key，这些都是离散的点
for n in range(NODES):
    h = _hash(n)
    ring.append(h)
ring.sort()

# 将 item 放到具体的节点上，看 item 的 key 落在 range的那个区间上
for item in range(ITEMS):
    h = _hash(item)
    from bisect import bisect_left

    n = bisect_left(ring, h) % NODES
    node_stat[n] += 1

# 数据分布情况
print sum(node_stat), node_stat

_ave = ITEMS / NODES
_min = min(node_stat)
_max = max(node_stat)

print 'AVG %s' % _ave
print("Max: %d\t(%0.2f%%)" % (_max, (_max - _ave) * 100.0 / _ave))
print("Min: %d\t(%0.2f%%)" % (_min, (_ave - _min) * 100.0 / _ave))