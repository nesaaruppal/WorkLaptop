import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day25.py\US_Game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day25.py\US_Game\50_states.csv")

def mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(mouse_click_coor)

all_states = data.state.to_list()

guessed_states = [] 

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"You've guessed {len(guessed_states)}/50:", 
    prompt="What's another state?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_Learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #GET THE ROW FOR THE STATE 
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
            


            
            


            
        
        
    










#addshape
#turtle.mainloop()