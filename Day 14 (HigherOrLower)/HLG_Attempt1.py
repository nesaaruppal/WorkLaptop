# Display art
from art import logo, vs
import random
from game_data import data

def format_account_A(data):
    random_account = random.choice(data)
    name = random_account["name"]
    followers = random_account["follower_count"]
    description = random_account["description"]
    country = random_account["country"]
    print(f"Compare A: {name}, a {description}, from {country}.")
    
def format_account_B(data):
    random_account = random.choice(data)
    name = random_account["name"]
    followers = random_account["follower_count"]
    description = random_account["description"]
    country = random_account["country"]
    print(f"Against B: {name}, a {description}, from {country}.")

print(logo)

format_account_A(data)

print(vs)

format_account_B(data)

# Generate a random account from the game data 
            #random_account = random.choice(data)
            #print(random_account)


# Format the account data into a printable form
#def format_account(random_account):
#    name = random_account["name"]
#    description = random_account["description"]
#    country = random_account["country"]
#    print(f"Compare A: {name}, a {description}, from {country}.")
    
    
    
# Ask the user for a guess
#guess = input("Who has more followers: A or B?: ")
#if guess == "A":
#    if format_account_A
#
# Check if user is correct

#


















