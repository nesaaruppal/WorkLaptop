from tkinter import *

def convert():
    miles = int(input.get())
    km = round(miles * 1.6)
    label_answer.config(text=km)
    

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=100, height=100)

input = Entry(width=20)
input.grid(row=3, column=2)
input.get()

label_answer = Label(text="0", font=("Times New Roman", 14, "bold"))
label_answer.grid(row=4, column=2)

label_miles = Label(text="miles", font=("Times New Roman", 14, "bold"))
label_miles.grid(row=3, column=3)

label_equal = Label(text="is equal to", font=("Times New Roman", 14, "bold"))
label_equal.grid(row=4, column=1)

label_km = Label(text="Km", font=("Times New Roman", 14, "bold"))
label_km.grid(row=4, column=3)

button = Button(text="Calculate", command=convert, font=("Times New Roman", 14, "bold"))
button.grid(row=5, column=2)



window.mainloop()