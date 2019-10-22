import datetime
import time

print(datetime.datetime.now())

epoch = 1485789600

print(datetime.datetime.fromtimestamp(epoch))
#           year  month day hour minute  second 
birth_day = (1975,     2, 23,   4,     0, 0,     0 ,0, 0)

birth_day_dt = time.mktime(birth_day)
print(birth_day_dt)

birth_day_date = datetime.date(1975,2,23)

today_date = datetime.date.today()

diff = (today_date - birth_day_date)

print(diff.days/365.24)