print("Fizz Buzz!")

for number in range(1, 100):
    if number % 5:
        if number % 3:
            print ("Fizz Buzz!")
    elif number % 5:
            print ("Fizz Buzz")
    elif number % 3:
        print("Buzz")
    else:
        print(number)
    
    
    
# divisible by 3 = fizz
#divisible by 5 = buzz 
#divisible by 3 and 5 = fizzbuzz