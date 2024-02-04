from turtle import Screen
import time
from snake import Snake
from food import Food
from score import scoreboard
sc=Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title("MY SNAKE GAME")

segments=[]
sc.tracer(0)

sn=Snake()
food=Food()
score=scoreboard()
sc.listen()
sc.onkey(sn.up,"Up")
sc.onkey(sn.down,"Down")
sc.onkey(sn.left,"Left")
sc.onkey(sn.right,"Right")

game_is_on=True

while game_is_on:
    sc.update()
    time.sleep(0.1)
    sn.move()
   #detect collision with food
    if sn.heads.distance(food)<15:
        food.refresh()
        sn.extend()
        score.update()

    #detect collision with wall
    if sn.heads.xcor()>280 or sn.heads.xcor()<-280 or sn.heads.ycor()>280 or sn.heads.ycor()<-280:
        game_is_on=False
        score.game_over()
        print("you lost")

    #detect collision with its own tail
    for segment in sn.segments[1:]:
        if sn.heads.distance(segment) < 10:
            game_is_on=False
            score.game_over()


sc.exitonclick()
