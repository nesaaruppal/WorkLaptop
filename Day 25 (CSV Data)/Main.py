#USING Pandas 
import pandas as pd

data = pd.read_csv(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day25.py\CSV_Files\weather_data.csv")
#print(data['condition'])
#print(type(data))


# Getting DATA in columns
# "data[condition]"
# print(data["condition"])

# Can ALSO use "data.condition"
#final = data.condition
#print(final)



# Getting DATA in rows
#print(data["temp"].max())
#data[data["day"]]
print(data[data.day == "Monday"])

