from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()

    def move(self):
        self.fd(5)

    def bounce_wall(self):
        self.setheading(-self.heading())
    
    def bounce_paddle(self):
        self.setheading(self.heading()+180)
