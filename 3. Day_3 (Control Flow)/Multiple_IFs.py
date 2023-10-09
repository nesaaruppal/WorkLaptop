print("Welcome to the Rollercoaster!")
height = int(input("How tall are you in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    photo = input("Would you like a photo? Y for yes and N for no.")
    if photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller.")
