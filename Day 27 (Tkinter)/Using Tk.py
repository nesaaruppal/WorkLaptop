import tkinter

window = tkinter.Tk()
window.title("First GUI Program!")
window.minsize(width=700, height=500)

#LABEL
my_label = tkinter.Label(text="I am a label!", font=("Times New Roman", 40, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.pack()

#BUTTON
#Create an "Event Listener" function:
def button_clicked():
    new_label = input.get()
    print("I got clicked")
    my_label.config(text=new_label)

button = tkinter.Button(text="Click me!", command=button_clicked)
button.pack()

#ENTRY 
input = tkinter.Entry(width=50)
input.pack()
#Returns input as a string


window.mainloop()

#window =
#window.mainloop() --> Listens and keeps on screen
#minsize(w, h)
#get
#command = "name_of_function"