from turtle import Turtle, Screen
from random import randint
from time import sleep

screen = Screen()
screen.setup(width=1000, height=400)

def get_ready(turtle, turtle_color, y_axis):
    # Create all turtles and move them to their starting points
    turtle.shape("turtle")
    turtle.shapesize(2)
    turtle.penup()
    turtle.color("black", turtle_color)
    turtle.goto(x=-420, y=y_axis)

def make_finish_line(turtle):
    # Create the finish line that a turtle must touch to win
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x=420, y=-160)
    turtle.pendown()
    turtle.goto(x=420, y=160)

def count_down(turtle, writing, x_axis, font_size):
    # Use to write on the screen. For example: 3 2 1 RACE
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x=x_axis, y=-70)
    turtle.write(arg=writing, move=False, align="left", font=("Courier New", font_size, "bold"))
    
# All turtles getting created and sent to their starting points
red = Turtle()
get_ready(turtle=red, turtle_color="red", y_axis=125)
orange = Turtle()
get_ready(turtle=orange, turtle_color="orange", y_axis=75)
yellow =Turtle()
get_ready(turtle=yellow, turtle_color="yellow", y_axis=25)
green = Turtle()
get_ready(turtle=green, turtle_color="green", y_axis=-25)
blue = Turtle()
get_ready(turtle=blue, turtle_color="blue", y_axis=-75)
purple = Turtle()
get_ready(turtle=purple, turtle_color="purple", y_axis=-125)

# The finish line getting drawn
finish_line = Turtle()
make_finish_line(finish_line)

# Take the user's bet
user_bet = screen.textinput(title="Make Your Bet", prompt="Which color turtle will win the race? Enter a color:").lower()

# Count down from 3 2 1 RACE
count_down_turtle = Turtle()
count_down(turtle=count_down_turtle, writing="3", x_axis=-200, font_size=100)
sleep(.25)
count_down(turtle=count_down_turtle, writing="2", x_axis=-60, font_size=100)
sleep(.25)
count_down(turtle=count_down_turtle, writing="1", x_axis=80, font_size=100)
sleep(.5)
count_down_turtle.clear()
count_down(turtle=count_down_turtle, writing="RACE", x_axis=-180, font_size=100)
sleep(.5)
count_down_turtle.clear()


turtle_colors = [red, orange, yellow, green, blue, purple]
turtle_colors_str = ["red", "orange", "yellow", "green", "blue", "purple"]

race_finished = False

while not race_finished:
    for turtle in turtle_colors:
        turtle.forward(randint(1, 16))
        xcor = int(turtle.xcor())
        if xcor >= 420:
            winning_turtle = turtle_colors_str[turtle_colors.index(turtle)]
            race_finished = True

screen.bgcolor(winning_turtle)
count_down(turtle=count_down_turtle, writing=f"{winning_turtle.capitalize()} won the race! You bet {user_bet}.", x_axis=-300, font_size=20)
sleep(3)
count_down_turtle.clear()
if user_bet == winning_turtle:
    count_down(turtle=count_down_turtle, writing="YOU WON :)", x_axis=-300, font_size=50)
else:
    count_down(turtle=count_down_turtle, writing="YOU LOST :(", x_axis=-300, font_size=50)
    
sleep(2)

screen.exitonclick()