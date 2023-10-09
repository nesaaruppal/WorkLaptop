# API Keys, Authentication, Environment Variables, Sending SMS

# API AUTHENTICATION
    # API KEY 
    # Tracks how much you use their API
    
# This works!
# https://api.openweathermap.org/data/2.5/weather?q=London,%20UK&appid=69f04e4613056b159c2761a9d9e664d2

#Twilio Information
MY_MOBILE = "+447969647356"
GENERATED_MOBILE = "+447700163085"

ACCOUNT_SID = "ACc224850df8f8b74b83ef5c46fb5c2da5"
AUTH_TOKEN = "4506c8ab860356f9d1809dff5bd2838e"

MY_EMAIL = "nesaaruppal@outlook.com"
MY_PASSWORD = "Py0thonK!ng@1997"


import requests
from twilio.rest import Client

API_KEY = "69f04e4613056b159c2761a9d9e664d2"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 36.093788,
    "lon": -95.892578,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# SLICE FUNCTION
    # a[start:stop] --> Item start and stop at "stop -1"
    # a[start:] --> Items start through the rest of the array 
    # a[:stop] --> Items from the beginning to "stop -1"
    # a[:] --> A copy of the whole array


# This produces the weather data for the first 12 hours (remember it starts at 0 so we use the SLICE and set it to 12.)
weather_slice = weather_data["hourly"][:12]
#print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 802: 
        will_rain = True 
        
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body= "It's going to rain today!",
            from_=GENERATED_MOBILE,
            to=MY_MOBILE
        )
    
    print(message.status)