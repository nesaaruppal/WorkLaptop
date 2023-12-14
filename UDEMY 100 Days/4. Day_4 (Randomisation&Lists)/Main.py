# RANDOMISATION
import random

import my_module

# randint(a, b) <- will return a random integer INCLUSIVE of a and b
random_integer = random.randint(100, 200)
print(random_integer)

# Import your own module
print(my_module.pi)

# Import a random floating number
# random.random() will return a floating point between 0 and 1.0 (does not include 1!)
random_float = random.random()
print(random_float)

# You can multiply the random float by a number so that your random float is higher than 1
larger_float = random.random() * 10
print(larger_float)

# LIST
# Type of Data Structure
fruits = ["oranges", "apples"]
# Can store all types of data <- strings, booleans, integers


# import random

# import my_module
 
# random_integer = random.randint(100, 200)
# pi = my_module.pi
# random_float = random.random()

# print(random_integer)
# print(pi)
# print(random_float)
