from turtle import Turtle

class Paddle():
    
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.hideturtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()

    def paddle_position(self, right_left):
        if right_left == "right":
            self.paddle.goto(350, 0)
        elif right_left == "left":
            self.paddle.goto(-350, 0)

    def move_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def move_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

