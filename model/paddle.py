from turtle import Turtle
from helpers import *


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__('square')

        self.setheading(90)
        self.color(PADDLE_COLOR)
        self.shapesize(PADDLE_WIDTH/CONV, PADDLE_HEIGHT/CONV)
        self.penup()
        self.goto(x_pos, 0)
        self.speed('fastest')
        self.sound = 'paddle'

    def bounds(self):
        return self.ycor()-PADDLE_HEIGHT/2, self.ycor()+PADDLE_HEIGHT/2

    def check_bounce(self, ball):
        if is_close(ball.xcor(), self.xcor()):
            n, s = self.bounds()
            if n <= ball.ycor() <= s:
                audio.play(self.sound)
                return True
        return False
