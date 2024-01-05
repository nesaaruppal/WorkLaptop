import datetime

now = datetime.datetime.now()
day_of_week = now.strftime("%A")

days_to_travel = int(input("Enter the number of days to travel: "))

end_date = now + datetime.timedelta(days_to_travel)

end_day_of_week = end_date.strftime("%A")

print(f"Current date: {now.strftime('%m/%d/%Y')}")
print(f"Day of the week: {day_of_week}")
print(f"End date: {end_date.strftime('%m/%d/%Y')}")
print(f"End day of the week: {end_day_of_week}")


# print(now)
