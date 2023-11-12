from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,starting_cords):
        super().__init__()
        self.starting_cords = starting_cords
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(starting_cords)

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

