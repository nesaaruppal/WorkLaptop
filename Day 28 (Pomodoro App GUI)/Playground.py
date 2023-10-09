PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20       
REPS = 0 

def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    
    #IF 1/3/5/7 rep:


def add_reps(): 
    global REPS
    REPS += 1
    
reps = add_reps()
print(reps)