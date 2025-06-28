from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segments(position)

    def add_segments(self,position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("blue")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_segment(self):
        self.add_segments(self.segments[-1].position())


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]



    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            x_corr=self.segments[seg_num-1].xcor()
            y_corr=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x_corr,y_corr)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
