import os
import time
import random

def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Addition')

    continue_calc = 'y'

    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 + num_2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))

        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans += num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def subtraction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')

    continue_calc = 'y'

    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 - num_2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))

        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans -= num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def multiplication():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Multiplication')

    continue_calc = 'y'

    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 * num_2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))

        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans *= num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Division')

    continue_calc = 'y'

    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    while num_2 == 0.0:
        print('Please enter a second number > 0')
        num_2 = float(input('Enter another number: '))

    ans = num_1 / num_2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))

        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        while num == 0.0:
            print('Please enter a number > 0')
            num = float(input('Enter another number: '))
        ans /= num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def calculator():
    quit = False
    while not quit:
        results = []
        print('Calculator in Python!')
        print('Enter \'a\' for addition')
        print('Enter \'s\' for subtraction')
        print('Enter \'m\' for multiplication')
        print('Enter \'d\' for division')
        print('Enter \'q\' to quit')

        choice = input('Selection: ')

        if choice == 'q':
            quit = True
            continue

        if choice == 'a':
            results = addition()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        elif choice == 's':
            results = subtraction()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        elif choice == 'm':
            results = multiplication()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        elif choice == 'd':
            results = division()
            print('Ans = ', results[0], ' total inputs: ', results[1])
        else:
            print('Sorry, invalid character')

def get_user_input():
    user_input = input("Enter countries, one at a time, separated by commas: ")
    return user_input.split(",")

def compare_inputs(user_input, largest_countries):
    correct = True
    score = 0
    lives = 3
    start_time = time.time()
    while lives > 0 and correct and (time.time() - start_time) < 60:
        for country in user_input:
            if country in largest_countries:
                largest_countries.remove(country)
                score += 1
                break
        else:
            correct = False
            lives -= 1
        if not correct:
            print(f"You got {score} out of {len(user_input)} correct. You have {lives} lives left.")
    if correct:
        print(f"You got {score} out of {len(user_input)} correct!")

largest_countries = [
    "Russia",
    "Canada",
    "USA",
    "China",
    "Brazil",
    "Australia",
    "India",
    "Argentina",
    "Kazakhstan",
    "Algeria",
]

random.shuffle(largest_countries)

while True:
    user_input = get_user_input()
    compare_inputs(user_input, largest_countries)