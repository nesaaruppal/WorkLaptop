"COUNTRIES OF AFRICA "

import random

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
]


def play_game():
    score = 0
    attempts = 6
    remaining_countries = african_countries.copy()
    while attempts > 0 and remaining_countries:
        guess = input("Guess an African country: ")
        if guess in remaining_countries:
            score += 1
            remaining_countries.remove(guess)
            print("Correct! The country is located in Africa.")
        else:
            attempts -= 1
            print(
                f"Sorry, {guess} is not a valid country. You have {attempts} attempts remaining.")
    print(f"Your score is {score} out of {len(african_countries)}.")


play_game()
