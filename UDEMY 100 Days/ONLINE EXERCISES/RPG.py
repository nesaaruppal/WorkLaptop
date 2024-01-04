import random

# Prompt the user to enter a list of words
words = input("Enter a list of words separated by spaces: ").split()

# Choose a random word from the list
word = random.choice(words)

# Initialize a variable to store the password
password = ""

# Loop through each letter in the word
for letter in word:
    # Choose a random number between 0 and 9
    index = random.randint(0, 9)

    # Add the letter to the password with the random number as a suffix
    password += letter + str(index)

# Print the password
print("Your password is:", password)
