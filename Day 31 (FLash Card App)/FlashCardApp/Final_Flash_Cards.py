from tkinter import * 
import csv
import pandas
import random
import time
import turtle

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv(r"UDEMY\Day31 (FLash Card App)\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"UDEMY\Day31 (FLash Card App)\data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


current_card = {}

def next_card():
    global current_card, flip_timer 
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)
    

def flip_card():   
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    
def is_known():
    """Removes known words from the dictionary list"""
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()
    
    

window = Tk()
window.title("FLASH CARDS")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="UDEMY\Day31 (FLash Card App)\images\card_front.png")
card_back_img = PhotoImage(file="UDEMY\Day31 (FLash Card App)\images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 68,"bold"))
canvas.grid(row=0, column=0, columnspan=3)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)



unknown_img = PhotoImage(file="UDEMY\Day31 (FLash Card App)\images\wrong.png")
unknown_button = Button(image=unknown_img, command=next_card)
unknown_button.grid(row=1, column=0)

known_img = PhotoImage(file="UDEMY\Day31 (FLash Card App)\images\correct.png")
known_button = Button(image=known_img, command=is_known)
known_button.grid(row=1, column=2)

start_button = Button(text="Start Button")
start_button.grid(row=1, column=1)



next_card()












window.mainloop()