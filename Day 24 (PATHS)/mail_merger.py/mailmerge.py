PLACEHOLDER = "[name]"


with open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day24.py\mail_merger.py\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)
    
with open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day24.py\mail_merger.py\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(rf"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day24.py\mail_merger.py\Output\ReadyToSend\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
        
