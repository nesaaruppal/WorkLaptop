import random

# Define a function to roll a dice


def roll_dice():
    return random.randint(1, 6)


# Prompt the user to enter the number of dice to roll
dice_count = int(input("Enter the number of dice to roll: "))

# Initialize a list to store the results
results = []

# Roll the dice the specified number of times
for i in range(dice_count):
    result = roll_dice()
    results.append(result)

# Print the results
print(results)
