print("Welcome to the Python Pizza Deliveries.")

size = input("What size pizza would you like? 'S', 'M' or 'L': ").upper()
add_pepperoni = input("Do you want pepperoni? Type 'Y' for yes and 'N' for no: ").upper()
extra_cheese = input("Do you want extra cheese? Type 'Y' for yes and 'N' for no: ").upper()

bill = 0 

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    
print(f"Your final bill is: £{bill}")