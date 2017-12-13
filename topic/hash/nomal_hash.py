# coding: utf-8
from hashlib import md5
from struct import unpack_from

ITEMS = 10000000
NODES = 100

node_stat = [0 for i in range(NODES)]

# 将 item 分配在节点上
for item in range(ITEMS):
    k = md5(str(item))
    h = unpack_from(">I", k)[0]
    n = h % NODES
    node_stat[n] += 1