from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.s1=0
        self.s2=0
        self.hideturtle()
        self.color("white")
        self.penup()
        
        self.update_score()
        
    def update_score(self):
        
        self.clear()
        self.goto(-100,300)
        self.write(self.s1,align="center",font=("courier",30,"normal"))
        self.goto(100,300)
        self.write(self.s2,align="center",font=("courier",30,"normal"))
        
    def increase_s1(self):
        self.s1+=1
        self.update_score()
        
    def increase_s2(self):
        self.s2+=1
        self.update_score()
        
    def game_over(self):
        self.screen.bgcolor("darkred")
        self.goto(0,0)
        self.write(f"Game over \nFinal Score: {self.score}",align="center",font={"Arial",28,"normal"})
        