import time 
from datetime import datetime
import datetime

def decalageDate(baseURL, decalage):
    today = datetime.datetime.today()
    
    day = today.day
    year = today.year
    month = today.month

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_days = 29
        else:
            max_days = 28
    else:
        max_days = 30

    if day + decalage > max_days:
        if month + 1 > 12:
            year = year + 1
            month = 1
            day = day + decalage - max_days
            url = baseURL + str(year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)
            print(url)
            return url
        else:
            day = day + decalage - max_days
            url = baseURL + str(year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)
            print(url)
            return url
    else:
        day = day + decalage
        url = baseURL + str(year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)
        print(url)
        return url

