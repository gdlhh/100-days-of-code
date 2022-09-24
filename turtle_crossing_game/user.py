from turtle import Turtle

class User(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.goto(x=0,y=-280)
        self.setheading(90)
    
    def up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def left(self):
        self.goto(x=self.xcor() - 20, y=self.ycor())
    
    def right(self):
        self.goto(x=self.xcor() + 20, y=self.ycor())

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)