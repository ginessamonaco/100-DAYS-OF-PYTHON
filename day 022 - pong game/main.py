from turtle import Screen, Turtle
from paddle import Paddle
from score_line import MiddleLine
import random
from ball import Ball
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("The Pong Game")
screen.tracer(0)

middle_line = MiddleLine()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

keep_playing = True
while keep_playing:

    pong_ball = Ball()

    game_on = True
    while game_on:
        middle_line.update_scoreboard()
        middle_line.make_line()

        sleep(0.1)
        screen.update()
        pong_ball.move()
        
        if pong_ball.ycor() > 290 or pong_ball.ycor() < -280:
            pong_ball.bounce_wall()
        
        if pong_ball.distance(right_paddle) < 50 and pong_ball.xcor() > 340 or pong_ball.distance(left_paddle) < 50 and pong_ball.xcor() < -340:
            pong_ball.bounce_paddle()

        if pong_ball.xcor() > 380:
            pong_ball.reset()
            middle_line.l_point()
        
        if pong_ball.xcor() < -368:
            pong_ball.reset()
            middle_line.r_point()


screen.exitonclick()