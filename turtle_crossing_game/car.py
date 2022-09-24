import turtle
from turtle import Turtle
import random

turtle.colormode(255)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=random.randint(0,500),y=random.randrange(-260, 280))
        self.shape("square")
        self.color(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        self.penup()
    
    def move(self):
        self.goto(x=self.xcor() - 2, y=self.ycor())

    def restart(self):
        self.goto(x=random.randint(300,400),y=random.randrange(-260, 280))
