# coding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import re


def exact_tro(title):
    title = u'%s' % title
    pattern = u'[\u4E00-\u9FA5\w]+'
    m = re.findall(pattern, title)
    group = m[0]
    abbr = ' '.join(m[1:])

    print 'title', title
    print 'group', group
    print ' abbr', abbr

    # for item in m: print item


    # try:
    #     print 'all', m.groups()
    #     for item in m.groups():
    #         print item
    #     print 'g', m.group(0)
    #     print 'g1', m.group(1)
    #     print 'g2', m.group(2)
    #     print 'g3', m.group(3)
    # except:
    #     print 'no group'

    print '*' * 50

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


    gen = load_local_file('/home/ashu/daypy/tmp/re_data')

    for title in gen:
        exact_tro(title)
