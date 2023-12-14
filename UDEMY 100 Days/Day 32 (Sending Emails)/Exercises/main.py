import smtplib


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("goodmanjoe98@gmail.com", "nenjwxyfhqfwdsyv")
    server.sendmail(
        "goodmanjoe98@gmail.com",
        ["yeomanssf@gmail.com]"],
        "Hello Yeomans!\n\nYou suck."
)
print("successfully sent email")


# USING DATETIME
#import datetime as dt
#
#current_date = dt.datetime.now()
## Returns FULL date and time 
#year = current_date.year
#month = current_date.month
#day = current_date.day
#hour = current_date.hour
#minute = current_date.minute
#
#day_of_week = current_date.weekday()
#
#print(day_of_week)
#print(year)
#print(month)
#print(day)
#print(hour)
#print(minute)
#
##Create a specific datetime
#date_of_birth = dt.datetime(year=1997, month=10, day=9)
#print(date_of_birth)