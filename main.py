from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
screen.tracer(0)

game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    






screen.exitonclick()
