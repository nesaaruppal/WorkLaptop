from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    """Takes the account data and returns a printable format."""
    account_name = account["name"]
    account_description = account ["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_description}, from {account_country}!")

def check_answer(guess, a_followers, b_followers):
    """Take user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()



    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls')
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Your current score is {score}!")
    else:
        print(f"Sorry! You're wrong! Final score: {score}.")
        game_should_continue = False