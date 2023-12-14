from art import logo
import os

print(logo)
print("Welcome to the Secret Auction!")

bidders = {}

def highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} who paid £{highest_bid}!")


should_continue = True
while should_continue:
    name = input("What is your name?: ")
    price = int(input("What is your bid? £"))
    bidders[name] = price
    go_again = input("Would you like to go again? Type 'Y' for yes and 'N' for no: ").upper()
    if go_again == "Y":
        os.system('cls')
    else:
        print(logo)
        highest_bid(bidders)
        should_continue = False
    




