# Create a new list from a previous list

# FOR LOOP
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
    #add_1 = n+1
    #new_list.append(add_1)

#LIST COMPREHENSION   
#   new_list = [new_item for item in list]
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Nesaar"
letters_list = [letter for letter in name]
print(letters_list)


doubled_numbers = [number*2 for number in range(1, 5)]
print(doubled_numbers)