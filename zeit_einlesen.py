import datetime

d = "1956-2-2"

year = d[0:4]
month = d[5:7]
day = d[8:] 

date_elements = [int(x) for x in d.split('-')]

[y,m,d] = [int(x) for x in d.split('-')]
print(date_elements)

print(y, m, d)
birth_day_date = datetime.date(y, m, d)
# (1956,2,23)