import datetime as dt
import smtplib
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day32\Exercises\DayMessage\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
        

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("goodmanjoe98@gmail.com", "nenjwxyfhqfwdsyv")
        server.sendmail(
            "goodmanjoe98@gmail.com",
            ["goodmanjoe98@gmail.com"],
            msg=f"Subject: Monday Motivation\n\n{quote}")
  
print("successfully sent email")