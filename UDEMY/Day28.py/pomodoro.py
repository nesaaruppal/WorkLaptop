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

#"01:35"
#300
#245/60 = 4 minutes
#245 % 60 = (remainder)


def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    
    if REPS % 8 == 0:
        countdown(long_break)
    elif REPS % 2 == 0:
        countdown(short_break)
    elif REPS % 2 != 0:
        countdown(short_break)
    else:
        countdown(work_sec)
    
    #IF 1/3/5/7 repetition:
    # countdown(work_sec)
    #IF 2/4/6 repetition
    # countdown(short_break)
    #IF 8 repetition:
    # countdown(long_break)
    
    #if REPS == 1:
    #    countdown(work_sec)
    #    REPS += 1
    #elif REPS == 2:
    #    countdown(short_break)
    #    REPS += 1
    #elif REPS == 3:
    #    countdown(work_sec)
    #    REPS += 1
    #elif REPS == 4:
    #    countdown(short_break)
    #    REPS += 1
    #elif REPS == 5:
    #    countdown(work_sec)
    #elif REPS == 6:
    #    countdown(short_break)
    #elif REPS == 7:
    #    countdown(work_sec)
    #elif REPS % 8 == 0:
    #    countdown(long_break)    
    
        
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
        window.after(1000, countdown, count-1)
    

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)


canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day28.py\tomato.png")
canvas.create_image(150, 175, image=tomato_img)
timer_text = canvas.create_text(150, 175, text="00:00", font=("Times New Roman", 28, "bold"), fill="white")
canvas.grid(row=2, column=2)


label_timer = Label(text="TIMER", font=("Times New Roman", 24, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(row=1, column=2)
label_check = Label(text="✅", bg= YELLOW, fg=GREEN, highlightthickness=0)
label_check.grid(row=4, column=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=1)


reset_button = Button(text="Reset")
reset_button.grid(row=3, column=3)





window.mainloop()
