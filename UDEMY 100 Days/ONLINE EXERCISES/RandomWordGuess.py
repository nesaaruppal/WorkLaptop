import random

# Define the list of possible words
words = ["hello", "world", "coding", "is", "fun"]

# Choose a random word from the list
word = random.choice(words)

# Initialize a list to store the guessed letters
guessed_letters = []

# Initialize a variable to store the number of incorrect guesses
incorrect_guesses = 0

# Display the hangman
print("_" * 11)
print(" | ".join(["_" for i in range(11)]))
print("_" * 11)

# Loop while the user has not guessed the word and the number of incorrect guesses is less than 6
while "_" in word and incorrect_guesses < 6:
    # Prompt the user to enter a letter
    guess = input("Guess a letter: ")

    # Convert the guess to lowercase
    guess = guess.lower()

    # Check if the guess is a valid letter
    if guess in "abcdefghijklmnopqrstuvwxyz" or guess in guessed_letters:
        # Check if the letter is in the word
        if guess in word:
            # Add the letter to the list of guessed letters
            guessed_letters.append(guess)

            # Display the updated list of guessed letters
            print(" ".join(guessed_letters))

            # Check if the word is fully guessed
            if all(letter in word for letter in guessed_letters):
                # Display the congratulations message
                print("Congratulations, you guessed the word!")
                break
        # Check if the letter is not in the word
        else:
            # Increment the number of incorrect guesses
            incorrect_guesses += 1

            # Display the updated hangman
            print("_" * 11)
            for i in range(incorrect_guesses):
                print(" | ", end="")
            print("_" * 11)
            print(f"Incorrect guess: {guess}")
            print(" ".join(guessed_letters))

            # Display the updated list of incorrect guesses
            if incorrect_guesses == 1:
                print("Missed guess: ")
            elif incorrect_guesses == 2:
                print("Missed guesses: ")
            else:
                print(f"Missed guesses: ")
    # Display an error message if the guess is not a valid letter
    else:
        print("Invalid guess. Please enter a letter.")

# Display the game over message if the user runs out of incorrect guesses or if the word is not guessed
if "_" in word and incorrect_guesses == 6:
    print("Game over. The word was:", word)
elif "_" not in word and incorrect_guesses < 6:
    print("Congratulations, you guessed the word!")
