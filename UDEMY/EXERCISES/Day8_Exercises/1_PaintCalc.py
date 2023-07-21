import math
print("The Paint Area Calculator!")

height = int(input("How tall is your wall in metres?\n"))
width = int(input("How wide is your wall?\n"))

number_of_cans = (height*width) / 5

cans = math.ceil(number_of_cans)

print(f"To paint your wall you will need {cans} cans of paint.")