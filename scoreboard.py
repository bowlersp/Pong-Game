from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Right_Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(200, 250)
        self.score = 0
        self.color("white")
        self.updaterightscoreboard()
        self.hideturtle()

    def updaterightscoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score_right(self):
        self.clear()
        self.score += 1
        self.updaterightscoreboard()


class Left_Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-200, 250)
        self.score = 0
        self.color("white")
        self.updateleftscoreboard()
        self.hideturtle()

    def updateleftscoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.clear()
        self.score += 1
        self.updateleftscoreboard()