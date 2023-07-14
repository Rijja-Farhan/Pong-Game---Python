import turtle
from turtle import Turtle,Screen
from Users import User
from Ball import Ball
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("pong")
screen.tracer(0)

right_paddle = User((270,0))
left_paddle = User((-270,0))
screen.listen()
screen.onkey(right_paddle.move_up,"Up")
screen.onkey(right_paddle.move_down,"Down")

screen.onkey(left_paddle.move_up,"w")
screen.onkey(left_paddle.move_down,"x")

game_is_on= True





my_ball = Ball()



while game_is_on:
    time.sleep(0.1)
    screen.update()
    my_ball.move_right()

    # Detect collision with walls
    if my_ball.ycor() >= 280 or my_ball.ycor() <= -280:
        my_ball.bounce()

    #detect collision with r_paddle
    if  my_ball.distance(right_paddle) < 50 and my_ball.xcor() > 300:
      print("ok")





screen.exitonclick()


