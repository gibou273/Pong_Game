from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

window = Screen()
window.setup(width=800, height=600)
window.title("My Pong Game")
window.bgcolor("black")
window.tracer(0)


right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

window.listen()
window.onkey(key="Up", fun=right_paddle.move_up)
window.onkey(key="Down", fun=right_paddle.move_down)
window.onkey(key="w", fun=left_paddle.move_up)
window.onkey(key="s", fun=left_paddle.move_down)

is_playing = True
while is_playing:
    time.sleep(0.1)
    window.update()
    ball.move()
    # Detect collision with top wall of the game window
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with the right paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect if the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
    # Detect if the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()


window.exitonclick()
