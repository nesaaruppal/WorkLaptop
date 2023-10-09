import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
print("Welcome to the Rock, Paper, Scissors game!")

player_selection = input(
    "Which would you like to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: ")

computer_selection = random.randint(1, 3)
if computer_selection == 1:
    print(rock)
elif computer_selection == 2:
    print(paper)
else:
    print(scissors)

if player_selection == computer_selection:
    print("DRAW!")
elif player_selection == 1 and computer_selection == 2:
    print(rock)
    print(computer_selection)
    print("The computer wins!")
elif player_selection == 1 and computer_selection == 3:
    print(rock)
    print(computer_selection)
    print("You win!")
elif player_selection == 2 and computer_selection == 1:
    print(paper)
    print(computer_selection)
    print("You win!")
elif player_selection == 2 and computer_selection == 3:
    print(paper)
    print(computer_selection)
    print("The computer wins!")
elif player_selection == 3 and computer_selection == 1:
    print(scissors)
    print(computer_selection)
    print("You win!")
elif player_selection == 3 and computer_selection == 2:
    print(scissors)
    print(computer_selection)
    print("The computer wins!")
