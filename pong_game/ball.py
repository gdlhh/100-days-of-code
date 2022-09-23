from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()

    def move(self):
        self.fd(15)

    def bounce_wall(self):
        self.setheading(-self.heading())
    
    def bounce_paddle(self):
        self.setheading(self.heading()+180)
    
    def restart(self):
        self.goto(x=0,y=0)
        self.setheading(random.randint(0,360))
