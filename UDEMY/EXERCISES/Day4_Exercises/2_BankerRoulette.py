import random
print("Banker Roulette!")

names_string = input("Enter everyones names, separated by a comma and a space:\n")
names = names_string.split(", ")

number_names = len(names)
person = random.randint(0, number_names - 1)

print(f"{names[person]} is going to buy the meal today!")