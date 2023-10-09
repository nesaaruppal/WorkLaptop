print("Hello! We are going to work out how many weeks, months and years you have if you live to 90!")

age = int(input("How old are you?\n"))

days = 365 * (90 - age)
weeks = 52 * (90 - age)
months = 12 * (90 - age)

print(days)


print(f"You are {age} years old!")
print(f"You have {days} days, {weeks} weeks, and {months} left.")
