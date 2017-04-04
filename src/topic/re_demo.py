# coding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import re



def exact_tro(title):
    title = u'%s' % title

    # pattern = u'^[\u4E00-\u9FA5\w]+'
    # m = re.search(pattern, title)
    # group_title = m.group() if m else ''
    #
    # pattern2 = u'[\u4E00-\u9FA5\w]+$'
    #
    # group_intro = re.search(pattern2, title)

    print 'title', title
    # pattern = u'相对'
    pattern = u'[\u4E00-\u9FA5\w]+'
    m = re.search(pattern, title)
    group_title = m.group() if m else ''
    print 'group_title', group_title

    # pattern = u'([\u4E00-\u9FA5\w]+)[\)）]{0,1}$'
    pattern = u'([\u4E00-\u9FA5\w]+).?$'

    #
    # pattern = u'([\u4E00-\u9FA5\w]+) ([\u4E00-\u9FA5\w]+)'
    m = re.search(pattern, title)
    # if  m:
    #     print 'g', m.group()
    #     print 'g0', m.group(0)
    #     print 'g1', m.group(1)
    #     print 'g2', m.group(2)
    # else:
    #     print 'no group'

    try:
        print 'g', m.group()
        print 'g0', m.group(0)
        print 'g1', m.group(1)
        # print 'g2', m.group(2)
    except AttributeError, e:
        print str(e), 'no group'

    # print 'g3', m.group(3)
    # abbr = m.group(2) if m else ''
    # print 'abbr', abbr



    # print group_title

def load_local_file(input_f):
    with open(input_f) as input_fd:
        for line in input_fd:
            line = line.strip()
            if line == '':
                continue
            yield line

if __name__ == '__main__':
    # title = u'看得见的中国史 -- 330'
    #
    # title = u'看得见的中国史 -- 330'
    # exact_tro(title)


    gen = load_local_file('/home/ashu/bookforge/src/tmp/test_titles')

    for title in gen:
        exact_tro(title)