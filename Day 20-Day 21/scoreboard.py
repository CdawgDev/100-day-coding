from turtle import Turtle

TEXT_ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("pink")
        self.goto(0,280)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=TEXT_ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=TEXT_ALIGNMENT, font=FONT)