from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20       
REPS = 0 
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="TIMER", font=("Times New Roman", 24, "bold"), fg=GREEN, bg=YELLOW)
    label_check.config(text="")
    global REPS
    REPS = 0 

def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    
    if REPS % 8 == 0:
        countdown(long_break)
        label_timer.config(text="Break", font=("Times New Roman", 28, "bold"), fg=RED)
    elif REPS % 2 == 0:
        countdown(short_break)
        label_timer.config(text="Break", font=("Times New Roman", 28, "bold"), fg=PINK)
    else:
        countdown(work_sec)
        label_timer.config(text="Work", font=("Times New Roman", 28, "bold"), fg=GREEN)


def countdown(count):
    count_min = math.floor(count/60)
    count_sec = (count % 60)
    #DYNAMIC TYPING
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min == 0:
        count_min = "00"
        
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # We want to cancel the following
        # So we give it a name
        global timer
        timer = window.after(1000, countdown, count-1)   
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✅"
        label_check.config(text=mark)
    

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)


canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day28 (Pomodoro App GUI)\Pomodoro App\tomato.png")
canvas.create_image(150, 175, image=tomato_img)
timer_text = canvas.create_text(150, 175, text="00:00", font=("Times New Roman", 28, "bold"), fill="white")
canvas.grid(row=2, column=2)


label_timer = Label(text="TIMER", font=("Times New Roman", 24, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(row=1, column=2)

label_check = Label(bg= YELLOW, fg=GREEN, highlightthickness=0)
label_check.grid(row=4, column=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=1)


reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=3)





window.mainloop()
