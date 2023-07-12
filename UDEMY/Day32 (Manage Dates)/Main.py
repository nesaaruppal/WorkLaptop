# EMAIL SMTP 
# DATETIME module

#Simple Mail Transfer Protocol 
# Each computer is a post box - each server is a post office 

import smtplib
#Email I've created 

my_email = "nudemy100@gmail.com"
my_password = "rykufcixgwrhlqma"


# Specific for different types of email
connection = smtplib.SMTP("smtp.gmail.com")
#TLS = Transport Layer Security
#Make the connection secure 
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="nudemy100@yahoo.com", msg="Hello")
connection.close()

#smtp.live.com = Hotmail
#smtp.mail.yahoo.com = Yahoo


