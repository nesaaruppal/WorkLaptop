from art import logo
import random

deck_cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def deal_cards():
    """Deal 2 random cards from the deck for the user and the computer."""
    for _ in range(2):
        user_cards.append(random.choice(deck_cards))
        computer_cards.append(random.choice(deck_cards))

def calculate_score(deck_cards):
    """Takes the cards and returns the winner and score!"""
    if user_cards == 21 and len(user_cards) == 2:
        return 0
    elif computer_cards == 21 and len(computer_cards) == 2:
        return 0
    elif user_cards > 21 and 11 in user_cards:
        user_cards.remove(11)
        user_cards.append(1)
    elif computer_cards > 21 and 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)
    elif user_cards == computer_cards:
        return "DRAW!"
    elif user_cards > computer_cards:
        return "You win!"
    else:
        return "You lose!"

def deal_new_card():
    for _ in range(1):
        user_cards.append(random.choice(deck_cards))
    
def computer_plays():
    if sum(computer_cards) < 17:
        computer_cards.append(random.choice(deck_cards))
    elif sum(computer_cards) >= 18:
        return computer_cards

def compare_scores():
    if sum(user_cards) > 21:
        print("You went over 21! YOU LOSE!")
    elif sum(computer_cards) > 21:
        print("Your opponent went over 21! YOU WIN!")
    elif sum(user_cards) > sum(computer_cards):
        print("You WIN!")
    elif sum(user_cards) < sum(computer_cards):
        print("You LOSE!")

print(logo)
print("Let's play Blackjack!") 
deal_cards()
print(f"The Computer's first card is: [{computer_cards[0]}]")

game_is_on = True
while game_is_on:
    choice = input(f"Your cards are {user_cards}, the totWould you like another card? Type 'Y' for yes and 'N' for no: ")
    if choice == "Y":
        deal_new_card()
        print(f"Your new card is: {user_cards}, and the new total is [{sum(user_cards)}].")
        if sum(user_cards) > 21:
            print(f"Sorry! You went over 21! You're bust!")
            game_is_on = False
    else: 
        computer_plays()
        print(f"The Computer's cards are: {computer_cards} and the total is {sum(computer_cards)}.")
        compare_scores()
        game_is_on = False
    