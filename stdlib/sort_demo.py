# coding: utf-8

dict = {
    1: 'B',
    2: 'A',
    0: 'C'
}
# dict.items 实际上得到的是一个元组列表，所以是对元组排序
print dict.items()

sorted_list = sorted(dict.items(), key=lambda ch: ch[1])

sorted_list = sorted(dict.items(), key=lambda ch: (ch[0], ch[1]), reverse=True)
print sorted_list

com_dict = {
    15: {'code': 'c',
         'value': 4},
    4: {'code': 'b',
        'value': 1},
    2: {'code': 'a',
        'value': 2},
    0: {'code': 'c',
        'value': 4},
    10: {'code': 'c',
         'value': 4}
}

# print com_dict.items()
# com_sorted = sorted(com_dict.items(), key=lambda ch: (ch[1]['value'], ch[1]['code']), reverse=True)
#
#
# for k, v in com_sorted:
#     print k
#     print v
# print com_dict
# com_dict.sort()
# print com_dict

a = com_dict.items()
print a
a.sort(key=lambda ch: (ch[1]['value'], ch[1]['code']))
print a





# print com_sorted
# # k = com_dict.items()
# # print k
# # # print v
# #
# #
# # a, b = k
#
# for k, v in com_dict.items():
#     print k
#     print v.items()
