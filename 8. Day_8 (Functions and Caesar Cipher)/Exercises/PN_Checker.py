print("Welcome to the Prime Number checker!")

number = int(input("Enter the number you would like to check: "))

def is_prime(number):
    is_prime = True
    for x in range(2, number):
        if number % x == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number!")
    else:
        print(f"{number} is not a prime number!")


        
is_prime(number)