import random
import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
turtle.speed(0)

# Define the snake and food objects
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.setheading(90)
snake.speed(0)

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.hideturtle()

# Define the game logic
snake_segments = []
snake_length = 5
food_pos = []

def move_snake():
    if len(snake_segments) > snake_length:
        del snake_segments[0]
    snake_head = snake_segments[-1]
    snake_head.goto(snake_head.xcor(), snake_head.ycor())
    snake_segments.append(snake_head)

def create_food():
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    food_pos = [x, y]
    food.goto(x, y)

def check_eat():
    if snake_head.distance(food) < 20:
        food_pos = create_food()
        snake_length += 1

# Create game elements
for i in range(snake_length):
    x = snake.xcor() - (snake_length - i) * 20
    y = snake.ycor()
    snake_segments.append(turtle.Turtle())
    snake_segments[-1].shape("square")
    snake_segments[-1].color("white")
    snake_segments[-1].penup()
    snake_segments[-1].goto(x, y)

# Start the game loop
create_food()
screen.listen()
screen.onkey(lambda: snake.forward(20), "Up")
screen.onkey(lambda: snake.back(20), "Down")
screen.onkey(lambda: snake.right(20), "Right")
screen.onkey(lambda: snake.left(20), "Left")

while True:
    screen.update()
    move_snake()
    check_eat()