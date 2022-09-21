from re import X
from turtle import Screen, Turtle, color
import time

# initialise the window

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
x_position = 0
turtle_list = []
screen.tracer(0)

# initialising the snake
for turtle in range(0,3):
    x_position -= 20
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.shape("square")
    new_turtle.goto(x=x_position, y=0)
    turtle_list.append(new_turtle)



# moving the turtles forwards
while True:
    screen.update()
    time.sleep(.1)
    for turtle_index in range(len(turtle_list) - 1,0,-1):
        new_x = turtle_list[turtle_index -1].xcor()
        new_y = turtle_list[turtle_index -1].ycor()
        turtle_list[turtle_index].goto(x=new_x, y=new_y)
    turtle_list[0].fd(20)
    
        

screen.exitonclick()