import smtplib

my_email = "nudemy100@gmail.com"
password = "nesaar14"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="nudemy100@yahoo.com", msg="Hello!")
connection.close()