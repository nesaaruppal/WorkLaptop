print("Squaring Numbers with List Comprehension!")

numbers = [1, 1, 2, 3, 5, 8, 13, 21,34, 55]

new_list = [number*number for number in numbers]
print(new_list)