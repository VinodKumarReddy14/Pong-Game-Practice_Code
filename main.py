from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
player = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 52 and ball.xcor() > 325 or ball.distance(l_paddle) < 52 and ball.xcor() < -325:
        ball.bounce2()

    if ball.xcor() > 410:
        player.player_1()
        ball.reset_pos()

    if ball.xcor() < -410:
        player.player_2()
        ball.reset_pos()

screen.exitonclick()
