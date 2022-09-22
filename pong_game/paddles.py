from turtle import Turtle

class Paddles(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=position,y=0)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)