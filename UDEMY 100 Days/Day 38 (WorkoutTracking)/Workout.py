import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 180
AGE = 25

APPLICATION_ID = "13d25273"
API_KEY = "4f305dc378fb874c6a908ef730fc3dac"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://docs.google.com/spreadsheets/d/1Sv2VstsYgyOYMdBhtO6j4JM9WPN90WduKv05XACz8SE/edit?pli=1#gid=0"


exercise_text = input("Tell me which exercise you did: ")

parameters = {
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY
}

query = {
    "query": "text"
}




response = requests.post(EXERCISE_ENDPOINT, json=parameters, data=query, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout:":{
            "date": today_date, 
            "time": now_time,
            "exercise": ["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)
    
    print(sheet_response.text)