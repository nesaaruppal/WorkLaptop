import requests
from datetime import datetime

USERNAME = "nesaaruppal"
TOKEN = "asty324njoeple!!"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"


##### CREATED PIXELA ACCOUNT #####
# Format of Json --> String and String 

user_params ={
    "token": "asty324njoeple!!",
    "username": "nesaaruppal",
    "agreeTermsofService": "yes",
    "notMinor": "yes"
}
#response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
#print(response.text)



##### REQUEST HEADERS #####
    # "X-USER-TOKEN": [REQUIRED]
    # Makes your API Key/ Token hidden  
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# Authenticating Ourselves
headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"




##### strfttime() #####
    # Pass in a string --> will format the date and time into any format we need
today = datetime(year=2023, month=7, day=30)
pixel_data = {
    # Updating the time --> "strftime"
    #"date": "20230731",
    #'date': today.strftime("%Y%m%d"),
    "quantity": "5.5"
}
#print(today.strftime("%Y%m%d"))



#response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#print(response.text)


##### PUT ##### 
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "500.5"
}

response =requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)



##### DELETE #####
delete_pixel = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_pixel, headers=headers)
print(response.text)