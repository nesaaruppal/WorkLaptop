
file1 = open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day26.py\file1.txt")
contents1 = file1.readlines()

file2 = open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day26.py\file2.txt")
contents2 = file2.readlines()

result = [int(number) for number in contents1 if number in contents2]
print(result)

#READLINES()