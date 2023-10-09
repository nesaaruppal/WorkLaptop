# USING Twilio for SMS 
# Recovery Code --> (CXUv7LULyAZpIfe7a_Bp3xcYp8AmcdvEGJ-aHV4c)

#Twilio Number
MY_MOBILE = "+447969647356"
GENERATED_MOBILE = "+447700163085"

ACCOUNT_SID = "ACc224850df8f8b74b83ef5c46fb5c2da5"
AUTH_TOKEN = "4506c8ab860356f9d1809dff5bd2838e"

MY_EMAIL = "nesaaruppal@outlook.com"
MY_PASSWORD = "Py0thonK!ng@1997"

from twilio.rest import Client
client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages \
    .create(
        body= "It's going to rain today!",
        from_= GENERATED_MOBILE,
        to=MY_MOBILE
    )

print(message.sid)
print(message.status)