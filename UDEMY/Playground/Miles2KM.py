#Create Screen
from tkinter import * 

FONT = ("Times New Roman", 18, "bold")

def calculate():
    miles = int(entry.get())
    km = miles * 1.6
    km_result_label.config(text=km)

screen = Tk()
screen.title("Miles to KM Converter")
screen.minsize(width=200, height=200, )
#screen.maxsize(width=400, height=400)

button = Button()
button.config(text="Calculate", font=FONT, command=calculate)
button.grid(row=3, column=1)

entry = Entry()
entry.focus()
entry.grid(row=1, column=1)
entry.get()

# Create labels
equal_to_label = Label()
equal_to_label.config(text="is equal to: ", font=FONT)
equal_to_label.grid(row=2, column=0)

km_conversion = Label()
km_conversion.config(text="Km", font=FONT)
km_conversion.grid(row=2, column=2)

miles_label = Label()
miles_label.config(text="Miles", font=FONT)
miles_label.grid(row=1, column=2)

km_result_label = Label()
km_result_label.config(text="0", font=FONT)
km_result_label.grid(row=2, column=1)

screen.mainloop()