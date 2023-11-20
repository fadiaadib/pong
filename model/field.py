from turtle import Turtle
from constants import *


class Field(Turtle):
    def __init__(self):
        super().__init__('square')

        self.hideturtle()
        self.penup()
        self.goto(x=0, y=SCREEN_HEIGHT / 2)
        self.pencolor(FIELD_COLOR)
        self.pensize(5)
        self.setheading(270)
        self.draw_center_line()

    def draw_center_line(self):
        while self.ycor() > -SCREEN_HEIGHT / 2:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(10)
