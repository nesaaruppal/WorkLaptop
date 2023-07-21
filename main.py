import turtle 
import pandas

#def get_click_coor(x, y):
#    print(x, y)

screen = turtle.Screen()
screen.title("U.S. States Game!")
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.tolist()

#turtle.onscreenclick(get_click_coor)
#turtle.mainloop()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)

screen.exitonclick()