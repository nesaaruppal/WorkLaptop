# Specific piece of information based on provided information

# ISS location API is very simple
# SUNRISE AND SUNSET TAKES PARAMETERS

# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400

import requests
import datetime
# Specified in the API Documentation
MY_LAT = 36.093788
MY_LONG = -95.892578

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
#print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
new_sunrise = sunrise.split("T")[1].split(":")[0]
new_sunset = sunset.split("T")[1].split(":")[0]

print(new_sunrise)
print(new_sunset)

current_time = datetime.datetime.now()
current_hour = current_time.hour
print(current_hour)

print(f"The sunrises at {new_sunrise} and sets and {new_sunset}. The current hour of the day is {current_hour}.")