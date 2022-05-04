from turtle import Screen, Turtle
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


ball = Turtle()
ball.color("white")
ball.penup()
ball.shape("circle")
ball.goto(0, 0)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    r_paddle
    l_paddle
    ball.forward(20)



screen.exitonclick()
