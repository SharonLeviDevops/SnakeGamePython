import time
from turtle import Screen, Turtle

screen = Screen()
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in starting_pos:
            self.add_snake(position)

    def add_snake(self,position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segment.append(new_snake)

    def extend(self):
        self.add_snake(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
     if self.head.heading() != down:
        self.head.setheading(up)

    def down(self):
       if self.head.heading() != up:
        self.head.setheading(down)

    def left(self):
       if self.head.heading() != right:
        self.head.setheading(left)

    def right(self):
       if self.head.heading() != left:
        self.head.setheading(right)
