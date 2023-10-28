import time
from turtle import Screen
import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


finish_line = player.FINISH_LINE_Y
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_turtle = Player()
car = CarManager()
score = Scoreboard()
level = 1

screen.listen()
screen.onkey(player_turtle.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    screen.update()

    car.create_car()
    car.move_cars()

    for cars in car.all_cars:
        if cars.distance(player_turtle) < 20:
            score.game_over()
            game_is_on = False

    if player_turtle.ycor() > finish_line:
        player_turtle.bring_back()
        score.level_up()
        car.faster()




screen.exitonclick()

















