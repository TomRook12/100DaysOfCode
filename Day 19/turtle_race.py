from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
all_turtles = []

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + turtle_index * 33.33)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



#def turtle_creator(name, number):
#    name = Turtle(shape="turtle")
#    name.color(colors[number])
#    name.penup()
#    name.goto(x=-230, y=-100 + number*33.33)
#
#turtle_creator("tim", 0)
#turtle_creator("steve", 1)
#turtle_creator("jenny", 2)
#turtle_creator("barry", 3)
#turtle_creator("susan", 4)
#turtle_creator("jeremy", 5)

screen.exitonclick()
