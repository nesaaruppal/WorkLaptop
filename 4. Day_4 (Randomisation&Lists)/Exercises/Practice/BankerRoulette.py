import random

names_string = input("Give me everybody's names, separated by a comma:\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_of_people = len(names)
random_num = random.randint(0, number_of_people - 1)
payer = names[random_num]

print(f"{payer} is going to buy the meal today!")

