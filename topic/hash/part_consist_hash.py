# coding: utf-8

ITEMS = 10000000
LOG_NODE = 7
MAX_POWER = 32
NODES = 100

PARTITION = MAX_POWER - LOG_NODE
node_stat = [0 for i in range(NODES)]
ring = []
part2node = {}

def _hash(value):
    from hashlib import md5
    k = md5(str(value)).digest()
    from struct import unpack_from
    ha = unpack_from('>I', k)[0]
    return ha

# 其实这个就是典型的分片思维

for part in range(2 ** LOG_NODE):
    ring.append(part)
    part2node[part] = part % PARTITION


for item in range(ITEMS):
    h = _hash(item) >> PARTITION
    from bisect import bisect_left
    part = bisect_left(ring, h)
    n = part % NODES
    node_stat[n] += 1



# 数据分布情况
print sum(node_stat), node_stat

_ave = ITEMS / NODES
_min = min(node_stat)
_max = max(node_stat)

print 'AVG %s' % _ave
print("Max: %d\t(%0.2f%%)" % (_max, (_max - _ave) * 100.0 / _ave))
print("Min: %d\t(%0.2f%%)" % (_min, (_ave - _min) * 100.0 / _ave))

