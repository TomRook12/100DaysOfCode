import turtle as t
import random


directions = [90, 180, 270, 360]

screen = t.Screen()

steve = t.Turtle()
steve.pensize(5)
steve.speed(0)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

for _ in range(200):
    steve.pencolor(random_color())
    steve.forward(25)
    steve.setheading(random.choice(directions))

screen.exitonclick()
