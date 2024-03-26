from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

segments = []
#turtle dimension is 20px X 20px
for i in range(0,-60,-20):
   new_segment =Turtle(shape='square')
   new_segment.color('white')
   new_segment.penup()
   new_segment.goto(i,0)
   new_segment.speed(1)
   segments.append(new_segment)

game_is_on = True
while game_is_on:
   screen.update()
   time.sleep(0.1)
   for i in range(2,0,-1):
      new_x_cor = segments[i - 1].xcor()
      new_y_cor = segments[i - 1].ycor()
      segments[i].goto(new_x_cor,new_y_cor)
   segments[0].forward(10)
   

screen.exitonclick()