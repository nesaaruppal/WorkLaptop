#def add(*args):
    #for n in args:
        #print(n)

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum 

number = add(7,8,9,12,18,19)
print(number)


def calculate(n, **kwargs):
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]  
    print(n)
    
calculate(2, add=3, multiply=5)



