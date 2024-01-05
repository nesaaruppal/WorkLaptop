import random


def get_user_input():
    user_input = input("Enter countries, one at a time, separated by commas: ")
    return user_input.split(",")


def compare_inputs(user_input, largest_countries):
    correct = True
    score = 0
    lives = 3
    while lives > 0 and correct:
        for country in user_input:
            if country in largest_countries:
                largest_countries.remove(country)
                score += 1
                break
        else:
            correct = False
            lives -= 1
        if not correct:
            print(
                f"You got {score} out of {len(user_input)} correct. You have {lives} lives left.")
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

while True:
    print("Guess the largest countries in the world:\n")
    user_input = get_user_input()
    compare_inputs(user_input, largest_countries)
