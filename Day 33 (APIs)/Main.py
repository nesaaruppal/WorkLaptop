# APIs
# Application Programming Interfaces
    # Set of Commands, Functions, Protocols and Objects
    # Used to create software
    # Used to interact with an external system
    
# API Endpoint
    # LOCATION
    # e.g. api.coinbase.com
    
# API Requests
    # Withdrawing data 
    # Like withdrawing money 
    
# Chrome Extension - JSON Viewer Pro
    # Can enter the URL for the website's API into another tab
    # E.g. http://api.open-notify.org/iss-now.json
    # Json will format this data into a dictionary
    
# Download modules
    # git clone https://github.com/psf/requests.git
    

    
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.raise_for_status())

data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)