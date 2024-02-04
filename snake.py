from turtle import Turtle,Screen
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOV_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.heads=self.segments[0]
    def create_snake(self):
        for positions in STARTING_POSITION:
            self.add_segment(positions)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def add_segment(self,positions):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(positions)
        self.segments.append(tim)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
           new_x = self.segments[seg_num - 1].xcor()
           new_y = self.segments[seg_num - 1].ycor()
           self.segments[seg_num].goto(new_x, new_y)
        self.heads.forward(MOV_DISTANCE)

    def up(self):
        if self.heads.heading()!=DOWN:
            self.heads.setheading(UP)
    def down(self):
        if self.heads.heading() != UP:
           self.heads.setheading(DOWN)
    def left(self):
        if self.heads.heading() != RIGHT:
           self.heads.setheading(LEFT)
    def right(self):
        if self.heads.heading() != LEFT:
           self.heads.setheading(RIGHT)
