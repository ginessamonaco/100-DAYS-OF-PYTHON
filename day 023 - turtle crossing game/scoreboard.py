from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-218, 260)
        self.number = 1
        self.pendown()
        self.write(f"Level {self.number}", False, "Center", FONT)

    def update_level(self):
        self.clear()
        self.number += 1
        self.write(f"Level {self.number}", False, "Center", FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", False, "Center", ("Courier", 16, "bold"))
