from random import randint
from turtle import Turtle, Screen
from score_board import ScoreBoard
from food import Food
from snake import Snake
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_on = True

while game_on:
    screen.update()
    sleep(0.14)
    snake.move()

    if snake.head.distance(food) < 16:
        food.relocate()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 294 or snake.head.xcor() < -294 or snake.head.ycor() > 294 or snake.head.ycor() < -294:
        scoreboard.keep_track()
        snake.snake_restart()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.keep_track()
            snake.snake_restart()

screen.exitonclick()


