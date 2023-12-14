from art import logo
import random
print("THE HANGMAN GAME!")
print(logo)


words_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(words_list)
print(f"{chosen_word}")

word_length = len(chosen_word)


display = []
for _ in range(word_length):
    display += "_"
print(display)

game_on = True
while game_on:
    guess = input("Guess a letter: ").lower()
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)