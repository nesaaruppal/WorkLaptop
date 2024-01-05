import sys
import os
from random import choice, random
import csv

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("x       US Presidents       x")
print("x          Quiz             x")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("")


presidents = ["Donald Trump", "Barack Obama", "George W. Bush", "Bill Clinton", "George H.W. Bush", "Ronald Reagan", "Jimmy Carter", "Gerald Ford", "Richard Nixon", "Lyndon B. Johnson", "John F. Kennedy", "Dwight D. Eisenhower", "Harry S. Truman", "Franklin D. Roosevelt", "Herbert Hoover", "Calvin Coolidge", "Warren G. Harding", "Woodrow Wilson", "Howard Taft", "Theodore Roosevelt", "William McKinley", "Grover Cleveland",
              "Benjamin Harrison", "Grover Cleveland", "Chester A. Arthur", "James Garfield", "Rutherford B. Hayes", "Ulysses S. Grant", "Andrew Johnson", "Abraham Lincoln", "James Buchanan", "Franklin Pierce", "Millard Fillmore", "Zachary Taylor", "James K. Polk", "John Tyler", "William Henry Harrison", "Martin Van Buren", "Andrew Jackson", "John Quincy Adams", "James Monroe", "James Madison", "Thomas Jefferson", "John Adams", "George Washington"]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


randomname = random.choice(presidents)
number = presidents.index(randomname)


def namegame():
    while True:
        print("Input the corresponding president's number or press 'N' to quit")
        answer = input(randomname + ": ")
        if answer == "n":
            break
        elif answer == number:
            print("Yay! You got it!")
            clear_screen()
        elif answer != number:
            print("Nope, that's not it!  Try again")
        elif answer != number or "n":
            print("I don't understand")


namegame()
