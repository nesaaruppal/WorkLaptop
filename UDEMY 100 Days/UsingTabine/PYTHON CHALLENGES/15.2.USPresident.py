import sys
import os
import random
import csv

# Print the scoreboard header


def print_scoreboard_header():
    print("=" * 40)
    print("Scoreboard")
    print("=" * 40)

# Print the scoreboard


def print_scoreboard(scores):
    print_scoreboard_header()
    for index, score in enumerate(scores):
        print(f"{index + 1}. {score['name']} - {score['score']}")
    print("=" * 40)

# Read the high scores from the file


def read_high_scores():
    try:
        with open("high_scores.txt", "r") as file:
            scores = [line.strip() for line in file]
            scores = [eval(score) for score in scores]
    except:
        scores = []
    return scores

# Save the high scores to the file


def save_high_scores(scores):
    with open("high_scores.txt", "w") as file:
        for score in scores:
            file.write(str(score) + "\n")

# Play the game


def play_game():
    presidents = ["Donald Trump", "Barack Obama", "George W. Bush", "Bill Clinton", "George H.W. Bush", "Ronald Reagan", "Jimmy Carter", "Gerald Ford", "Richard Nixon", "Lyndon B. Johnson", "John F. Kennedy", "Dwight D. Eisenhower", "Harry S. Truman", "Franklin D. Roosevelt", "Herbert Hoover", "Calvin Coolidge", "Warren G. Harding", "Woodrow Wilson", "Howard Taft", "Theodore Roosevelt", "William McKinley", "Grover Cleveland",
                  "Benjamin Harrison", "Grover Cleveland", "Chester A. Arthur", "James Garfield", "Rutherford B. Hayes", "Ulysses S. Grant", "Andrew Johnson", "Abraham Lincoln", "James Buchanan", "Franklin Pierce", "Millard Fillmore", "Zachary Taylor", "James K. Polk", "John Tyler", "William Henry Harrison", "Martin Van Buren", "Andrew Jackson", "John Quincy Adams", "James Monroe", "James Madison", "Thomas Jefferson", "John Adams", "George Washington"]
    # Initialize the game variables
    scores = read_high_scores()
    score = 0
    name = input("What is your name? ")
    high_score = scores[0]["score"] if scores else 0

    # Play the game until the user quits
    while True:
        # Print the scoreboard
        print_scoreboard(scores)

        # Get the user's guess
        guess = input(f"{name}, guess a president: ")

        # Check if the user quit
        if guess.lower() == "q":
            return

        # Check if the user's guess is correct
        if guess in presidents:
            score += 1
            if score > high_score:
                high_score = score
            print(f"{name}, you are correct! Your score is {score}.")
        else:
            print(f"{name}, that's not a president. Try again.")

        # Add the user's score to the list of scores
        scores.append({"name": name, "score": score})

        # Save the high scores
        save_high_scores(scores)


# Main program starts here
print("US Presidents Quiz")
print("=" * 20)
play_game()


# Print the scoreboard header

def print_scoreboard_header():
    print("=" * 40)
    print("Scoreboard")
    print("=" * 40)

# Print the scoreboard


def print_scoreboard(scores):
    print_scoreboard_header()
    for index, score in enumerate(scores):
        print(f"{index + 1}. {score['name']} - {score['score']}")
    print("=" * 40)

# Read the high scores from the file


def read_high_scores():
    try:
        with open("high_scores.txt", "r") as file:
            scores = [line.strip() for line in file]
            scores = [eval(score) for score in scores]
    except:
        scores = []
    return scores

# Save the high scores to the file


def save_high_scores(scores):
    with open("high_scores.txt", "w") as file:
        for score in scores:
            file.write(str(score) + "\n")

# Play the game


def play_game():
    # Initialize the game variables
    scores = read_high_scores()
    score = 0
    name = input("What is your name? ")
    high_score = scores[0]["score"] if scores else 0

    # Play the game until the user quits
    while True:
        # Print the scoreboard
        print_scoreboard(scores)

        # Get the user's guess
        guess = input(f"{name}, guess a president: ")

        # Check if the user quit
        if guess.lower() == "q":
            return

        # Check if the user's guess is correct
        if guess in presidents:
            score += 1
            if score > high_score:
                high_score = score
            print(f"{name}, you are correct! Your score is {score}.")
        else:
            print(f"{name}, that's not a president. Try again.")

        # Add the user's score to the list of scores
        scores.append({"name": name, "score": score})

        # Save the high scores
        save_high_scores(scores)


# Main program starts here
print("US Presidents Quiz")
print("=" * 20)
play_game()
