from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.setheading(random.randrange(0, 45))
        self.move_speed = 10

    def move(self):
        self.forward(self.move_speed)

    def bounce_wall(self):
        new_angle = 360 - self.heading()
        self.setheading(new_angle)
        self.forward(10)

    def bounce_paddle(self):
        new_angle = 180 - self.heading()
        self.setheading(new_angle)
        self.move_speed += 5
        self.forward(self.move_speed)

    def reset(self):
        self.goto(0, 0)
        position = 180 - self.heading()
        self.setheading(position)
        self.move_speed = 10
