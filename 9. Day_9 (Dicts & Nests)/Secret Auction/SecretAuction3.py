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
    print(f"The winner was {winner} with a bid of £{highest_bid}!")
                




auction_on = True
while auction_on:
    name = input("What is your name?: ")
    price = int(input("How much are you bidding? £"))
    bidders[name] = price
    should_continue = input("Would someone else like to bid? Type 'Y' for yes   and type 'N' for no: ")
    if should_continue == "Y":
        os.system('cls')
    else:
        print(logo)
        highest_bid(bidders)
        auction_on = False
        should_continue = False
        

