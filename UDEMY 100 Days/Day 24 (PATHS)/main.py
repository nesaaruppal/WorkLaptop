# Opening and printing a file
# Using the File Path seems to work better than just the text name. 

file = open("UDEMY\Day24.py\my_file.txt")
contents = file.read()
print(contents)
file.close()

# USING WITH "WITH" AND "AS"
# Don't have to close the file each time.

    #with open("UDEMY\Day24.py\my_file.txt") as file:
    #    contents = file.read()
    #    print(contents)
    

# WRITING INTO A TEXT FILE. 
# Must change the mode (defaults to read-only)
# If we want to change it then we change the mode.
# "w" = 'Write' and will OVERWRITE your text file.
# "a" = 'Append' will ADD to the file 

    #with open("UDEMY\Day24.py\my_file.txt", mode="a") as file:
    #    file.write("\nThis is me adding new text using mode=a.")


# CREATE NEW TEXT FILE
# If Python can't find the text file, it will create one for you if the mode is set to "w" (WRITE)

    #with open("new_file.txt", mode="w") as #file:
    #    file.write("This is a new file.\nWith #new text added by 'Open' and 'Write'.")



