# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(?P<mygroup>\wat) "

test_str = "The fat cat sat on the mat."

matches = re.finditer(regex, test_str, re.IGNORECASE | re.UNICODE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                         end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                         end=match.end(groupNum),
                                                                         group=match.group(groupNum)))

        print 'gourp: ', match.group('mygrou')


m = re.search(regex, test_str)
# print m.

# group 肯定是在括号里的
#