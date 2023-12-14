from tkinter import *

def button_clicked():
    label.config(text="Hello World!") 

window = Tk()
window.title("GUI PROGRAM")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10)

label = Label(text="New UI!", font=("Ariel", 28, "bold"))
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

button = Button(text="Click here!")
button.grid(row=1, column=1)

new_button = Button(text="NEW BUTTON")
new_button.grid(row=0, column=2)


input = Entry()
input.grid(row=2, column=3)


window.mainloop()


#pack()
#place()
#grid()
#padx()
#pady()