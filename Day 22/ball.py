from turtle import Turtle

GAME_MAX_HEIGHT = 300
GAME_MAX_WIDTH = 400

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def reset_position(self):
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.bounce_x()
    def increase_speed(self):
        if self.x_move > 0:
            self.x_move += .5
        else:
            self.x_move -= .5
        if self.y_move > 0:
            self.y_move += .5
        else:
            self.y_move -= .5
        # self.y_move += 1
        print(self.x_move,self.y_move)