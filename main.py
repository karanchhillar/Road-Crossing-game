import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.cars:
        # if car.distance(player) < 28 and player.ycor()-car.ycor() < 20  :
        if  car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            screen.exitonclick()

    if player.ycor() > 280:
        player.reset_level_up()
        scoreboard.level_up()
        car_manager.increase_speed()

