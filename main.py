from turtle import Screen
from scoreboard import Scoreboard 
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(f"Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
game_is_on = True

speed = 0.1
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.resetPosition()
        scoreboard.addScore()
        # speed -= 0.1 adicionar velocidade/dificuldade
        snake.growSnake()
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        scoreboard.gameOver()
        
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameOver()

screen.exitonclick()
