from random import randint, choice, random
# Define the list of options for the game
options = ["Rock", "Paper", "Scissors"]

# Define a function to play a round of Rock, Paper, Scissors


def play_round():
    # Choose a random option from the list
    option = random.choice(options)
    print(option)
    # Prompt the user to choose
    user_choice = input(f"Choose Rock, Paper or Scissors: ").lower()

    # Check if the user's choice is correct
    if user_choice == option:
        print("It's a tie!")
    elif user_choice == options[(options.index(option) + 1) % 3]:
        print("You win!")
    else:
        print("You lose!")


# Play multiple rounds of Rock, Paper, Scissors
print("Rock, Paper, Scissors!")
print("=================")
for i in range(30):
    play_round()
    print("=================")
