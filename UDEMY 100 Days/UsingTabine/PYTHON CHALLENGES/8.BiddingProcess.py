from datetime import datetime
import re


class Auction:
    def __init__(self):
        self.start_time = datetime.now()
        self.current_bid = 0

    def accept_bid(self):
        current_time = datetime.now()
        time_elapsed = current_time - self.start_time
        print(f"Time elapsed: {time_elapsed}")

        bid = input("Enter your bid: ")
        if re.match(r"^\d+(\.\d+)?$", bid):
            bid_value = float(bid)
            if bid_value > self.current_bid:
                self.current_bid = bid_value
                print(f"New high bid: ${bid_value:.2f}")
            else:
                print("Your bid is too low.")
        else:
            print("Invalid bid. Please enter a number.")


while playing_game == True:
    auction = Auction()
    auction.accept_bid()
