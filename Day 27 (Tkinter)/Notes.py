#KEYWORD ARGUMENTS
#def my_function(a=1, b=2, c=3):
    #Do this with 'a'
    #Then this with 'b'
    #Finally do this with 'c'


#UNLIMITED POSITIONAL ARGUMENTS
def add(*args):
    for n in args:
        print(n)

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum 

#Creates a tuple
number = add(7,8,9,12,18,19)
print(number)


#MANY KEYWORD ARGUMENTS
def calculate(n, **kwargs):
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]  
    print(n)
    
calculate(2, add=3, multiply=5)

#Need to fill in every **Kwarg
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

#"GET" allows for the function to be called but you don't have to have every keyword filled in.
my_car = Car(make="GTR")
print(my_car.make)
print(my_car.model) #Returns "None"