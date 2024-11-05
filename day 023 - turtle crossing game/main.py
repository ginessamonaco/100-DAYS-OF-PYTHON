import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()

screen.listen()
screen.onkeypress(timmy.move_forward, "Up")

score_board = Scoreboard()
car_manager = CarManager()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.drive()

    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            game_on = False

    if timmy.ycor() >= 290:
        score_board.update_level()
        timmy.reset()
        car_manager.drive_faster()

score_board.game_over()
car_manager.stop_moving()
screen.bgcolor("dark red")

screen.exitonclick()