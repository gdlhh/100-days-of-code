from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.goto(x=-100, y=250)
        self.write(f"{self.score1}", align="center", font=('comic sans',18, "normal"))
        self.goto(x=100, y=250)
        self.write(f"{self.score2}", align="center", font=('comic sans',18, "normal"))
        self.midline()
    
    def midline(self):
        self.color("white")
        for i in range(280,-400,-100):
            self.width(3)
            self.penup()
            self.goto(x=0, y=i)
            self.pendown()
            self.goto(x=0,y=i-50)
    
    # def update_score(self):
    #     self.score1 += 1
    #     self.score2 += 1

            
