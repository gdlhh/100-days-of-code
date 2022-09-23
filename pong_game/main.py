from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddles import Paddles
from ball import Ball
import random

# initialise the window

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

midline = Turtle()
midline.color("white")
for i in range(280,-400,-100):
    midline.width(3)
    midline.penup()
    midline.goto(x=0, y=i)
    midline.pendown()
    midline.goto(x=0,y=i-50)
l_scoreboard = Scoreboard(-100)
r_scoreboard = Scoreboard(100)
r_paddle = Paddles(580)
l_paddle = Paddles(-590)
ball = Ball()
ball.setheading(random.randint(0,360))

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

screen.tracer(1)

game_is_on = True

while game_is_on:
    screen.update()
    
    ball.move()

    # detect collision with paddles

    if ball.distance(l_paddle) < 50 or ball.distance(r_paddle) < 50:
        ball.bounce_paddle()
    
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # detect when a player scores
    if ball.xcor() > 590:
        l_scoreboard.update_score()
        ball.restart()
    elif ball.xcor() < -590:
        r_scoreboard.update_score()
        ball.restart()   

screen.exitonclick()