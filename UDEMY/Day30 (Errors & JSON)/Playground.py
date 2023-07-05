import json
with open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day30.py\data.json", mode='r') as data_file:
    data = json.load(data_file)
    data_txt = str(data)
    print(data_txt)