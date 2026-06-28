from turtle import Turtle 

class Paddles(Turtle):
    def __init__(self,positions,color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color(color)
        self.penup()
        self.goto(positions)
    
    def go_up(self):
        self.goto(self.xcor(),self.ycor()+40)
        
    def go_down(self):
        self.goto(self.xcor(),self.ycor()-40)
        