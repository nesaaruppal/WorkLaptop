from tkinter import *
import math
import turtle

timer = None
BACKGROUND_COLOR = "#B1DDC6"
GREEN = "#9bdeac"   

def flip_card():
    window.update()
    back_card_img = PhotoImage(file=r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day31 (FLash Card App)\images\card_back.png")
    back_label = Label(image=back_card_img, bg=BACKGROUND_COLOR)
    back_label.grid(row=0, rowspan=3, column=0, columnspan=5)

    english_text = Label(text="English", font=("Cascadia Code", 20, "italic"), bg=GREEN)
    english_text.grid(row=0, column=2)
    french_word = Label(text="'Demande'", font=("Cascadia Code", 28, "bold"), bg=GREEN)
    french_word.grid(row=1, column=2)
   
def start_countdown():
    global timer
    timer = window.after(3000, flip_card())

window = Tk()
window.title("FLASH CARDS!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=500, height=500)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card_img = PhotoImage(file=r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day31 (FLash Card App)\images\card_front.png")
front_card_label = Label(image=front_card_img, bg=BACKGROUND_COLOR)
front_card_label.grid(row=0, rowspan=3, column=0, columnspan=5)

french_text = Label(text="French", font=("Cascadia Code", 20, "italic"), bg="white")
french_text.grid(row=0, column=2)
french_word = Label(text="'Request'", font=("Cascadia Code", 28, "bold"), bg="white")
french_word.grid(row=1, column=2)



#Buttons
start_button = Button(text="Start Button", font=("Times New Roman", 14, "bold"), highlightthickness=0, bg="Green", command=start_countdown)
start_button.grid(column=2, row=5)

incorrect_img = PhotoImage(file=r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day31 (FLash Card App)\images\wrong.png") 
incorrect_button = Button(image=incorrect_img, highlightthickness=0, height=50, width=50, bg=BACKGROUND_COLOR)
incorrect_button.grid(column=1, row=5)

correct_img = PhotoImage(file=r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day31 (FLash Card App)\images\right.png")
correct_button = Button(image=correct_img, highlightthickness=0, height=50, width=50, bg=BACKGROUND_COLOR)
correct_button.grid(column=3, row=5)




    



window.mainloop()