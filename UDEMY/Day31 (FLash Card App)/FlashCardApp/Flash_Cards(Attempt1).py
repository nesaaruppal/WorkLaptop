from tkinter import *
import turtle

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FLASH CARDS!")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=1000, height=500, bg=BACKGROUND_COLOR)

#Label Flash Cards
front_card_img = PhotoImage(file=r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day31 (FLash Card App)\images\card_front.png")
front_label = Label(image=front_card_img, bg=BACKGROUND_COLOR)
front_label.grid(row=0, column=1)

back_card_img = PhotoImage(file=r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day31 (FLash Card App)\images\card_back.png")
back_label = Label(image=back_card_img, bg=BACKGROUND_COLOR)
back_label.grid(row=0, column=0)



#Buttons
correct_img = PhotoImage(file=r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day31 (FLash Card App)\images\right.png")
correct_button = Button(image=correct_img, highlightthickness=0, height=50, width=50, bg=BACKGROUND_COLOR)
correct_button.grid(row=1, column=2, sticky=E)

incorrect_img = PhotoImage(file=r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day31 (FLash Card App)\images\wrong.png") 
incorrect_button = Button(image=incorrect_img, highlightthickness=0, height=50, width=50, bg=BACKGROUND_COLOR)
incorrect_button.grid(row=1, column=0, sticky=W)


    



window.mainloop()


# SLOW way to use CSV
# def next_card():
    # french_word = random.choice(french_words)
    # print(french_word)
# 
# with open (r"UDEMY\Day31 (FLash Card App)\data\french_words.csv") as french_words:
    # df = pandas.read_csv(french_words)
   #print(df)
    # french_words = df["French"]
    # french_word = random.choice(french_words)
    # print(french_word)