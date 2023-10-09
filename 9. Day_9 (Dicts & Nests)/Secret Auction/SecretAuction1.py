from art import logo 
import os

print(logo)
print("Welcome to the Secret Auction Program!")

bidders = {}

def highest_bidders(bidding_record):
    highest_bid = 0 
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner was {winner} with a highest bid of £{highest_bid}.")

auction_on = True
while auction_on:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bidders[name] = price
    go_again = input("Would you like to place another bid? Type 'Y' for Yes and 'N' for no: ").upper()
    if go_again == "Y":
        os.system('cls')
    if go_again == "N":
        print(logo)
        highest_bidders(bidders)
        auction_on = False


