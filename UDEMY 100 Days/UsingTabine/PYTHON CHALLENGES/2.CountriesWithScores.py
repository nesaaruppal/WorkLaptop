import random

"AFRICAN COUNTRIES"

african_countries = [
    "Algeria",
    "Angola",
    "Benin",
    "Botswana",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Cameroon",
    "Central African Republic",
    "Chad",
    "Comoros",
    "Ivory Coast",
    "Djibouti",
    "Democratic Republic of the Congo",
    "Egypt",
    "Equatorial Guinea",
    "Eritrea",
    "Eswatini",
    "Ethiopia",
    "Gabon",
    "Gambia",
    "Ghana",
    "Guinea",
    "Guinea-Bissau",
    "Kenya",
    "Lesotho",
    "Liberia",
    "Libya",
    "Madagascar",
    "Malawi",
    "Mali",
    "Mauritania",
    "Mauritius",
    "Morocco",
    "Mozambique",
    "Namibia",
    "Niger",
    "Nigeria",
    "Republic of the Congo",
    "Rwanda",
    "Sao Tome & Principe",
    "Senegal",
    "Seychelles",
    "Sierra Leone",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Sudan",
    "Tanzania",
    "Togo",
    "Tunisia",
    "Uganda",
    "Zambia",
    "Zimbabwe",
].lower()


def play_game():
    lives = 3
    score = 0
    remaining_countries = african_countries.copy()
    while lives > 0 and remaining_countries:
        guess = input("Guess an African country: ")
        if guess in remaining_countries:
            score += 1
            remaining_countries.remove(guess)
            print("Correct! The country is located in Africa.")
        else:
            lives -= 1
            print(
                f"Sorry, {guess} is not a valid country. You have {lives} lives remaining.")
    if lives > 0:
        print(
            f"You found all {len(african_countries)} countries! Your score is {score}.")
    else:
        print(
            f"You lost. The correct answers were {african_countries}. Your score was {score}.")


play_game()
