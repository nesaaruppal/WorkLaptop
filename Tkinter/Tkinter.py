from tkinter import * 
import random

colours = ["red", "blue", "green", "purple", "pink", "yellow"]

def change_colour():
    BACKGROUND_COLOUR = random.choice(colours)
    canvas = Canvas(width=450, height=300, bg=BACKGROUND_COLOUR)
    canvas.place(x=0, y=50)


TITLE_FONT = ("Cascadia Code", 18, "bold")

window = Tk()
window.config(width=500, height=500, padx=25, pady=25)
window.title("Tkinter Page!")

#Labels
title_label = Label()
title_label.config(text="Practicing With TK!", font=TITLE_FONT)
title_label.place(x=0, y=0)

canvas = Canvas(width=450, height=300)
canvas.place(x=0, y=50)


#buttons 
button = Button(command=change_colour)
button.config(text="Change to a random colour!")
button.place(x=0, y=400)


window.mainloop()