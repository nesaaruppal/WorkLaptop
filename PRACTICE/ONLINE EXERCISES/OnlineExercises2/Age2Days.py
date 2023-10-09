print("Convert AGE to Days!")

def convert_age(number):
    year_age = int(number)
    months = year_age / 12
    weeks = months * 12
    days = round(weeks * 365)
    print(days)
    
    
convert_age(65)