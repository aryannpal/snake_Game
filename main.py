import time
from turtle import  Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Welcome To my Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)


is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food)<17:
        snake.extend_segment()
        food.refresh()
        scoreboard.change_score()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    #Detect Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()