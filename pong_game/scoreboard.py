from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=position, y=250)
        self.ht()
        self.write(f"{self.score}", align="center", font=('comic sans',18, "normal"))
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align="center", font=('comic sans',18, "normal"))


            
