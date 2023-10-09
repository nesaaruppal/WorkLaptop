import pandas

data = pandas.read_csv(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day25.py\SquirrelCensus\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


gray = []
cinnamon = []
black = []

fur_colour = data["Primary Fur Color"]

for colour in fur_colour:
    if colour == "Gray":
        gray.append("Gray")
    elif colour == "Cinnamon":
        cinnamon.append("Cinnamon")
    elif colour == "Black":
        black.append("Black")

number_of_gray = gray.count("Gray")
#print(number_of_gray)
number_of_cinnamon = cinnamon.count("Cinnamon")
#print(number_of_cinnamon)
number_of_black = black.count("Black")
#print(number_of_black)

colour_data = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [number_of_gray, number_of_cinnamon, number_of_black]
}

df = pandas.DataFrame(colour_data)

df.to_csv("squirrel_count2.csv")


#gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
#gray_squirrels_COUNT = len(data[data["Primary Fur Color"] == "Gray"]) 

#data_dict = {
#    "Fur Colour": ["Gray", "Cinnamon", "Black"],
#    "Count": [number_of_gray, number_of_cinnamon, #number_of_black]
#}