import requests
from datetime import datetime 

USERNAME = "nezuppal"
TOKEN = "oauefauerar213221efw"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph2"

##### CREATE ACCOUNT #####
account_params = {
    "token": TOKEN, 
    "username": USERNAME, 
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#response = requests.post(url=PIXELA_ENDPOINT, json=account_params)
#print(response.text)

##### CREATE GRAPH #####
headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "graph2",
    "name": "Reading Tracker",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu"
}
#response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, #headers=headers)
#print(response.text)


##### VIEW GRAPH #####
nezuppal_graph = "https://pixe.la/v1/users/nezuppal/graphs/graph2.html"


##### ADD DATA #####
create_pixels = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

# Change the date or the quantity to add new data 
pixel_data = {
    "date": "20230726",
    "quantity": "10"
}

response = requests.post(url=create_pixels, json=pixel_data, headers=headers)
print(response.text)

