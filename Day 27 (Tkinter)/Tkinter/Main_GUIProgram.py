import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(500, 300)

# LABEL
my_label = tkinter.Label(text="I am a label", font=("Times New Roman", 28, "bold"))
my_label.pack(side="top")

#Changing Properties
my_label["text"] = "New Text"
my_label.config(text="More Text")

# BUTTON
def button_clicked():
    new_text = input.get()
    #my_label.config(text="I got clicked!")
    my_label.config(text=new_text)
    

my_button = tkinter.Button(text="Button1", command=button_clicked)
my_button.pack(side="right")


# ENTRY
input = tkinter.Entry(width=30)
input.pack()
entered_text = input.get()



#minsize()
#pack()










window.mainloop()