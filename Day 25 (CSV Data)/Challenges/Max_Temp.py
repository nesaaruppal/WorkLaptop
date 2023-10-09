import pandas as pd

data = pd.read_csv(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day25.py\CSV_Files\weather_data.csv")

temp = data["temp"].to_list()
print(max(temp))
print(data)
















