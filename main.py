from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# h g " '
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

snake = Snake()
snake.body[0].shape("triangle")
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')
screen.onkey(snake.left, 'a')

start = True
while start:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.body[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

    if snake.body[0].xcor() > 290 or snake.body[0].xcor() < -290 or snake.body[0].ycor() > 290 or snake.body[
        0].ycor() < -290:
        snake.walkthrough()

    for seg in snake.body[1:]:
        if snake.body[0].distance(seg) < 10:
            start = False
            scoreboard.game_over()

screen.exitonclick()
