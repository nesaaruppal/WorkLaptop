# ERRORS

# FileNotFound - File does not exist
    #with open("a_file") as file:
        #file.read()
        
#KeyError - No key found 
    #a_dict = {"key":"value"}
    #value = a_dict["different_key"]    

#IndexError - Wrong index
    #fruit_list = ["Apple", "Orange", "Pear"]
    #fruit = fruit_list[3]
    
#TypeError - Wrong Data Types being combined
    #text = "abc"
    #print(text + 5)

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human's are not taller than metres!")

bmi = weight / height ** 2
print(bmi)
