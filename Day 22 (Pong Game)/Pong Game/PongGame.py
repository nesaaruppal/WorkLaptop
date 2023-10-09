from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.canvheight = 600
screen.canvwidth = 800
screen.bgcolor('Black')
screen.title('PONG')
screen.tracer(0)

r_paddle = Paddle((280, 0))
l_paddle = Paddle((-280, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detect collision with the wall
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()
        
    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 250 or ball.distance(l_paddle) < 50 and ball.xcor() < -250:
        ball.bounce_x() 
        
    #Detect R paddle misses
    if ball.xcor() > 320:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -320:
        ball.reset_position()
        scoreboard.r_point()
    
screen.exitonclick()