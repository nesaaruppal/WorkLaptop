from turtle import * 
import random
from matplotlib import * 

## Create an empty dictionary - use this to track who's put what where.
    # Add the items to it 
    # If x and y in this dictionary = you win or lose or pass your go 



##### DRAW BOARD #####

def outer_square(self):
    self.forward(450)
    self.left(90)
    self.forward(450)
    self.left(90)
    self.forward(450)
    self.left(90)
    self.forward(450)
    self.left(90)

def vertical1(self):
    self.forward(150)
    self.left(90)
    self.forward(450)

def vertical2(self):
    self.right(90)
    self.forward(150)
    self.right(90)
    self.forward(450)
    
def horizontal1(self):
    self.left(90)
    self.forward(150)
    self.left(90)
    self.forward(150)
    self.left(90)
    self.forward(450)
    
def horizontal2(self):
    self.right(90)
    self.forward(150)
    self.right(90)
    self.forward(450)


##### LEFT CROSSES SIDE #####

def bl_cross(self):
    self = Turtle()
    self.hideturtle()
    self.pencolor("red")
    self.pensize(3)
    self.penup()
    self.speed("fastest")
    self.goto(x=-200, y=-200)
    self.setheading(45)
    self.pendown()
    self.forward(150)
    self.penup()
    self.goto(x=-200, y=-100)
    self.pendown()
    self.setheading(315)
    self.pendown()
    self.forward(150)
    
def ml_cross(self):
    self = Turtle()
    self.hideturtle()
    self.pencolor("red")
    self.pensize(3)
    self.penup()
    self.speed("fastest")
    self.goto(x=-200, y=-50)
    self.setheading(45)
    self.pendown()
    self.forward(150)
    self.penup()
    self.goto(x=-200, y=50)
    self.pendown()
    self.setheading(315)
    self.pendown()
    self.forward(150)

def tl_cross(self):
    self = Turtle()
    self.hideturtle()
    self.pencolor("red")
    self.pensize(3)
    self.penup()
    self.speed("fastest")
    self.goto(x=-200, y=100)
    self.setheading(45)
    self.pendown()
    self.forward(150)
    self.penup()
    self.goto(x=-200, y=200)
    self.pendown()
    self.setheading(315)
    self.pendown()
    self.forward(150)

##### LEFT CIRCLES SIDE #####
                
def bl_circle(self):
    self = Turtle()
    self.color("blue")
    self.hideturtle()
    self.speed("fastest")
    self.penup()
    self.pensize(5)
    self.goto(x=-150, y=-200)
    self.pendown()   
    self.circle(50) 
    
def ml_circle(self):
    self = Turtle()
    self.color("blue")
    self.hideturtle()
    self.speed("fastest")
    self.penup()
    self.pensize(5)
    self.goto(x=-150, y=-50)
    self.pendown()   
    self.circle(50) 

def tl_circle(self):
    self = Turtle()
    self.color("blue")
    self.hideturtle()
    self.speed("fastest")
    self.penup()
    self.pensize(5)
    self.goto(x=-150, y=100)
    self.pendown()   
    self.circle(50) 

##### MIDDLE CROSSES #####

def b_cross(self):
    self = Turtle()
    self.hideturtle()
    self.pencolor("red")
    self.pensize(3)
    self.penup()
    self.speed("fastest")
    self.goto(x=-50, y=-200)
    self.setheading(45)
    self.pendown()
    self.forward(150)
    self.penup()
    self.goto(x=-50, y=-100)
    self.pendown()
    self.setheading(315)
    self.pendown()
    self.forward(150)
    
def m_cross(self):
    self = Turtle()
    self.hideturtle()
    self.pencolor("red")
    self.pensize(3)
    self.penup()
    self.speed("fastest")
    self.goto(x=-50, y=-50)
    self.setheading(45)
    self.pendown()
    self.forward(150)
    self.penup()
    self.goto(x=-50, y=50)
    self.pendown()
    self.setheading(315)
    self.pendown()
    self.forward(150)

def t_cross(self):
    self = Turtle()
    self.hideturtle()
    self.pencolor("red")
    self.pensize(3)
    self.penup()
    self.speed("fastest")
    self.goto(x=-50, y=100)
    self.setheading(45)
    self.pendown()
    self.forward(150)
    self.penup()
    self.goto(x=-50, y=200)
    self.pendown()
    self.setheading(315)
    self.pendown()
    self.forward(150)

##### MIDDLE CIRCLES #####

def b_circle(self):
    self = Turtle()
    self.color("blue")
    self.hideturtle()
    self.speed("fastest")
    self.penup()
    self.pensize(5)
    self.goto(x=0, y=-200)
    self.pendown()   
    self.circle(50) 

def m_circle(self):
    self = Turtle()
    self.color("blue")
    self.hideturtle()
    self.speed("fastest")
    self.penup()
    self.pensize(5)
    self.goto(x=0, y=-50)
    self.pendown()   
    self.circle(50) 

def t_circle(self):
    self = Turtle()
    self.color("blue")
    self.hideturtle()
    self.speed("fastest")
    self.penup()
    self.pensize(5)
    self.goto(x=0, y=100)
    self.pendown()   
    self.circle(50) 

##### RIGHT CROSSES #####

def br_cross(self):
    self = Turtle()
    self.hideturtle()
    self.pencolor("red")
    self.pensize(3)
    self.penup()
    self.speed("fastest")
    self.goto(x=100, y=-200)
    self.setheading(45)
    self.pendown()
    self.forward(150)
    self.penup()
    self.goto(x=100, y=-100)
    self.pendown()
    self.setheading(315)
    self.pendown()
    self.forward(150)
    
def mr_cross(self):
    self = Turtle()
    self.hideturtle()
    self.pencolor("red")
    self.pensize(3)
    self.penup()
    self.speed("fastest")
    self.goto(x=100, y=-50)
    self.setheading(45)
    self.pendown()
    self.forward(150)
    self.penup()
    self.goto(x=100, y=50)
    self.pendown()
    self.setheading(315)
    self.pendown()
    self.forward(150)
    
def tr_cross(self):
    self = Turtle()
    self.hideturtle()
    self.pencolor("red")
    self.pensize(3)
    self.penup()
    self.speed("fastest")
    self.goto(x=100, y=100)
    self.setheading(45)
    self.pendown()
    self.forward(150)
    self.penup()
    self.goto(x=100, y=200)
    self.pendown()
    self.setheading(315)
    self.pendown()
    self.forward(150)

##### RIGHT CIRCLES SIDE #####

def br_circle(self):
    self = Turtle()
    self.color("blue")
    self.hideturtle()
    self.speed("fastest")
    self.penup()
    self.pensize(5)
    self.goto(x=150, y=-200)
    self.pendown()   
    self.circle(50) 

def mr_circle(self):
    self = Turtle()
    self.color("blue")
    self.hideturtle()
    self.speed("fastest")
    self.penup()
    self.pensize(5)
    self.goto(x=150, y=-50)
    self.pendown()   
    self.circle(50) 

def tr_circle(self):
    self = Turtle()
    self.color("blue")
    self.hideturtle()
    self.speed("fastest")
    self.penup()
    self.pensize(5)
    self.goto(x=150, y=100)
    self.pendown()   
    self.circle(50) 


screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("#AEDFF7")

t = Turtle()
t.hideturtle()
t.color("black")
t.speed("fastest")
t.penup()
t.pensize(3)
t.goto(x=-225, y=-225)
t.pendown()


dictionary = {
    ##### CROSSES #####
    1: bl_cross,
    2: b_cross,
    3: br_cross, 
    4: ml_cross,
    5: m_cross, 
    6: mr_cross, 
    7: tl_cross,
    8: t_cross,
    9: tr_cross,
    ##### CIRCLES ######
    11: bl_circle, 
    12: b_circle, 
    13: br_circle,
    14: ml_circle,
    15: m_circle,
    16: mr_circle,
    17: tl_circle,
    18: t_circle, 
    19: tr_circle, 
}

    
used_squares = []
#Change to list???


outer_square(t)
vertical1(t)
vertical2(t)
horizontal1(t)
horizontal2(t)


print("Let's Play Tic Tac Toe!\n\n")

print("The Rules:")
print("--> You will enter the number of the square where you would like place your circle or cross.")
print("--> For crosses you will enter a number between 1 and 9.\nIf you are circles you will enter a number from 10 to 19.")
print("--> The board will be like this for crosses:\n[7][8][9]\n[4][5][6]\n[1][2][3]!")
print("--> The board will be like this for circles:\n[17][18][19]\n[14][15][16]\n[11][12][13]!")

game_is_on = True
while game_is_on:

    print(used_squares)
    
    chosen_square = (input("You are CROSSES! Choose your square:\n"))
    chosen_cross_square = int(chosen_square)
    
    if chosen_cross_square in used_squares:
        print("That square has already been taken!! Look at the board again!\nFocus. Regroup. Remember how to place your cross!!!")

                ##### CROSSES #####
    if chosen_cross_square == 1:
        dictionary[1] == bl_cross(t)
        used_squares.append(1)
    elif chosen_cross_square == 2: 
        dictionary[2] == b_cross(t)
        used_squares.append (2)
    elif chosen_cross_square == 3: 
        dictionary[3] == br_cross(t)
        used_squares.append (3)
        
    elif chosen_cross_square == 4: 
        dictionary[4] == ml_cross(t)
        used_squares.append (4)
    elif chosen_cross_square == 5: 
        dictionary[5] == m_cross(t)
        used_squares.append (5)
    elif chosen_cross_square == 6: 
        dictionary[6] == mr_cross(t)
        used_squares.append (6)
        
    elif chosen_cross_square == 7: 
        dictionary[7] == tl_cross(t)
        used_squares.append (7)
    elif chosen_cross_square == 8: 
        dictionary[8] == t_cross(t)
        used_squares.append (8)
    elif chosen_cross_square == 9: 
        dictionary[9] == tr_cross(t)
        used_squares.append (9)

            ##### CIRCLES #####

    chosen_square = (input("You are NAUGHTS! Choose your square:\n"))
    chosen_circle_square = int(chosen_square)
    
    if chosen_circle_square in used_squares:
        print("That square has already been taken!! Look at the board again!\nFocus. Regroup. Remember how to place your cross!!!")
    
    if chosen_circle_square == 11:
        dictionary[11] == bl_circle(t)
        used_squares.append (11)
    elif chosen_circle_square == 12: 
        dictionary[12] == b_circle(t)
        used_squares.append (12)
    elif chosen_circle_square == 13: 
        dictionary[13] == br_circle(t)
        used_squares.append (13)
        
    elif chosen_circle_square == 14: 
        dictionary[14] == ml_circle(t)
        used_squares.append (14)
    elif chosen_circle_square == 15: 
        dictionary[15] == m_circle(t)
        used_squares.append (15)
    elif chosen_circle_square == 16: 
        dictionary[16] == t_circle(t)
        used_squares.append (16)
        
    elif chosen_circle_square == 17: 
        dictionary[17] == tl_circle(t)
        used_squares.append (17)
    elif chosen_circle_square == 18: 
        dictionary[18] == t_circle(t)
        used_squares.append (18)
    elif chosen_circle_square == 19: 
        dictionary[19] == tr_circle(t)
        used_squares.append (19)

    else:
        continue
        
        ##############Append the new dictionary to have the full "1:bl_cross"
        
        
                    ##### WINNER? #####
    
    ##### CROSSES #####
    
                ##### Horizontal #####
    for _ in used_squares:                           # Use continue or pass????
        if 1 and 2 and 3 in used_squares:
            textinput(title="CROSSES WINS!", prompt="Horizontal!")
            game_is_on = False
        else:
            pass
                        
        if 4 and 5 and 6 in used_squares:
            textinput(title="CROSSES WINS", prompt="Horizontal!")
            game_is_on = False
        else:
            pass
                    
        if 7 and 8 and 9 in used_squares:
            textinput(title="CROSSES WINS", prompt="Horizontal!")
            game_is_on = False
        else:
            pass
        
                    ##### Vertical #####
        if 1 and 4 and 7 in used_squares:
            textinput(title="CROSSES WINS!", prompt="Vertical!")
            game_is_on = False
        else:
            pass
        
        if 2 and 5 and 8 in used_squares:
            textinput(title="CROSSES WINS", prompt="Vertical!")
            game_is_on = False
        else:
            pass
        
        if 3 and 6 and 9 in used_squares:
            textinput(title="CROSSES WINS", prompt="Vertical!")
            game_is_on = False
        else:
            pass
        
                    ##### Diagonal l --> r #####
        if 1 and 5 and 9 in used_squares:
            textinput(title="CROSSES WINS!", prompt="Diagonal!")
            game_is_on = False
        else:
            pass
                
        if 3 and 5 and 7 in used_squares: 
            textinput(title="CROSSES WINS", prompt="Diagonal!")
            game_is_on = False
        else:
            pass

                    
                ##### CIRCLES #####
                        ##### Horizontal #####
        if 11 and 12 and 13 in used_squares:
            textinput(title="CIRCLES WINS!", prompt="Horizontal!")
            game_is_on = False
        else:
            pass

        if 14 and 15 and 16 in used_squares:
            textinput(title="CIRCLES WINS!", prompt="Horizontal!")
            game_is_on = False
        else:
            pass
        
        if 17 and 18 and 19 in used_squares:
            textinput(title="CIRCLES WINS!", prompt="Horizontal!")
            game_is_on = False
        else:
            pass
        
                    ##### Vertical #####
        if 11 and 14 and 17 in used_squares:
            textinput(title="CIRCLES WINS!", prompt="Vertical!!")
            game_is_on = False
        else:
            pass
        
        if 12 and 15 and 18 in used_squares:
            textinput(title="CIRCLES WINS!", prompt="Vertical!!")
            game_is_on = False
        else:
            pass
        
        if 13 and 16 and 19 in used_squares: 
            textinput(title="CIRCLES WINS", prompt="Vertical!!")
            game_is_on = False
        else:
            pass
        
                    ##### Diagonal l --> r ######
        if 11 and 15 and 19 in used_squares:
            textinput(title="CIRCLES WINS!", prompt="Diagonal!!")
            game_is_on = False
        else:
            pass
        
        if 17 and 15 and 13  in used_squares:
            textinput(title="CIRCLES WINS", prompt="Diagonal!!")
            game_is_on = False
        else:
            pass


screen.mainloop()




