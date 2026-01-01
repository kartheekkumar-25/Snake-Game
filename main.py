from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

food=Food()
score=Scoreboard()
sc=Screen()
sc.setup(600,600)
sc.bgcolor("darkseagreen")
sc.title("Buss Buss Game")
sc.listen()
sc.tracer(0)

crawl=True
snake=Snake()

#keyboard controls
sc.onkey(snake.up,"Up")
sc.onkey(snake.down,"Down")
sc.onkey(snake.left,"Left")
sc.onkey(snake.right,"Right")

#main game group
while(crawl):
    snake.move()

    #collision with snake body
    if snake.tailcheck()==False:
        crawl=False
        score.gameover()

    #collision with food
    if snake.head.distance(food)<=15:
        snake.addseg()
        food.refresh()
        score.score+=1
        score.refresh()

    #collision with wall
    if snake.head.xcor()==-300 or snake.head.xcor()==300 or snake.head.ycor()==-300 or snake.head.ycor()==300:
        crawl=False
        score.gameover()
    sc.update()
    time.sleep(0.2)


sc.exitonclick()