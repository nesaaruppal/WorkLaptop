import random

# Define the characters
knight1 = "Knight 1"
knight2 = "Knight 2"

# Define the health of the characters
knight1_health = 100
knight2_health = 100

# Define the attack power of the characters
knight1_attack = 5
knight2_attack = 7

# Define the game loop
game_running = True
while game_running:

    # Display the health of the characters
    print(f"{knight1}: {knight1_health} HP")
    print(f"{knight2}: {knight2_health} HP")

    # Prompt the user to choose an option
    print("Choose an option:")
    print("1. Attack")
    print("2. Heal")
    print("3. Exit")
    option = input()

    # Check if the user wants to exit the game
    if option == "3":
        game_running = False
        print("Game over!")

    # Check if the user wants to attack
    elif option == "1":
        # Choose a random character to attack
        if random.randint(1, 2) == 1:
            attacker = knight1
            defender = knight2
        else:
            attacker = knight2
            defender = knight1

        # Calculate the damage done by the attacker
        damage = random.randint(1, 50)

        # Display the attack
        print(f"{attacker} attacked {defender} for {damage} damage!")

        # Reduce the health of the defender
        defender_health = defender = - damage

        # Check if the defender is dead
        if defender_health <= 0:
            print(f"{defender} died!")
            if attacker == knight1:
                knight2_health = knight2 = + 10
            else:
                knight1_health = knight1 = + 10

    # Check if the user wants to heal
    elif option == "2":
        # Choose a random character to heal
        if random.randint(1, 2) == 1:
            healer = knight1
            target = knight2
        else:
            healer = knight2
            target = knight1

        # Calculate the amount of health to heal
        heal_amount = random.randint(1, 10)

        # Display the heal
        print(f"{healer} healed {target} for {heal_amount} HP!")

        # Heal the target
        target_health = target_health + heal_amount
