#WRITE 
# json.dump()

#READ
# json.load()

#UPDATE
# json.update()

from tkinter import * 
from tkinter import messagebox
import json
from random import choice, randint, shuffle


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please make sure you fill in all fields!")
        
        # 1. Reading the existing data
        # 2. Updating it with new data 
        # 3. Saving the updated data   
        
        # json.dump(new_data, data_file, indent=4)   
    else:               
        try:
            with open (r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\data.json", "r") as data_file: 
                #Read old data 
                data = json.load(data_file)
        except FileNotFoundError:
            with open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old with new data
            data.update(new_data)
         
            
            with open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\data.json", "w") as data_file:
                #Saving the updated data
                json.dump(data, data_file, indent=4)
                
                website_entry.delete(0, END)
                password_entry.delete(0, END)  
                
                
def random_password():
    """Shorter way of creating a random password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',   'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',  'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  
    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]
    
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    
    password = "".join(password_list)
    
    password_entry.insert(0, password)

def find_password():
    website = website_entry.get()
    try:
        with open (r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error!", message="No Data File Found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error!", message=f"No details for {website} saved!")
            
            

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
paddlock_img = PhotoImage(file=r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day29 (Password Manager)\logo.png")
canvas.create_image(100, 100, image=paddlock_img)
canvas.grid(row=0, column=1)

#LABELS
web_label = Label(text="Website:")
web_label.grid(row=1, column=0, sticky=W)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky=W)

password_label = Label(text="Password:", )
password_label.grid(row=3, column=0, sticky=W)


#ENTERED TEXT
website_entry = Entry(width=35, bg=GREEN)
website_entry.grid(row=1, column=1, sticky=W)
website_entry.focus()

email_entry = Entry(width=35, bg=GREEN)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
email_entry.insert(0, "nesaar97@gmail.com")

password_entry = Entry(width=21, bg=GREEN)
password_entry.grid(row=3, column=1, sticky=W)

#BUTTONS 
gen_pw = Button(text="Generate Password", command=random_password)
gen_pw.grid(row=3, column=2, sticky=W)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(row=4, column=0, columnspan=3)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()