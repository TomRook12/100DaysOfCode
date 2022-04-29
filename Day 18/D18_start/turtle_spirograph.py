import turtle
import random

screen = turtle.Screen()
barry = turtle.Turtle()
barry.speed(0)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        barry.pencolor(random_color())
        barry.circle(100)
        barry.left(size_of_gap)


draw_spirograph(5)


screen.exitonclick()