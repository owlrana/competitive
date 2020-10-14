# DX-Ball type game 

import turtle # has in-built functions we can use, can also use pygame

wn = turtle.Screen()
wn.title("DX-Ball by owlrana")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # helps control the time it takes for window to refresh

# Paddle A
paddle_a = turtle.Turtle() # turtle is module and Turtle is the class name
paddle_a.speed(0) # speed of animation, not the speed of paddhle movement
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0) # we set 800 width so we want it on the edge

# Paddle B
paddle_b = turtle.Turtle() # turtle is module and Turtle is the class name
paddle_b.speed(0) # speed of animation, not the speed of paddhle movement
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) # we set 800 width so we want it on the edge


# Ball
ball = turtle.Turtle() # turtle is module and Turtle is the class name
ball.speed(0) # speed of animation, not the speed of paddhle movement
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) # we set 800 width so we want it on the edge
ball.dx = 2
ball.dy = 2

# Function to move the paddles
def paddle_a_up():
    y = paddle_a.ycor() # method from turtle module that returns the y coordinate
    y += 20
    paddle_a.sety(y) # sets the new coordinate to y

def paddle_a_down():
    y = paddle_a.ycor() # method from turtle module that returns the y coordinate
    y -= 20
    paddle_a.sety(y) # sets the new coordinate to y

def paddle_b_up():
    y = paddle_b.ycor() # method from turtle module that returns the y coordinate
    y += 20
    paddle_b.sety(y) # sets the new coordinate to y

def paddle_b_down():
    y = paddle_b.ycor() # method from turtle module that returns the y coordinate
    y -= 20
    paddle_b.sety(y) # sets the new coordinate to y

# Keyboard binding to call the function to move paddles
wn.listen() # waits for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)