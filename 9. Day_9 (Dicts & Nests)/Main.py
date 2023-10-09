# EXAMPLE DICTIONARY
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

# Retrieve Values from a dictionary
print(programming_dictionary["Bug"])

# Adding new items to the dictionary 
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Loop through the dictionary
for key in programming_dictionary:
    #print(key)
    print(programming_dictionary[key])