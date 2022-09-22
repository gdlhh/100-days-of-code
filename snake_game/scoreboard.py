from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0,y=280)
        self.ht()
        self.write(f"Score: {self.score}", align="center", font=('comic sans',14, "normal"))
    
    def score_update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=('comic sans', 14,"normal"))

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER", align="center", font=("comic sans", 24, "normal"))
        
