from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


# Screen Setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
snake = Snake() 
food = Food()
scoreboard = ScoreBoard()
is_game_on = True

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.right,'Right')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(screen.bye,'q')
# screen.onkey(snake.extend_segment,'a')

def game_over():
    is_game_on= False
    scoreboard.game_over()



while is_game_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.refresh()

    #  Detect collision with wall
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        game_over()

    
       




screen.exitonclick()
