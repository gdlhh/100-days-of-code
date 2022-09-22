from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# initialise the window

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    # detect collision with food

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.score_update()
        snake.extend()
    
    # detect collision with wall

    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # detect collision with tail

    for segment in snake.segments:
        if segment != snake.segments[0]:
            if snake.segments[0].distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False



screen.exitonclick()