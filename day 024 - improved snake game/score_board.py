from turtle import Turtle

ALIGNMENT = "center"
FONT1 = ("Courier", 18, "normal")
FONT2 = ("Courier", 28, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.highest_score = int(data.read())
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Current Score: {self.score}   Highest Score: {self.highest_score}", False, ALIGNMENT, FONT1)
        self.hideturtle()
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Current Score: {self.score}   Highest Score: {self.highest_score}", False, ALIGNMENT, FONT1)

    def keep_track(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.clear()
        self.write(f"Current Score: {self.score}   Highest Score: {self.highest_score}", False, ALIGNMENT, FONT1)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("yellow")
    #     self.write(f"GAME OVER", False, ALIGNMENT, FONT2)