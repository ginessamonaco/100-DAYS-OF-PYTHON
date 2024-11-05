from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def drive_faster(self):
        self.speed += MOVE_INCREMENT

    def stop_moving(self):
        for car in self.all_cars:
            car.forward(0)