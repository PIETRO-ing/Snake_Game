from turtle import Turtle, Screen
import time

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

#snake attributes: positions(by default 0,-20,-40), color, shape
#snake functionality: create, move together, listen to keyboard

class Snake:
    def __init__(self) -> None:
        self.positions = [0, -20, -40]
        self.shape = 'square'
        self.color = 'white'
        self.segments = []
        self.move_forward = 10
        # self.head = self.segments[0]
    
    def create_snake(self):
        for i in self.positions:
            new_segment =Turtle(shape=self.shape)
            new_segment.color(self.color)
            new_segment.penup()
            new_segment.goto(i,0)
            new_segment.speed(1)
            self.segments.append(new_segment)
    
    def move(self):
        for i in range(2,0,-1):
            new_x_cor = self.segments[i - 1].xcor()
            new_y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x_cor,new_y_cor)
        self.segments[0].forward(self.move_forward)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
        

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
