from turtle import Turtle

SPEED_INCREASE = 1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def speed_increase_x(self):
        if abs(self.x_move) == self.x_move:
            self.x_move += SPEED_INCREASE
        else:
            self.x_move -= SPEED_INCREASE

    def speed_increase_y(self):
        if abs(self.y_move) == self.y_move:
            self.y_move += SPEED_INCREASE
        else:
            self.y_move -= SPEED_INCREASE

    def reset_position(self):
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.bounce_x()



