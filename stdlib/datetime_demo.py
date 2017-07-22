# coding : utf-8

import datetime


# case 1: timedelta&combin
work_day = datetime.datetime.now() - datetime.timedelta(days=1)
print work_day, work_day.date()
work_day = datetime.datetime.combine(work_day, datetime.time(0, 0, 0))
print work_day


other_day = datetime.date(1991, 12, 1)
print other_day
