import random

# Define a list of targets
targets = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

# Define a function to shoot at the targets
def shoot_targets():
    # Choose a random target
    target = random.choice(targets)
    # Prompt the user to enter their shot
    shot = input(f"Shoot at {target}: ")
    # Convert the user input to an integer
    shot = int(shot)
    # Check if the user hit the target
    if shot == target:
        print(f"You hit the target! The target was {target}.")
    else:
        print(f"You missed the target. The target was {target}.")

# Loop until the user quits
while True:
    # Prompt the user to shoot
    choice = input("Do you want to shoot targets (y/n): ")
    if choice.lower() == "y":
        shoot_targets()
    elif choice.lower() == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter y or n.")