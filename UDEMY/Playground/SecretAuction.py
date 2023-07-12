from art import logo
import os

print(logo)

print("Welcome to the Secret Auction Program!")

bidders = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0 
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of £{highest_bid}")
    

auction_is_on = True
while auction_is_on:
    
    name = input("What is your name?: ")
    price = int(input("What is your bid?: £"))

    bidders[name] = price

    more_bids = input("Are there any other bidders? Type 'Y' for yes and 'N' for no: ")
    if more_bids == "Y":
        os.system('cls')
    if more_bids == "N":
        for bids in bidders:
            highest_bid = 0
            if price > highest_bid:
                highest_bid = price
                winning_bid = highest_bid
            print(winning_bid)
            
        
        
        
        
        
       #
       #for bid in bidders:
       #    high_bid = bidders[bid]
       #    if high_bid > bidders[bid]:
       #        highest_bid = high_bid
       #        


       #print(highest_bid)
    