print("PRIME NUMBERS!")

number = int(input("Which number would you like to check?\n"))

def check(number):
    is_prime = True
    for _ in range(2, number):
        if number % _ == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number!")
    else:
        print("It is not a prime number!")

check(number)