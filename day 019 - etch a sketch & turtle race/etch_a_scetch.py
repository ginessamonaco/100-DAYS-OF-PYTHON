import turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def move_forward():
    t.forward(4)

def move_backward():
    t.backward(4)

def turn_counter_clockwise():
    t.left(4)
    t.forward(4)

def turn_clockwise():
    t.right(4)
    t.forward(4)

def clear_screen():
    t.penup()
    t.clear()
    t.home()
    t.pendown()

t = turtle.Turtle()

screen = turtle.Screen()

screen.listen()
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_counter_clockwise, "Left")
screen.onkeypress(turn_clockwise, "Right")
screen.onkey(clear_screen, "c")


screen.exitonclick()