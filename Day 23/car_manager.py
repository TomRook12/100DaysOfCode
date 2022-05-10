from turtle import Turtle
import random


CAR_COLOR = ["red", "green", "blue", "orange", "pink", "grey"]
Y_SPAWN = 180
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10

class CarManager():

        def __init__(self):
            self.all_cars = []
            self.car_speed = STARTING_MOVE_DISTANCE

        def create_car(self):
            random_chance = random.randint(1,6)
            if random_chance == 1:
                new_car = Turtle("square")
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.penup()
                new_car.color(random.choice(CAR_COLOR))
                new_car.goto(x=300, y=random.randint(-230, 230))
                self.all_cars.append(new_car)

        def move_cars(self):
            for car in self.all_cars:
                car.backward(STARTING_MOVE_DISTANCE)

        def level_up(self):
            self.car_speed += MOVE_INCREMENT





