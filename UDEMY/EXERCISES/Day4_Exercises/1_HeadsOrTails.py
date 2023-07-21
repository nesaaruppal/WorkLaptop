import random
print("Let's play Heads or Tails!")

coin = random.randint(0, 1)

if coin == 0:
    print("HEADS!")
else:
    print("TAILS!")