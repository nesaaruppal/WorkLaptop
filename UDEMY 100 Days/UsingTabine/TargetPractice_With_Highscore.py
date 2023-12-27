import random
import pickle

# Define a list of targets
targets = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

# Load the highscores from the file
with open("highscores.dat", "rb") as file:
    highscores = pickle.load(file)

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
        # Update the highscores if the user hit the target
        if len(highscores) == 0 or shot > highscores[-1][1]:
            highscores.append((your_name, shot))
        # Save the highscores back to the file
        with open("highscores.dat", "wb") as file:
            pickle.dump(highscores, file)
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
        # Print the highscores and save them back to the file
        with open("highscores.dat", "wb") as file:
            pickle.dump(highscores, file)
        print("Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter y or n.")