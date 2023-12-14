print("LIST COMPREHENSION!")

numbers = [1,2,3]

#new_list = [new_item for item in list]
    # list = numbers
    # item = anything (n)
    # new_item (n+1)
    
new_numbers = [n+1 for n in numbers]
print(new_numbers)

# List Comprehension with STRINGS
name = "Nesaar"
new_list = [letter for letter in name]
print(new_list)

# List comprehension with RANGE
range_list = [num * 2 for num in range(1,5)]
print(range_list)

# List comprehension with CONDITIONS
    # new_list = [new_item for item in list IF TEST]
names = ["Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [new_item for item in list if test]
short_names = [n for n in names if len(n) < 5]
print(short_names)

long_names = [n.upper() for n in names if len(n) > 5]

print(long_names)