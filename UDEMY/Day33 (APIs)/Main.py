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
    
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
    



    
