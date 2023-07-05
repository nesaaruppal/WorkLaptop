print("Welcome to the rollercoaster!")

bill = 0

height = int(input("What is your height in cm?\n"))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("You are too short to ride the rollercoaster!")

age = int(input("How old are you?"))

if age < 10:
    print("The ticket price is £5.")
    bill += 5
elif age < 15:
    print("The ticket price is £10.")
    bill += 10
else:
    print("The ticket price is £20") 
    bill += 20

want_ticket = input("Would you like to buy a ticket for the price of £5? Type 'Y' for yes and 'N' for no: ")

if want_ticket == 'Y':
    bill += 5
    print(f"The total price is {bill}.")
else:
    print(f"This total bill is {bill}.")

