from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.title("Py snake game")

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()

    # detecting snake collision with food
    if snake.head.distance(food) < 15:
        food.reset_food()
        snake.extend()
        score.update_scoreboard()
        print("Eaten up")

    # calling game when snake exceeds the screen
    if snake.head.xcor() > 300 or snake.head.xcor() < - 300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        score.game_over()

    # calling game when the snake bites itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
