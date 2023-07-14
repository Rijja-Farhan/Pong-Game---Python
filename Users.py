from turtle import Turtle

class User(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.user_paddle = Turtle("square")
        self.user_paddle.shapesize(stretch_wid =5, stretch_len=1)
        self.user_paddle.color("white")
        self.user_paddle.penup()
        self.user_paddle.goto(pos)



    def move_up(self):

            new_y = self.user_paddle.ycor()+20
            self.user_paddle.goto(self.user_paddle.xcor(),new_y)
    def move_down(self):
           new_y = self.user_paddle.ycor()-20
           self.user_paddle.goto(self.user_paddle.xcor(),new_y)

