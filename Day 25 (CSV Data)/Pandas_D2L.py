import pandas

data = pandas.read_csv(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day25.py\CSV_Files\weather_data.csv")

#Each column will return as a separate dictionary
data_dictionary = data.to_dict()
print(data_dictionary)


temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))


total_number = 0
for num in temp_list:
    total_number += num
    
average = total_number/len(temp_list)
print(average)
#print(data["temp"].mean())
#print(data["temp"].mode())