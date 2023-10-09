print("Hello and welcome to the Odd or Even Calculator.")

number = int(input("Type a number to check whether it's odd or even:\n"))

if number % 2 == 0:
    print(f"Your number {number} is even!")
elif number % 2 == 1:
    print(f"Your number {number} is odd!")
elif number == 1:
    print("Your number is odd!")
else:
    print("Please enter the number you would like to check!")
