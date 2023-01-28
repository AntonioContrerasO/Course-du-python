import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import  ScoreBoard

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800,height=600)
screen.title("Ping-Pong")
screen.tracer(0)

screen.listen()

player_1 = Paddle(350)
player_2 = Paddle(-350)
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(player_1.up,"Up")
screen.onkey(player_1.down,"Down")

screen.onkey(player_2.up,"w")
screen.onkey(player_2.down,"s")


game_is_on = True
speed = 0.1
while game_is_on:
    screen.update()
    time.sleep(speed)
    ball.move()

    if ball.ycor() > 286 or ball.ycor() < -286:
        ball.bounce()
    if (ball.distance(player_1) < 50 and ball.xcor() > 330) or (ball.distance(player_2) < 50 and ball.xcor() < -340):
        speed *= 0.9
        ball.collision_with_paddle()
        print(speed)
    if ball.xcor() > 400:
        ball.restart("")
        scoreboard.l_point()
        speed = 0.1
    if ball.xcor() < -400:
        ball.restart("right")
        scoreboard.r_point()
        speed = 0.1






















screen.exitonclick()
