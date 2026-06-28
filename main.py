from paddle import Paddles
from turtle import Screen
from ball import  Ball 
from score import Score
import time


window = Screen()
window.bgcolor("black")
window.setup(800,680)
window.title("Octucode: Ping Poing")
window.tracer(0)

r_paddle = Paddles((380,0),"blue")
l_paddle = Paddles( (-380,0),"red")
ball = Ball()
s = Score()

window.listen()

window.onkey(r_paddle.go_up,"Up")
window.onkey(r_paddle.go_down,"Down")

window.onkey(l_paddle.go_up,"w")
window.onkey(l_paddle.go_down,"s")

sleep = 0.1
game_on = True
while game_on:
    window.update()
    time.sleep(sleep)
    
    # تحريك الكرة
    ball.goto(ball.xcor()+ ball.x_move ,ball.ycor()+ball.y_move)
    
    # اكتشاف التصادم مع الجدار العلوي و السفلي
    if ball.ycor()>=290 or ball.ycor()<=-310:
        ball.y_move*=-1
    
    # اكتشاف التصادم مع المضارب   
    if (ball.xcor()>=330 and ball.distance(r_paddle)<=40  ) or (ball.xcor()<=-330 and ball.distance(l_paddle)<=40  ):
        ball.x_move*=-1 
        sleep*=0.9       
    # اذا خرجت من الجهة اليمنة
    if ball.xcor()>400 :
        ball.goto(0,0)
        ball.x_move*=-1
        s.increase_s1()
        sleep=0.1
    # اذا خرجت من الجهة اليسرة
    if  ball.xcor()<-400:
        ball.goto(0,0)
        ball.x_move*=-1
        s.increase_s2()
        sleep = 0.1
        
        
        
window.exitonclick()