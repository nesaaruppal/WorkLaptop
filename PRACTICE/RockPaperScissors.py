import random

# Define the list of options for the game
options = ["Rock", "Paper", "Scissors"]

# Define a function to play a round of Rock, Paper, Scissors
print(random.choice(options))


def play_round():
    # Choose a random option from the list
    option = random.choice(options)

    # Print the options and ask the user to choose
    print("Choose from:")
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    choice = int(input("Enter your choice: "))

    # Check if the user's choice is correct
    if choice == len(options):
        print("Invalid choice. Please choose a number between 1 and 3.")
    elif choice == option:
        print("It's a tie!")
    elif (choice - 1) % 3 == (options.index(option) - 1) % 3:
        print("You lose!")
    else:
        print("You win!")


# Play multiple rounds of Rock, Paper, Scissors
print("Rock, Paper, Scissors!")
print("=================")
for i in range(3):
    play_round()
    print("=================")
