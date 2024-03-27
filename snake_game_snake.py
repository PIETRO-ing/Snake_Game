from turtle import Turtle, Screen
import time

#snake attributes: positions(by default 0,-20,-40), color, shape
#snake functionality: create, move

class Snake:
    def __init__(self) -> None:
        self.positions = [0, -20, -40]
        self.shape = 'square'
        self.color = 'white'
        self.segments = []
    
    def create_snake(self):
        for i in self.positions:
            new_segment =Turtle(shape=self.shape)
            new_segment.color(self.color)
            new_segment.penup()
            new_segment.goto(i,0)
            # new_segment.speed(1)
            self.segments.append(new_segment)
    
    def move(self):
        for i in range(2,0,-1):
            new_x_cor = self.segments[i - 1].xcor()
            new_y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x_cor,new_y_cor)
        self.segments[0].forward(20)
