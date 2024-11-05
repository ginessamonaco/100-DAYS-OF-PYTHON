# import colorgram

# color_list = []
# extracted_colors = colorgram.extract("image.jpg", 16)

# x = 0

# for _ in extracted_colors:
#     color = extracted_colors[x]
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     final_color = (r, g, b)
#     color_list.append(final_color)
#     x += 1

color_list = [(234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164),
              (16, 128, 96), (172, 44, 88), (1, 177, 143), (153, 18, 54), 
              (224, 201, 117), (225, 76, 115), (163, 166, 35),
              (28, 35, 84), (227, 86, 43)]

import turtle
import random

turtle.colormode(255)

timmy = turtle.Turtle()
timmy.speed("fastest")
turtle.setworldcoordinates(-1, -1, 20, 20)
timmy.hideturtle()

def make_row():
    for _ in range(10):
        random_color = random.choice(color_list)

        timmy.pendown()
        timmy.dot(40, random_color)
        timmy.penup()
        timmy.forward(2)


def next_row():
    timmy.left(90)
    timmy.forward(2)
    timmy.right(90)
    timmy.backward(20)


for _ in range(10):
    make_row()
    next_row()


screen = turtle.Screen()
screen.exitonclick()