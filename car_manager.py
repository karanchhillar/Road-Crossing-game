import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.number = 2


    def create_cars(self):
        random_no = random.randint(1, 6)
        if random_no == 1:
            tim = Turtle("square")
            tim.penup()
            tim.setheading(180)
            tim.shapesize(stretch_len=2, stretch_wid=1)
            no = random.randint(0, 5)
            tim.color(COLORS[no])
            yaxis = random.randint(-250, 250)
            tim.goto(300, yaxis)
            self.cars.append(tim)

    def move(self):
        for cars in self.cars:
            cars.fd(STARTING_MOVE_DISTANCE + self.number*MOVE_INCREMENT)

    def increase_speed(self):
        self.number += 1
    


        

        
