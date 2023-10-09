#with open(r"C:\Users\NUppal\OneDrive - CBRE, #Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day25.py\weather_data.csv") as #weather_data:
#    data = weather_data.readlines()
#    print(data)

import csv

with open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day25.py\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures =[]
    #Creates a CSV OBJECT (data)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)