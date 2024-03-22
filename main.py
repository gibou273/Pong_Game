from turtle import Turtle, Screen
from paddle import Paddle

window = Screen()
window.setup(width=800, height=600)
window.title("My Pong Game")
window.bgcolor("black")
window.tracer(0)


right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)


def paddle_up(paddle):
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def paddle_down(paddle):
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


window.listen()
window.onkey(key="Up", fun=lambda: paddle_up(right_paddle))
window.onkey(key="Down", fun=lambda: paddle_down(right_paddle))
window.onkey(key="w", fun=lambda: paddle_up(left_paddle))
window.onkey(key="s", fun=lambda: paddle_down(left_paddle))

is_playing = True
while is_playing:
    window.update()

window.exitonclick()
