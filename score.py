from turtle import Turtle
FONT=("courier",12,"normal")
ALIGN="center"

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score=0
        self.setposition(0,270)
        self.hideturtle()
        self.initial()


    def initial(self):
        self.write(f"score={self.score}", align=ALIGN, font=FONT)

    def update(self):
        self.score+=1
        self.clear()
        self.write(f"score={self.score}", align=ALIGN,font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write(f"GAME OVER", align=ALIGN,font=("courier",24,"bold"))
