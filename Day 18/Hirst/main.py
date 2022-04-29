#import colorgram
#
#colors = colorgram.extract("image.jpg", 30)
#print(colors)
#
#rgb_list = []
#
#for i in range(len(colors)):
#    all_color_info = colors[i] # Get each color
#    rgb_dirty_tuple = all_color_info.rgb
#    rgb_dirty_list = list(rgb_dirty_tuple)
#    rgb_clean_tuple = tuple(rgb_dirty_list)
#    rgb_list.append(rgb_clean_tuple)
#
#print(rgb_list)
import turtle
from turtle import Turtle, Screen
import random

color_list = [(218, 154, 94), (39, 111, 148), (120, 168, 194), (199, 131, 155), (212, 228, 217), (149, 66, 90), (193, 88, 114), (33, 133, 96), (164, 75, 53), (211, 87, 66), (125, 182, 159), (235, 216, 222), (232, 198, 117), (162, 158, 48), (211, 222, 229), (54, 169, 141), (50, 158, 177), (237, 170, 160), (234, 163, 179), (14, 99, 73), (152, 212, 199), (108, 44, 62), (41, 59, 102), (115, 115, 160), (147, 207, 216), (35, 49, 83), (64, 43, 62), (18, 70, 53), (4, 103, 115)]
richard = Turtle()
richard.penup()
richard.hideturtle()
richard.speed(0)
turtle.colormode(255)
print(richard.position())

coordiantes = []

for i in range((-5), 6):
    for j in range((-5), 6):
        x = j*50
        y = i*50
        coordiantes.append((x, y))


for k in range(len(coordiantes)):
    richard.setposition(coordiantes[k])
    richard.dot(20, random.choice(color_list))


screen = Screen()
screen.exitonclick()