from turtle import Turtle, Screen

tim = Turtle()
tim.shapesize(stretch_len=3, stretch_wid=3)
tim.shape("turtle")
tim.color("Green")


for _ in range(360):
    num_sides = 3
    set_heading = (360/num_sides)
    tim.forward(10)
    num_sides += 1
    
    
    
screen = Screen()
screen.screensize(canvheight=400, canvwidth=400)




screen = Screen()
screen.mainloop()
