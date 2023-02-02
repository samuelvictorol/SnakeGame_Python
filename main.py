from turtle import Screen
from snake import Snake
import time

player = str(input("Nome do jogador: "))

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(f"Snake Game | {player}")
screen.tracer(0)

snake = Snake(player)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
