import turtle
import pandas

screen = turtle.Screen()
screen.title("London Boroughs Game")
image = "blank_boroughs.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("london_boroughs.csv")
all_boroughs = data.boroughs.tolist()

guessed_boroughs = []


while len(guessed_boroughs) < 32:
    answer_borough = screen.textinput(title=f"{len(guessed_boroughs)}/32 boroughs correct",
                                      prompt="Whats another boroughs name?").title()
    if answer_borough == "Exit":
        missing_boroughs = [borough for borough in all_boroughs if borough not in guessed_boroughs]
        new_data = pandas.DataFrame(missing_boroughs)
        new_data.to_csv("boroughs_to_learn.csv")
        break
    if answer_borough in all_boroughs:
        guessed_boroughs.append(answer_borough)
        t = turtle.Turtle()
        t.hideturtle()
        t.color("purple")
        t.penup()
        borough_data = data[data.boroughs == answer_borough]
        t.goto(int(borough_data.x), int(borough_data.y))
        t.write(borough_data.boroughs.item())

