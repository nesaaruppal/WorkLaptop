print("Welcome to the BMI Calculator!")

weight = float(input("What is your weight in Kg?\n"))
height = float(input("What is your height in Metres?\n"))

bmi = (weight / (height*height))

print(f"{weight} / ({height * height}) = {bmi}")

print(round(bmi))