

from datetime import datetime, timedelta


d2 = datetime.now()

d1 = (datetime.now() - timedelta(days=1))


print (d2 - d1).seconds
