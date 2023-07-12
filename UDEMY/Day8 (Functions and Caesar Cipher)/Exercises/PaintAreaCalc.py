import math
print("Welcome to the Paint Area Calculator!")

test_height = int(input("Height of wall: "))
test_width = int(input("Width of wall: "))
coverage = 5


def paint_calc(height, width, coverage):
    number_of_cans = ((height * width) / coverage)
    total_num_cans = math.ceil(number_of_cans)
    print(f"You'll need {total_num_cans} cans of paint.")
    
paint_calc(height=test_height, width=test_width, coverage=5)