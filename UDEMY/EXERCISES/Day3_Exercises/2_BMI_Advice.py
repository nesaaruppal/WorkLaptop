print("Let's work out your BMI!")

weight = float(input("How much do you weigh in Kg?\n"))
height = float(input("How tall are you in metres?\n"))

bmi = round(weight / (height * height))

if bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese!")
elif bmi > 30:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 25:
    print(f"Your BMI is {bmi}, you are slightly overweight!")
elif bmi >= 18.5:
    print(f"Your BMI is {bmi}, you are a normal weight.")
else:
    print(f"Your BMI is {bmi}, you are underweight)")