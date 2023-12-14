import os
import random

from art import logo

os.system('cls')


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and returns the score of these cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compares your score to the computer's score"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You LOSE! The opponent has Blackjack!"
    elif user_score == 0:
        return "You WIN! You got Blackjack!"
    elif computer_score > 21:
        return "The opponent went over 21! You WIN!"
    elif user_score > 21:
        return "You went over 21! You LOSE!"
    elif user_score > computer_score:
        return "YOU WIN!"
    else:
        return "You LOSE!"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # For User
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(
            f"Your cards: {user_cards} and your current score is: {user_score}")
        print(f"The computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card or 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # For computer
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(
        f"Your final hand is {user_cards} and your final score was: {user_score}!")
    print(
        f"The computer's final hand was {computer_cards} and the final score was: {computer_score}!")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()
