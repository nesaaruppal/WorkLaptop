import random


class Knight:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} attacked for {damage} damage!")
        self.health -= damage
        return self.health

    def heal(self):
        heal_amount = random.randint(1, 10)
        print(f"{self.name} healed for {heal_amount} HP!")
        self.health += heal_amount
        return self.health

    def pick_action(self):
        options = ["attack", "heal"]
        action = random.choice(options)
        return action


knight1 = Knight("Knight 1", 100)
knight2 = Knight("Knight 2", 100)

game_running = True
while game_running:

    print(f"{knight1.name}: {knight1.health} HP")
    print(f"{knight2.name}: {knight2.health} HP")

    action = knight1.pick_action()
    if action == "attack":
        damage = knight1.attack()
        if damage <= 0:
            game_running = False

    elif action == "heal":
        heal_amount = knight1.heal()
        if heal_amount >= knight1.health:
            game_running = False

    print()
