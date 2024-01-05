import random

print(" ______________________________ ")
print("|                              |")
print("|      Planets Top Trumps      |")
print("|______________________________|")
print("")

planets = [
    ["Mercury", 4600000, 2439.7, 88, 0],
    ["Venus", 1082000, 1210.2, 224.7, 0],
    ["Earth", 149600000, 12742, 365.26, 1],
    ["Mars", 22790000, 6792, 687, 2],
    ["Jupiter", 778400000, 142984, 4332, 69],
    ["Saturn", 143360000, 120536, 10759, 82],
    ["Uranus", 287100000, 51118, 30685, 27],
    ["Neptune", 45030000, 49528, 16460, 14],
    ["Pluto", 5906000, 2370, 905, 0],
]


def display_planet(planet):
    name, distance, size, orbital_period, moons = planet
    print(f"Name: {name}")
    print(f"Distance from the Sun: {distance} million km")
    print(f"Size: {size} km")
    print(f"Orbital Period: {orbital_period} days")
    print(f"Number of Moons: {moons}")


def compare_planets(planet1, planet2, criteria):
    name1, distance1, size1, orbital_period1, moons1 = planet1
    name2, distance2, size2, orbital_period2, moons2 = planet2

    if criteria == 1:
        if distance1 > distance2:
            return True
        elif distance1 == distance2:
            return False
        else:
            return False
    elif criteria == 2:
        if size1 > size2:
            return True
        elif size1 == size2:
            return False
        else:
            return False
    elif criteria == 3:
        if orbital_period1 > orbital_period2:
            return True
        elif orbital_period1 == orbital_period2:
            return False
        else:
            return False
    elif criteria == 4:
        if moons1 > moons2:
            return True
        elif moons1 == moons2:
            return False
        else:
            return False


def play_game():
    points = {"player": 0, "computer": 0}
    criteria = random.randint(1, 4)

    planet1 = random.choice(planets)
    planet2 = random.choice(planets)
    display_planet(planet1)
    display_planet(planet2)

    while points["player"] < 12 and points["computer"] < 12:
        winner = compare_planets(planet1, planet2, criteria)
        if winner:
            points["player"] += 3
            print(f"You win! Your score is {points['player']}.")
        else:
            points["computer"] += 1
            print(f"Computer wins! Computer's score is {points['computer']}.")

        if points["player"] == 12:
            print("You win!")
            break
        elif points["computer"] == 12:
            print("Computer wins!")
            break

        planet1 = random.choice(planets)
        planet2 = random.choice(planets)
        display_planet(planet1)
        display_planet(planet2)

    print(f"Player score: {points['player']}")
    print(f"Computer score: {points['computer']}")


play_game()
