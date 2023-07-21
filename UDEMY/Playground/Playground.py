from tkinter import *
from playground_art import apple

BACKGROUND = "#FFE0BD"
FORGROUND = "#90B5C1"
FONT = ("Cascadia Code", 14)


window = Tk()
window.title("Guess the Fruit!")
window.config(width=500, height=500, padx=50, pady=50, bg=BACKGROUND)

canvas = Canvas(width=400, height=250, highlightthickness=1, bg=BACKGROUND)
apple_img = PhotoImage("apple.png")
canvas.create_image(200, 200, image=apple_img)
canvas.place(x=100, y=100)





#Label
title_label = Label(text="What Fruit is This?", font=FONT, fg="#CA4B9B", bg="#DCBF5E", highlightcolor="black", highlightbackground="black", highlightthickness=5)
title_label.config(width=20, height=1)
title_label.place(x=100, y=5)

# BUTTONS
known_img = PhotoImage(file="UDEMY\Day31 (FLash Card App)\images\correct.png")
known_button = Button(image=known_img)
known_button.config(width=50, height=50)
known_button.place(x=0, y=320)

unknown_img = PhotoImage(file="UDEMY\Day31 (FLash Card App)\images\wrong.png")
unknown_button = Button(image=unknown_img)
unknown_button.config(width=50, height=50)
unknown_button.place(x=345, y=320)

start_button = Button(text="START BUTTON", font=("Cascadia Code", 14, "bold"))
start_button.config(width=15, height=1)
start_button.place(x=115, y=320)

window.mainloop()