print("LIST COMP - Filtering Evens!")

list_of_strings = input().split(',')

new_list = [int(number) for number in list_of_strings]

result = [number for number in new_list if number % 2 == 0]

print(new_list)
print(result)