import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(key="Up" ,fun=snake.up)
screen.onkey(key="Down" , fun=snake.down)
screen.onkey(key="Left" ,fun=snake.left)
screen.onkey(key="Right" , fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score = ScoreBoard()
    score.update_score()

    if snake.head.distance(food) < 10:
        snake.extend()
        food.refresh()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()