from datetime import datetime
import smtplib
import pandas
import random 

MY_EMAIL = "goodmanjoe98@gmail.com"
MY_PASSWORD = "nenjwxyfhqfwdsyv"



today = datetime.now()
today_tuple = (today.month, today.day)
print(today_tuple)

data = pandas.read_csv(r"UDEMY\Day32\Exercises\DayMessage\Birthdays.csv") 
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path_1 = r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day32\Exercises\DayMessage\letter_templates\letter_1.txt"
    file_path_2 = r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day32\Exercises\DayMessage\letter_templates\letter_2.txt"
    file_path_3 = r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day32\Exercises\DayMessage\letter_templates\letter_3.txt"
    letter_templates = (file_path_1, file_path_2, file_path_3)
    file_path = random.choice(letter_templates)
    
    
    
    
    
with open(file_path) as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[NAME]", birthday_person["name"])
    contents = contents.replace("Angela", "Nesaar")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("goodmanjoe98@gmail.com", "nenjwxyfhqfwdsyv")
    server.sendmail(
        "goodmanjoe98@gmail.com",
        ["goodmanjoe98@gmail.com"],
        msg=f"Subject:Happy Birthday!\n\n{contents}")
print("Email sent!")    

import requests
response = requests.get()




