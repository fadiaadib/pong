import random
from turtle import Turtle
from helpers import *


class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')

        self.color(BALL_COLOR)
        self.shapesize(BALL_SIZE, BALL_SIZE)
        self.speed('fastest')
        self.penup()
        self.restart()
        self.speed = 3

    def restart(self):
        self.goto(x=0, y=0)

        angle = 61
        while 60 < angle < 120 or 240 < angle < 300:
            angle = random.randint(*BALL_ORIENT)
        self.setheading(angle)

    def bounce_wall(self):
        if is_close(self.ycor(), SCREEN_HEIGHT/2) or is_close(self.ycor(), -SCREEN_HEIGHT/2):
            self.setheading(360 - self.heading())

    def bounce_paddle(self, player):
        if is_close(self.xcor(), player.paddle.xcor()):
            n, s = player.paddle.bounds()
            if n <= self.ycor() <= s:
                self.setheading(180 - self.heading())
                self.speed += BALL_SPEED_INC

    def move(self):
        self.forward(self.speed)
