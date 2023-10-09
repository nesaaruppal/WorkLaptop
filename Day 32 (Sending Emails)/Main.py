# CORRECT WAY TO SEND AN EMAIL

# jamie - mptqvguytqdeirif
# joe - nenjwxyfhqfwdsyv

# jamiestallard639@gmail.com
# Vitamins123!

# goodmanjoe98@gmail.com
# Vitamins123!

import smtplib


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("goodmanjoe98@gmail.com", "nenjwxyfhqfwdsyv")
    server.sendmail(
        "goodmanjoe98@gmail.com",
        ["goodmanjoe98@gmail.com"],
        "Subject: Sup!\n\nI'm sending this through Python haha!"
    )
    print("successfully sent email")









