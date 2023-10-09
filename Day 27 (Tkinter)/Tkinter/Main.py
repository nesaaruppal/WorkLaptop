from tkinter import *

def button_clicked():
    label.config(text="Hello World!") 

window = Tk()
window.title("GUI PROGRAM")
window.minsize(500, 500)

button = Button(text="Click here!")
button.pack()

label = Label(text="New UI!", font=("Ariel", 28, "bold"))
label.pack()


input = Entry()
input.pack()
text = input.get()



window.mainloop()