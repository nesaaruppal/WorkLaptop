# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

first_digit = position[0]
second_digit = position[1]

digit1 = int(first_digit)
digit2 = int(second_digit)

positions = []

print(digit1)
print(digit2)

if digit1 == 0:
    row1 = ["⬜️","️⬜️","️⬜️"]



#if first_digit == 2 and second_digit == 3:
    







#column_digit = int(input("Choose a column (1, 2 or 3): "))
#row_digit = int(input("Choose a row (1, 2 or 3): "))

#if column_digit == 2 and row_digit == 1:
#    row1[2] = row1 = ["⬜️","️X","️⬜️"]
#else:
#    print("Guess Again!")




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")