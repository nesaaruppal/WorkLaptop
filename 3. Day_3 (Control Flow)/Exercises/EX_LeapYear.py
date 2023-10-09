print("Welcome to the Leap Year calculator!")

year = int(input("Which year would you like to check?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Your year {year} is a leap year!")
        else:
            print(f"Your year {year} is not a leap year!")
    else:
        print(f"Your year {year} is a leap year!")
else:
    print(f"Your year {year} is not a leap year!")
