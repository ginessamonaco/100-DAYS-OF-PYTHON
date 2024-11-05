from random import randint
from turtle import Turtle

class Food(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("light blue")
        self.relocate()

    def relocate(self):
        random_xcor = randint(-280, 280)
        random_ycor = randint(-280, 280)
        self.goto(random_xcor, random_ycor)