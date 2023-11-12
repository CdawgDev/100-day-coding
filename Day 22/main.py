from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.listen()
screen.tracer(0)
game_is_running = True

# paddle_body = []
l_starting = (-350,0)
r_starting = (350,0)

r_paddle = Paddle(r_starting)
l_paddle = Paddle(l_starting)

ball = Ball()
scoreboard = Scoreboard()





screen.onkeypress(l_paddle.move_up,"w")
screen.onkeypress(l_paddle.move_down,"s")
screen.onkeypress(r_paddle.move_up,"Up")
screen.onkeypress(r_paddle.move_down,"Down")


while game_is_running:
    screen.update()
    time.sleep(.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #collision with r_paddle or l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    #detect when R paddle misses
    if ball.xcor() >= 400:
        ball.reset_position()
        scoreboard.l_point()

    #Dect When L paddle misses
    if ball.xcor() <= -400:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()