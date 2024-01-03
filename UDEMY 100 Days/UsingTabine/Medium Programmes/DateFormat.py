from datetime import datetime
def mm_dd_yyyy_to_yyyymmdd(date):
    return date.strftime("%Y%m%d")

print(mm_dd_yyyy_to_yyyymmdd(222024))