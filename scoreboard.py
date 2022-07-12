from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.write(f"Level = {self.level}", align="center", font=FONT)

    def game_over(self):
        a = Turtle()
        a.hideturtle()
        a.penup()
        a.write("GAME OVER",align="center",font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level = {self.level}", align="center", font=FONT)