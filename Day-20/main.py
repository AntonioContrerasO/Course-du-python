from turtle import Screen
import time
from food import Food
from Snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    food.colorful()

    #Colission with food
    if snake.snake[0].distance(food) < 15:
        food.refresh()
        scoreboard.plus_score()
        snake.grow()

    # Colission whit walls
    if (snake.snake[0].xcor() > 290 or snake.snake[0].xcor() < -300
            or snake.snake[0].ycor() > 295 or snake.snake[0].ycor() < -295):
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
