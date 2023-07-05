print("Hello! Welcome! This is the BMI Calculator!")

height = (input("How tall are you in metres?\n"))
weight = (input("How much do you weigh in kg?\n"))

height_m = float(height)
weight_kg = int(weight)

BMI = (weight_kg / height_m**2)
round_BMI = int(BMI)
print(f"Your BMI is {round_BMI}.")
