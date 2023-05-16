print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower
name2 = input("What is their name? \n").lower

name1_letters = 0

for letter in name1:
    if letter == "T":
        name1_letters += 1
        if letter == "R":
            name1_letters += 1
            if letter == "U":
                name1_letters += 1
                if letter == "E":
                    name1_letters += 1

name2_letters = 0

for letters in name2:
    if letters == "L":
        name2_letters += 1
        if letters == "O":
            name2_letters += 1
            if letters == "V":
                name2_letters += 1
                if letters == "E":
                    name2_letters += 1

print(name1_letters)
print(name2_letters)
