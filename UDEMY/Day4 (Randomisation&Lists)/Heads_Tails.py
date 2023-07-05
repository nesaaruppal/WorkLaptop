import random
print("Welcome to heads or tails!")

coin_toss = random.randint(0, 1)
if coin_toss == 0:
    print("HEADS!")
else:
    print("TAILS!")
