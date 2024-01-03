# TRY:
    # Something that might cause an exception 

# EXCEPT:
    # Do this if there WAS an exception 

# ELSE:
    # Do this if there were NO exceptions

# FINALLY:
    # Do this NO MATTER WHAT HAPPENS 
    
        ##### E.G. #####
    # File not found 
# try:
#     file = open("a_file.txt")
# except:
#     print("There was an error!")
    
    
    
    
try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["aysdufeaufgkaytsajfeyfadtjewarrydwafjwytetar"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something interesting ...")
except KeyError as error_message:
    print(f"That key {error_message} does not exist!")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was successfully closed!")   