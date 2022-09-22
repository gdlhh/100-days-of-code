from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddles import Paddles

# initialise the window

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

scoreboard = Scoreboard()
r_paddle = Paddles(580)
l_paddle = Paddles(-590)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()