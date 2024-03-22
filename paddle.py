from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.xpos = x_pos
        self.y_pos = y_pos
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=self.xpos, y=self.y_pos)
