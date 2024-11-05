from turtle import Turtle

class MiddleLine(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.color("yellow")
        self.goto(-100, 170)
        self.write(self.l_score, False, "center", ("Courier", 80, "bold"))
        self.goto(100, 170)
        self.write(self.r_score, False, "center", ("Courier", 80, "bold"))

    def l_point(self):
        self.l_score += 1
        self.make_line()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.make_line()
        self.update_scoreboard()

    def make_line(self):
        self.hideturtle()
        self.penup()
        self.pensize(2)
        self.color("white")
        self.goto(0, 300)
        self.setheading(270)
        done = False
        while not done:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
            if self.ycor() <= -300:
                done = True