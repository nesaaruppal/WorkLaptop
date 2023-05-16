################### Scope ####################

# GLOBAL SCOPE
enemies = 1

# LOCAL SCOPE


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
# inside = 2
# outside = 1
