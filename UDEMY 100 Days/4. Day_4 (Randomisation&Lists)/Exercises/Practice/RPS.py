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


print("Welcome to the Rock, Paper, Scissors Game!")
user_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors: "))
computer_choice = random.randint(0, 2)

if user_choice == 0 and computer_choice == 0:
    print(rock)
    print("Computer Chose: ")
    print(rock)
    print("DRAW!")
elif user_choice == 0 and computer_choice == 1:
    print(rock)
    print("Computer Chose: ")
    print(paper)
    print("You Lose!")
elif user_choice == 0 and computer_choice == 2:
    print(rock)
    print("Computer Chose: ")
    print(scissors)
    print("You Win!")
elif user_choice == 1 and computer_choice == 0:
    print(paper)
    print("Computer Chose: ")
    print(rock)
    print("You Win!")
elif user_choice == 1 and computer_choice == 1:
    print(paper)
    print("Computer Chose: ")
    print(paper)
    print("DRAW!")
elif user_choice == 1 and computer_choice == 2:
    print(paper)
    print("Computer Chose: ")
    print(scissors)
    print("You Lose!")
elif user_choice == 2 and computer_choice == 0:
    print(scissors)
    print("Computer Chose: ")
    print(rock)
    print("You Lose!")   
elif user_choice == 2 and computer_choice == 1:
    print(scissors)
    print("Computer Chose: ")
    print(paper)
    print("You Win!")  
elif user_choice == 2 and computer_choice == 2:
    print(scissors)
    print("Computer Chose: ")
    print(scissors)
    print("DRAW!")
else:
    print("Please enter either 0, 1 or 2!")
    
