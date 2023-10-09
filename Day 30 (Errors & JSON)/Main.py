#TRY 
    # Might cause an exception
    
#EXCEPT
    # Code to execute if there WAS an exception
    
#ELSE
    # If there were no exceptions carry out the code
    
#FINALLY
    # Carry out the code no matter what happens

#RAISE
    # Raise your own exceptions
    
    
    
    
#FileNotFound
try:
    file = open("a_file.txt")
    #Because the file does not exist it will move to the dictonary
    #If the EXCEPT is specified then the TRY block will continue
    a_dictionary = {"Key": "Value"}
    print(a_dictionary["readyyyy"])
    
except FileNotFoundError:
    # Specify what you want to fix to allow the second part of the TRY block to work
    file = open("a_file.txt", "w")
    file.write("Writing more things!")

except KeyError as error_message:
    #Specify if you want error message shown
    print(f"That key {error_message} does not exist!")
    
else:
    # Will not happen unless the TRY and EXCEPT methods work
    contents = file.read()
    print(contents)
    
finally:
    #Code that runs no matter what
    #file.close()
    #print("File was closed!")
    raise KeyError("I made it up")
