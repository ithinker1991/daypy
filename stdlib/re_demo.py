# coding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import re


click_regxs = {
    # 图书
    "pub_click_market": (re.compile(r'/hs/static/_track_\?path=/hs/market/publish'), u'图书书城首页', 0),
    "pub_click_banner_1": (re.compile(r'.*_t=ch_427(\.[0-9]+)?\.sld\.0'), u'图书banner图1', 11),
    "pub_click_banner_2": (re.compile(r'.*_t=ch_427(\.[0-9]+)?\.sld\.1'), u'图书banner图2', 12),
    "pub_click_banner_3": (re.compile(r'.*_t=ch_427(\.[0-9]+)?\.sld\.2'), u'图书banner图3', 13),
    "pub_click_banner_4": (re.compile(r'.*_t=ch_427(\.[0-9]+)?\.sld\.2'), u'图书banner图4', 13),
    "pub_click_rank": (re.compile(r'.*/hs/market/rank_publish.*'), u'图书榜单', 20),
    "pub_click_category": (re.compile(r'/hs/static/_track_\?path=/hs/market/cate&.*_t=ch_427\.[0-9]+\.tab\.1'), u'图书分类(old)', 21),
    "pub_click_topic": (re.compile(r'.*/hs/market/channel/552.*_t=ch_427'), u'图书专题', 22),
    "pub_click_bargain": (re.compile(r'.*/hs/static/_track_\?path=/hs/market/channel/393&.*_t=ch_427\.[0-9]+\.tab\.2'), u'图书特价', 23),
    "pub_click_magazine": (re.compile(r'/hs/static/_track_\?path=/hs/market/channel/581&.*_t=ch_427\.[0-9]+\.tab\.3'), u'图书杂志', 24),
    "pub_click_booklist": (re.compile(r'/hs/feed.*_t=ch_427\.[0-9]+\.tab\.4'), u'图书书单', 25),
    "pub_click_hot": (re.compile(r'/hs/static/_track_\?path=/hs/market/channel/402'), u'图书热门推荐', 31),
    "pub_click_free": (re.compile(r'/hs/static/_track_\?path=/hs/market/channel/403'), u'图书免费专区',  32),
    "pub_click_new": (re.compile(r'/hs/static/_track_\?path=/hs/market/new'), u'图书新品专区', 33),
    "pub_click_trumpet_1": (re.compile(r'.*_t=ch_427\.[0-9]+\.anc\.0'), u'图书小喇叭1', 41),
    "pub_click_trumpet_2": (re.compile(r'.*_t=ch_427\.[0-9]+\.anc\.1'), u'图书小喇叭2', 42),
    "pub_click_recommend_1": (re.compile(r'.*_t=ch_427(\.[0-9]+)?\.rec\.b\.0'), u'图书推荐位1', 51),
    "pub_click_recommend_2": (re.compile(r'.*_t=ch_427(\.[0-9]+)?\.rec\.b\.1'), u'图书推荐位2', 52),
    "pub_click_recommend_3": (re.compile(r'.*_t=ch_427(\.[0-9]+)?\.rec\.b\.2'), u'图书推荐位3', 53),
    "pub_click_recommend_4": (re.compile(r'.*_t=ch_427(\.[0-9]+)?\.rec\.b\.3'), u'图书推荐位4', 54),
    "pub_click_recommend_5": (re.compile(r'.*_t=ch_427(\.[0-9]+)?\.rec\.b\.4'), u'图书推荐位5', 55),
    "pub_click_recommend_6": (re.compile(r'.*_t=ch_427(\.[0-9]+)?\.rec\.b\.5'), u'图书推荐位6', 56),
    "pub_click_usertask": (re.compile(r'^/hs/user/task\?.*'), u'图书书币任务',61),
    # "homepage_book_": (re.compile(r'/hs/static/_track_?path=/hs/book/0&source=1&source_id=63cde66807bc11e2b02b00163e0123ac&_data=global13&_t=ch_427.wtf.1.b.0'), u'图书页图书'),
    # "fiction_book_": (re.compile(r'/hs/static/_track_?path=/hs/market/topic/14488&_t=ch_427.wtf.0.n.0*2_14488'), u'图书页专题'),


    # 原创
    "net_click_market": (re.compile(r'/hs/static/_track_\?path=/hs/market/fiction'), u'原创书城首页', 0),
    "net_click_banner_1": (re.compile(r'.*_t=(ch_444|ch437)\.([0-9]+\.)?sld\.0'), u'原创banner图1', 11),
    "net_click_banner_2": (re.compile(r'.*_t=(ch_437|ch_444)\.([0-9]+\.)?sld\.1'), u'原创banner图2', 12),
    "net_click_banner_3": (re.compile(r'.*_t=(ch_437|ch_444)\.([0-9]+\.)?sld\.2'), u'原创banner图3', 13),
    "net_click_category": (re.compile(r'/hs/static/_track_\?path=/hs/market/cate&.*_t=(ch_437|ch_444)\.[0-9]+\.tab\.1'), u'原创分类(old)', 20),

    "net_click_rank": (re.compile(r'/hs/market/rank_original\?.*_t=(ch_437|ch_444)\.[0-9]+\.tab\.0'), u'原创榜单', 21),
    # "net_click_topic": (re.compile(r'/hs/market/topic[lL]ist/fiction.*_t=(ch_437|ch_444).*'), u'原创专题', 22),
    "net_click_topic": (re.compile(r'.*/hs/market/topicList/fiction.*_t=(ch_437|ch_444)\.[0-9]\.tab\.[0-9].*'), u'原创专题', 22),
    "net_click_boy": (re.compile(r'/hs/static/_track_\?path=/hs/market/channel/405&.*_t=ch_[0-9]+\.[0-9]+\.tab\.2'), u'原创男生专区', 23),
    "net_click_girl": (re.compile(r'/hs/static/_track_\?path=/hs/market/channel/406&.*_t=ch_[0-9]+\.[0-9]+\.tab\.3'), u'原创女生专区', 24),
    "net_click_booklist": (re.compile(r'/hs/feed&user_type.*_t=(ch_444|ch_437)\.[0-9]+\.tab\.[0-9]+'), u'原创书单', 34),
    # "net_click_comic": (re.compile(r'/hs/static/_track_\?path=/hs/market/comic.*_t=ch_[0-9]+\.[0-9]+\.tab\.4'), u'原创漫画', 25),

    "net_click_free": (re.compile(r'/hs/static/_track_\?path=/hs/market/channel/394&.*_t=ch_[0-9]+\.[0-9]+\.tpc\.0'), u'原创免费及特价', 31),
    "net_click_hot": (re.compile(r'/hs/static/_track_\?path=/hs/market/channel/464&.*_t=ch_[0-9]+\.[0-9]+\.tpc\.1'), u'原创热门', 32),
    "net_click_whole": (re.compile(r'/hs/static/_track_\?path=/hs/market/channel/401&.*_t=ch_[0-9]+\.[0-9]+\.tpc\.2'), u'原创完本', 33),
    "net_click_trumpet_1": (re.compile(r'.*_t=(ch_444|ch_437)\.[0-9]+\.anc\.0'), u'原创小喇叭1', 41),
    "net_click_trumpet_2": (re.compile(r'.*_t=(ch_444|ch_437)\.[0-9]+\.anc\.1'), u'原创小喇叭2', 42),
    "net_click_recommend_1": (re.compile(r'.*_t=(ch_444|ch_437)(\.[0-9]+)?\.rec\.b\.0'), u'原创推荐位1', 51),
    "net_click_recommend_2": (re.compile(r'.*_t=(ch_444|ch_437)(\.[0-9]+)?\.rec\.b\.1'), u'原创推荐位2', 52),
    "net_click_recommend_3": (re.compile(r'.*_t=(ch_444|ch_437)(\.[0-9]+)?\.rec\.b\.2'), u'原创推荐位3', 53),
    "net_click_recommend_4": (re.compile(r'.*_t=(ch_444|ch_437)(\.[0-9]+)?\.rec\.b\.3'), u'原创推荐位4', 54),
    "net_click_recommend_5": (re.compile(r'.*_t=(ch_444|ch_437)(\.[0-9]+)?\.rec\.b\.4'), u'原创推荐位5', 55),
    "net_click_recommend_6": (re.compile(r'.*_t=(ch_444|ch_437)(\.[0-9]+)?\.rec\.b\.5'), u'原创推荐位6', 56),
    "net_click_usertask": (re.compile(r'(^/hs/user/task\?.*)'),u'原创书币任务', 61),
    #"net_click_cate1": (re.compile(r'/hs/static/_track_\?path=/hs/market/cate/fiction/.*_t=(ch_437|ch_444)\.6\.cate\.0.*'), u'原创分类1', 34),
    #"net_click_cate2": (re.compile(r'/hs/static/_track_\?path=/hs/market/cate/fiction/.*_t=(ch_437|ch_444)\.6\.cate\.1.*'), u'原创分类2', 35),

    # 漫画
    "comic_click_market": (re.compile(r'/hs/static/_track_\?path=/hs/market/comic'), u'漫画书城首页', 0),
    "comic_click_banner_1": (re.compile(r'.*_t=ch_595\.[0-9]+\.sld\.0'), u'漫画banner图1', 11),
    "comic_click_banner_2": (re.compile(r'.*_t=ch_595\.[0-9]+\.sld\.1'), u'漫画banner图2', 12),
    "comic_click_banner_3": (re.compile(r'.*_t=ch_595\.[0-9]+\.sld\.2'), u'漫画banner图3', 13),
    "comic_click_trumpet_1": (re.compile(r'.*_t=ch_595\.[0-9]+\.anc\.0'), u'漫画小喇叭1', 41),
    "comic_click_trumpet_2": (re.compile(r'.*_t=ch_595\.[0-9]+\.anc\.1'), u'漫画小喇叭2', 42),

    "comic_click_rank": (re.compile(r'/hs/static/_track_\?path=/hs/market/comic_topic/.*_t=ch_595'), u'漫画排行榜', 23),
    "comic_click_store": (re.compile(r'/hs/static/_track_\?path=/hs/market/channel/599&_t=ch_595'), u'漫画铺子', 24),
    "comic_click_update": (re.compile(r'/hs/static/_track_\?path=/hs/market/comic_update'), u'漫画日更表', 25),

    "comic_click_recommend_1": (re.compile(r'.*native_immersive=1&_t=ch_595\.4\.b\.0'), u'漫画强势安利1', 51),
    "comic_click_recommend_2": (re.compile(r'.*native_immersive=1&_t=ch_595\.4\.b\.1'), u'漫画强势安利2', 52),
    "comic_click_recommend_3": (re.compile(r'.*native_immersive=1&_t=ch_595\.4\.b\.2'), u'漫画强势安利3', 53),
    "comic_click_recommend_4": (re.compile(r'.*native_immersive=1&_t=ch_595\.4\.b\.3'), u'漫画强势安利4', 54),
}

# "net_click_market": (re.compile(r'/hs/static/_track_\?path=/hs/market/fiction'), u'原创书城首页', 0),
# uri = '/hs/static/_track_?path=/hs/market/fiction'
# for key in click_regxs.keys():
#     ret = click_regxs[key][0].search(uri)
#     if ret:
#         print click_regxs[key][1]
#     print ret



with open('/home/ashu/daypy/data/test_re.txt') as fd:
    pattern = re.compile(r'.*_t=(ch_444|ch_437)(\.[0-9]+)?\.rec\.b\.3')
    i, j= 0, 0
    for line in fd:
        j +=1
        id, uri = line.strip().split()
        m = pattern.match(uri)
        if m:
            i += 1
            print '---' * 100
            print uri
            print m.group(0)
        else:
            print uri


    print j, i





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


    # gen = load_local_file('/home/ashu/daypy/tmp/re_data')

    # for title in gen:
    #     exact_tro(title)
    pass
