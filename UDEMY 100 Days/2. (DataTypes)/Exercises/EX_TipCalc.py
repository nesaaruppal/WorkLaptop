print("Welcome to the Tip Calculator!")

bill = float(input("How much was the total bill?\n"))
tip = int(input("How much would you like to add as a tip: 10, 12 or 15?\n"))
people = int(input("How many people are splitting the bill?\n"))

bill_with_tip = (tip / 100 * bill) + bill

per_person = bill_with_tip / people
final_amount = "{:.2f}".format(per_person)

print(f"Each person should pay ${final_amount}.")
