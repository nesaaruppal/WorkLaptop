import pandas as pd

data = pd.read_csv(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day25.py\CSV_Files\weather_data.csv")

monday = data[data.day == "Monday"]
monday_temperature = int(monday.temp)
monday_farenheit = (monday_temperature * 9/5) + 32
print(monday_farenheit)


#CREATE A DATAFRAME 
data_dict = {
    "students": ["James", "Ben", "Adam"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)


#The Dataframe can be converted into a CSV file
data.to_csv("new_data.csv")