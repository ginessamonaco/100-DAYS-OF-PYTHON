import turtle
import random

screen = turtle.Screen()

def turtle_traits(turtle, color):
    turtle.color("black", color)
    turtle.shape("turtle")
    turtle.shapesize(2)

def get_ready(turtle, spot):
    turtle.penup()
    turtle.backward(300)
    turtle.left(90)
    turtle.forward(spot)
    turtle.right(90)

def make_line(finish_line):
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.forward(300)
    finish_line.right(90)
    finish_line.forward(250)
    finish_line.right(180)
    finish_line.pendown()
    finish_line.forward(475)

def move_forward(turtle):
    turtle.forward(random.randint(2, 20))

red = turtle.Turtle()
turtle_traits(red, "red")
get_ready(red, 175)

orange = turtle.Turtle()
turtle_traits(orange, "orange")
get_ready(orange, 100)

yellow = turtle.Turtle()
turtle_traits(yellow, "yellow")
get_ready(yellow, 25)

green = turtle.Turtle()
turtle_traits(green, "green")
get_ready(green, -50)

blue = turtle.Turtle()
turtle_traits(blue, "blue")
get_ready(blue, -125)

purple = turtle.Turtle()
turtle_traits(purple, "purple")
get_ready(purple, -200)

finish_line = turtle.Turtle()
make_line(finish_line)

guess = input("Which turtle will win?\n(red, orange, yellow, green, blue, purple): ")

turtles = [red, orange, yellow, green, blue, purple]

race_complete = False

while not race_complete:
    for t in turtles:
        move_forward(t)
        x_coordinate = t.xcor()
        if x_coordinate >= 300:
            winner = t
            screen.bgcolor(t.color()[1])
            print(f"{t.color()[1].capitalize()} finished the race 1st!")
            if guess == t.color()[1]:
                print("You guessed correctly so you won!")
            else:
                print(f"You guessed {guess} so you lost.")
            race_complete = True

screen.bye()