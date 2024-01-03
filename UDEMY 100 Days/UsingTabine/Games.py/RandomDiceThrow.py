import random

# Define the number of dice and sides
dice_count = 2
dice_sides = 6

# Roll the dice
rolls = []
for i in range(dice_count):
    rolls.append(random.randint(1, dice_sides))

# Print the results
print(f"You rolled {', '.join([str(r) for r in rolls])}.")