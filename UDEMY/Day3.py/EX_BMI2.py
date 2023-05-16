print("Hello and Welcome to your BMI Calculator!")
# BMI is weight in kg squared over their height in m

weight = float(input("How much do you weigh in Kg?\n"))
height = float(input("How tall are you in metres?\n"))

BMI_calc = (weight / (height*height))

BMI = round(BMI_calc)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight!")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are a normal weight!")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight!")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are obese!")
else:
    print(f"Your BMI is {BMI}, you are clinically obese!")
