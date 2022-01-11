from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


L_paddle = Paddle((-350, 0))
R_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(fun=L_paddle.go_up, key="w")
screen.onkeypress(fun=L_paddle.go_down, key="s")

screen.onkeypress(fun=R_paddle.go_up, key="Up")
screen.onkeypress(fun=R_paddle.go_down, key="Down")

game_is_on = True

while game_is_on:
    # While the game is on ball will keep on moving, and we will
    # change its direction according to collisions mentioned below
    ball.move()
    time.sleep(ball.move_speed)
    # Updating screen once ball is moved
    screen.update()

    # Detecting collision on top and bottom wall and bouncing the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detection collision with paddle and bouncing the ball
    if ball.distance(R_paddle) < 50 and ball.xcor() > 320 or ball.distance(L_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed()

    # Detecting if right paddle misses the ball and updating the left score
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # Detecting if left paddle misses the ball and updating the right score
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
