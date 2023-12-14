import random

logo = """
   _  __           __             _____                 _             
  / |/ /_ ____ _  / /  ___ ____  / ___/_ _____ ___ ___ (_)__  ___ _   
 /    / // /  ' \/ _ \/ -_) __/ / (_ / // / -_|_-<(_-</ / _ \/ _ `/   
/_/|_/\_,_/_/_/_/_.__/\__/_/    \___/\_,_/\__/___/___/_/_//_/\_, /    
                                                            /___/     
"""

print(logo)
print("Let's play the Number Guessing Game!")


computer_number = random.randint(1, 100)

game_on = True
lives = 5

while game_on:
    guess = int(input("Guess a number:\n"))
    
    if guess == computer_number:
        print("CORRECT!")
        print(f"You guessed '{guess}'!")
        game_on = False
        
    if lives == 0:
        print("You ran out of lives!")
        print("You LOSE!")
        print(f"The number was: '{computer_number}'!")
        game_on = False

    if guess > computer_number:
        lives -= 1
        print("Your guess was too high!")
        print(f"You only have '{lives}' lives left!\n")
    elif guess < computer_number:
        lives -= 1
        print("Your guess was too low!")
        print(f"You only have '{lives}' lives left!\n")
        
        
        
        