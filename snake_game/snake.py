from turtle import Screen, Turtle, color
import time


x_position = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self): 
        global x_position
        for turtle in range(0,3):
            x_position -= 20
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.shape("square")
            new_turtle.goto(x=x_position, y=0)
            self.segments.append(new_turtle)

    def extend(self):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.shape("square")
        last_segment_xpos = self.segments[-1].xcor()
        last_segment_ypos = self.segments[-1].ycor()
        new_turtle.goto(x=last_segment_xpos, y=last_segment_ypos)
        self.segments.append(new_turtle)
    
    def move(self):
        for segment in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[segment -1].xcor()
            new_y = self.segments[segment -1].ycor()
            self.segments[segment].goto(x=new_x, y=new_y)
        self.segments[0].fd(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
