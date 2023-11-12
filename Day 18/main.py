import turtle as turtle_module
import random
import colorgram

turtle_module.colormode(255)
colors = colorgram.extract('image.jpg',30)
list_of_colors = []
for x in colors:
    r = x.rgb.r
    g = x.rgb.g
    b = x.rgb.b
    list_of_colors.append((r,g,b))

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.ht()
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):

    tim.dot(20,random.choice(list_of_colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()

screen.exitonclick()