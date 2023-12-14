PLACEHOLDER = "[name]"

with open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day24.py\mail_merger.py\Input\Names\invited_names.txt") as names:
    invited_names = names.readlines()
    print(invited_names)
    
with open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day24.py\mail_merger.py\Input\Letters\starting_letter.txt") as starting_letter:
    new_letter = starting_letter.read()
    print(new_letter)