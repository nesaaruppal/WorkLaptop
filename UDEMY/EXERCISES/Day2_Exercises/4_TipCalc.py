print("Welcome to the Tip Calculator!")

num_people = int(input("How many people are sharing the bill?\n"))
price = int(input("How much did the meal cost?\n£"))
tip = 1.12

each_person_pays = (price/num_people) * tip 
final_price = round(each_person_pays, 2)

print(f"Each person should pay £{final_price:.2f}!")