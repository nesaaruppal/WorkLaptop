# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items-1)
person_paying = names[random_choice]

print(f"The person paying the bill is {person_paying}!")


# Can also use random.choice()
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

person_paying = random.choice(names)
print(f"The person paying is {person_paying}!")
