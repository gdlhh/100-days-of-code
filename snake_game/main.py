from turtle import Screen
from snake import Snake
import time


# initialise the window

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()


screen.exitonclick()