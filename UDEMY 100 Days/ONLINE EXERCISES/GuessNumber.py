import random


def play_game():
    # Generate a random number
    secret_number = random.randint(1, 10)

    # Initialize a counter for guesses
    guess_count = 0

    # Loop while the user has not guessed the secret number
    while True:
        # Prompt the user to enter a guess
        guess = input("Enter a guess: ")

        # Convert the guess to an integer
        guess_int = int(guess)

        # Check if the guess is correct
        if guess_int == secret_number:
            # Print a congratulations message
            print(
                f"Congratulations, you guessed the secret number in {guess_count} guesses!")
            break
        elif guess_int > secret_number:
            # Print a message indicating that the guess is too high
            print(f"Your guess is too high. Try again.")
        elif guess_int < secret_number:
            # Print a message indicating that the guess is too low
            print(f"Your guess is too low. Try again.")

        # Increment the guess count
        guess_count += 1


play_game()
