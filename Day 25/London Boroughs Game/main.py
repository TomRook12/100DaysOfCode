import turtle
import pandas

screen = turtle.Screen()
screen.title("London Boroughs Game")
image = "blank_boroughs.gif"
screen.addshape(image)
turtle.shape(image)

answer_borough = screen.textinput(title="Guess the borough", prompt="Whats another boroughs name?")



#screen.exitonclick()