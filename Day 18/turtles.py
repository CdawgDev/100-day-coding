from turtle import Screen
import turtle
import random
import colorgram
t = turtle.Turtle()

t.shape("turtle")
screen = Screen()
colors = colorgram.extract('image.jpg',30)
list_of_colors = []
for x in colors:
    r = x.rgb.r
    g = x.rgb.g
    b = x.rgb.b
    list_of_colors.append((r,g,b))

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)

def draw_square():
    for x in range(4):
        t.forward(100)
        t.left(90)

def draw_dotted_line():
    for x in range(15):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
def draw_shapes():
    sides = 3
    count = 0
    angle = 360 / sides
    while sides < 10:
        t.pencolor(random_color())
        for _ in range(sides):
            count += 1
            t.right(angle)
            t.forward(100)
        sides += 1
        angle = 360 / sides
def random_walk():
    t.pensize(10)
    t.speed("fastest")
    direction = [0,90,180,270]
    for _ in range(200):
        t.pencolor(random_color())
        turtle_direction = random.choice(direction)
        t.forward(30)
        t.setheading(turtle_direction)

def sphere_thing():
    t.speed("fastest")
    degree_of_rotation = 5
    range_of_circle = round(360 / degree_of_rotation)
    for x in range(range_of_circle):
        t.pencolor(random_color())
        t.circle(100)
        t.right(degree_of_rotation)
def draw_filled_circle():
    # color_choice = random.choice(list_of_colors)
    screen_width = -(screen.window_width() / 2)
    screen_height = -(screen.window_height() / 2)
    screen_height += 100
    t.speed("fastest")
    t.penup()
    t.goto(screen_width,screen_height)

    count = 0
    for _ in range(100):
        count += 1
        if count % 10 == 0:
            t.penup()
            screen_height += 100
            t.goto(screen_width,screen_height)
        print(t.pos())
        color_choice = random.choice(list_of_colors)
        t.pendown()
        t.color(color_choice)
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        t.penup()
        t.forward(100)


draw_filled_circle()
screen.exitonclick()